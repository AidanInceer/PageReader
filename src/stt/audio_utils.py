"""Audio processing utilities for silence detection and analysis."""

import logging

import numpy as np

logger = logging.getLogger(__name__)


def calculate_rms(audio_chunk: np.ndarray) -> float:
    """Calculate Root Mean Square (RMS) energy of audio chunk.
    
    RMS provides a measure of the audio signal's amplitude, useful for
    detecting silence vs. speech.
    
    Args:
        audio_chunk: Audio samples as numpy array
    
    Returns:
        RMS energy value (higher = louder)
    """
    return np.sqrt(np.mean(audio_chunk ** 2))


def detect_silence(audio_chunk: np.ndarray, threshold: float = 500.0) -> bool:
    """Detect if audio chunk is silent (below threshold).
    
    Args:
        audio_chunk: Audio samples as numpy array
        threshold: RMS threshold below which audio is considered silent
    
    Returns:
        True if chunk is silent, False if audio detected
    """
    rms = calculate_rms(audio_chunk)
    return rms < threshold


class SilenceDetector:
    """Stateful silence detector for tracking consecutive silent chunks.
    
    This class maintains state across multiple audio chunks to detect
    sustained periods of silence (e.g., 5 seconds) before stopping recording.
    
    Attributes:
        silence_duration: Target silence duration in seconds
        sample_rate: Audio sample rate in Hz
        chunk_duration: Duration of each audio chunk in seconds
        silent_chunks: Count of consecutive silent chunks detected
        required_chunks: Number of chunks needed to reach silence duration
    """

    def __init__(
        self,
        silence_duration: float = 5.0,
        sample_rate: int = 16000,
        chunk_duration: float = 0.1,
        silence_threshold: float = 500.0,
    ):
        """Initialize silence detector.
        
        Args:
            silence_duration: Seconds of silence to detect (default: 5.0)
            sample_rate: Audio sample rate in Hz (default: 16000)
            chunk_duration: Duration of each chunk in seconds (default: 0.1)
            silence_threshold: RMS threshold for silence detection
        """
        self.silence_duration = silence_duration
        self.sample_rate = sample_rate
        self.chunk_duration = chunk_duration
        self.silence_threshold = silence_threshold
        
        # Calculate how many chunks constitute the target silence duration
        self.required_chunks = int(silence_duration / chunk_duration)
        self.silent_chunks = 0
        
        logger.debug(
            f"SilenceDetector initialized: {silence_duration}s = "
            f"{self.required_chunks} chunks of {chunk_duration}s"
        )

    def process_chunk(self, audio_chunk: np.ndarray) -> bool:
        """Process audio chunk and update silence tracking state.
        
        Args:
            audio_chunk: Audio samples from microphone
        
        Returns:
            True if silence threshold reached, False otherwise
        """
        is_silent = detect_silence(
            audio_chunk, threshold=self.silence_threshold
        )
        
        if is_silent:
            self.silent_chunks += 1
            if self.silent_chunks % 10 == 0:  # Log every 1 second
                logger.debug(
                    f"Silence: {self.silent_chunks}/{self.required_chunks} "
                    f"chunks"
                )
        else:
            # Reset counter if sound detected
            if self.silent_chunks > 0:
                logger.debug("Sound detected, resetting silence counter")
            self.silent_chunks = 0
        
        return self.is_silence_threshold_reached()

    def is_silence_threshold_reached(self) -> bool:
        """Check if the required silence duration has been reached.
        
        Returns:
            True if sustained silence detected, False otherwise
        """
        return self.silent_chunks >= self.required_chunks

    def reset(self) -> None:
        """Reset silence detection state."""
        logger.debug("Resetting silence detector")
        self.silent_chunks = 0

    def get_status(self) -> dict:
        """Get current silence detection status.
        
        Returns:
            Dictionary with current state information
        """
        elapsed_silence = self.silent_chunks * self.chunk_duration
        return {
            "silent_chunks": self.silent_chunks,
            "required_chunks": self.required_chunks,
            "elapsed_silence_seconds": elapsed_silence,
            "target_silence_seconds": self.silence_duration,
            "threshold_reached": self.is_silence_threshold_reached(),
        }
