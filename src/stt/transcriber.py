"""Main transcription orchestrator coordinating recording and STT."""

import logging
import tempfile
from pathlib import Path
from typing import Optional

from src.config import DEFAULT_STT_MODEL, SAMPLE_RATE, SILENCE_DURATION
from src.stt.audio_utils import SilenceDetector
from src.stt.engine import STTEngine
from src.stt.recorder import MicrophoneRecorder
from src.utils.errors import TranscriptionError

logger = logging.getLogger(__name__)


class Transcriber:
    """Orchestrates voice recording and transcription workflow.
    
    This class coordinates the complete speech-to-text pipeline:
    1. Record audio from microphone (with Enter or silence stop)
    2. Save recording to temporary WAV file
    3. Transcribe audio using Whisper model
    4. Display and optionally save transcription result
    
    Attributes:
        model_name: Whisper model size to use
        silence_duration: Seconds of silence before auto-stop
        engine: STT engine instance
        recorder: Microphone recorder instance
    """

    def __init__(
        self,
        model_name: str = DEFAULT_STT_MODEL,
        silence_duration: float = SILENCE_DURATION,
        sample_rate: int = SAMPLE_RATE,
    ):
        """Initialize transcriber with model and recording settings.
        
        Args:
            model_name: Whisper model size (default: "medium")
            silence_duration: Seconds of silence to auto-stop (default: 5.0)
            sample_rate: Audio sample rate in Hz (default: 16000)
        """
        self.model_name = model_name
        self.silence_duration = silence_duration
        self.sample_rate = sample_rate
        
        logger.info(
            f"Initializing Transcriber: model={model_name}, "
            f"silence={silence_duration}s"
        )
        
        # Initialize STT engine
        self.engine = STTEngine(model_name=model_name)
        
        # Initialize silence detector for auto-stop
        self.silence_detector = SilenceDetector(
            silence_duration=silence_duration,
            sample_rate=sample_rate,
        )
        
        # Initialize recorder (will be created fresh for each transcription)
        self.recorder: Optional[MicrophoneRecorder] = None

    def transcribe(
        self,
        output_file: Optional[Path] = None,
        language: str = "en",
    ) -> str:
        """Execute complete transcription workflow.
        
        This is the main entry point that:
        1. Records audio from microphone
        2. Transcribes to text
        3. Displays result
        4. Saves to file if requested
        
        Args:
            output_file: Optional path to save transcription
            language: Language code for transcription (default: "en")
        
        Returns:
            Transcribed text
        
        Raises:
            TranscriptionError: If transcription pipeline fails
        """
        try:
            # Step 1: Record audio
            print("\n🎤 Recording... (Press Enter to stop, or wait for silence)")
            audio_data = self._record_audio()
            
            # Step 2: Process recording (save and transcribe)
            print("\n⏳ Transcribing...")
            text = self._process_recording(audio_data, language)
            
            # Step 3: Display result
            self._display_result(text)
            
            # Step 4: Save to file if requested
            if output_file:
                self._save_result(text, output_file)
            
            return text
            
        except Exception as e:
            if isinstance(e, (TranscriptionError, Exception)):
                logger.error(f"Transcription failed: {str(e)}")
                raise
            raise TranscriptionError(
                f"Transcription pipeline failed: {str(e)}",
                error_code="TRANSCRIPTION_PIPELINE_FAILED",
            ) from e

    def _record_audio(self) -> "np.ndarray":
        """Record audio from microphone with Enter or silence stop.
        
        Returns:
            Numpy array of audio samples
        """
        # Create fresh recorder with silence detection
        self.recorder = MicrophoneRecorder(
            sample_rate=self.sample_rate,
            channels=1,
            silence_detector=self.silence_detector,
        )
        
        # Display device info
        device_info = self.recorder.get_device_info()
        logger.info(f"Recording from: {device_info['device_name']}")
        
        # Start recording
        self.recorder.start_recording()
        
        # Wait for Enter key or silence detection
        self.recorder.wait_for_enter()
        
        # Stop and get audio data
        audio_data = self.recorder.stop_recording()
        
        return audio_data

    def _process_recording(self, audio_data: "np.ndarray", language: str) -> str:
        """Save recording to WAV and transcribe to text.
        
        Args:
            audio_data: Recorded audio samples
            language: Language code for transcription
        
        Returns:
            Transcribed text
        """
        # Save to temporary WAV file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            tmp_path = Path(tmp_file.name)
        
        try:
            # Save audio to WAV
            if self.recorder:
                self.recorder.save_wav(audio_data, tmp_path)
            else:
                raise TranscriptionError(
                    "Recorder not initialized",
                    error_code="RECORDER_NOT_INITIALIZED",
                )
            
            # Transcribe WAV file
            text = self.engine.transcribe_audio(tmp_path, language=language)
            
            return text
            
        finally:
            # Clean up temporary file
            if tmp_path.exists():
                tmp_path.unlink()
                logger.debug(f"Cleaned up temporary file: {tmp_path}")

    def _display_result(self, text: str) -> None:
        """Display transcription result to terminal.
        
        Args:
            text: Transcribed text to display
        """
        print("\n" + "="*60)
        print("📝 Transcription:")
        print("="*60)
        print(text)
        print("="*60 + "\n")

    def _save_result(self, text: str, output_file: Path) -> None:
        """Save transcription to file.
        
        Args:
            text: Transcribed text
            output_file: Path to output file
        """
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(text, encoding="utf-8")
            print(f"✅ Saved to: {output_file}")
            logger.info(f"Transcription saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Failed to save transcription: {e}")
            print(f"⚠️  Warning: Could not save to file: {e}")

    def get_model_info(self) -> dict:
        """Get information about the transcription setup.
        
        Returns:
            Dictionary with configuration details
        """
        return {
            "model_name": self.model_name,
            "silence_duration": self.silence_duration,
            "sample_rate": self.sample_rate,
            "engine_info": self.engine.get_model_info() if self.engine else None,
            "recorder_info": self.recorder.get_device_info() if self.recorder else None,
        }
