"""UI event constants for Vox application.

Defines standardized event names used for communication between
UI components, ensuring consistent event naming across the application.
"""

from typing import Final

# Main window events
EVENT_WINDOW_CLOSE: Final[str] = "window:close"
EVENT_WINDOW_MINIMIZE: Final[str] = "window:minimize"
EVENT_WINDOW_RESTORE: Final[str] = "window:restore"

# TTS events
EVENT_TTS_START: Final[str] = "tts:start"
EVENT_TTS_STOP: Final[str] = "tts:stop"
EVENT_TTS_PAUSE: Final[str] = "tts:pause"
EVENT_TTS_RESUME: Final[str] = "tts:resume"
EVENT_TTS_PROGRESS: Final[str] = "tts:progress"
EVENT_TTS_COMPLETE: Final[str] = "tts:complete"
EVENT_TTS_ERROR: Final[str] = "tts:error"

# STT events
EVENT_STT_START: Final[str] = "stt:start"
EVENT_STT_STOP: Final[str] = "stt:stop"
EVENT_STT_RECORDING: Final[str] = "stt:recording"
EVENT_STT_PROCESSING: Final[str] = "stt:processing"
EVENT_STT_RESULT: Final[str] = "stt:result"
EVENT_STT_ERROR: Final[str] = "stt:error"

# Settings events
EVENT_SETTINGS_CHANGED: Final[str] = "settings:changed"
EVENT_SETTINGS_RESET: Final[str] = "settings:reset"
EVENT_SETTINGS_SAVED: Final[str] = "settings:saved"

# History events
EVENT_HISTORY_REFRESH: Final[str] = "history:refresh"
EVENT_HISTORY_CLEAR: Final[str] = "history:clear"
EVENT_HISTORY_SELECT: Final[str] = "history:select"
EVENT_HISTORY_DELETE: Final[str] = "history:delete"

# Status events
EVENT_STATUS_UPDATE: Final[str] = "status:update"
EVENT_STATUS_ERROR: Final[str] = "status:error"
EVENT_STATUS_CLEAR: Final[str] = "status:clear"

# System tray events
EVENT_TRAY_SHOW: Final[str] = "tray:show"
EVENT_TRAY_HIDE: Final[str] = "tray:hide"
EVENT_TRAY_EXIT: Final[str] = "tray:exit"

# Tab events
EVENT_TAB_CHANGED: Final[str] = "tab:changed"

# Recording indicator events
EVENT_INDICATOR_SHOW: Final[str] = "indicator:show"
EVENT_INDICATOR_HIDE: Final[str] = "indicator:hide"
EVENT_INDICATOR_UPDATE: Final[str] = "indicator:update"


# Grouped event dictionary for easy access
UI_EVENTS: Final[dict[str, str]] = {
    # Window
    "window_close": EVENT_WINDOW_CLOSE,
    "window_minimize": EVENT_WINDOW_MINIMIZE,
    "window_restore": EVENT_WINDOW_RESTORE,
    # TTS
    "tts_start": EVENT_TTS_START,
    "tts_stop": EVENT_TTS_STOP,
    "tts_pause": EVENT_TTS_PAUSE,
    "tts_resume": EVENT_TTS_RESUME,
    "tts_progress": EVENT_TTS_PROGRESS,
    "tts_complete": EVENT_TTS_COMPLETE,
    "tts_error": EVENT_TTS_ERROR,
    # STT
    "stt_start": EVENT_STT_START,
    "stt_stop": EVENT_STT_STOP,
    "stt_recording": EVENT_STT_RECORDING,
    "stt_processing": EVENT_STT_PROCESSING,
    "stt_result": EVENT_STT_RESULT,
    "stt_error": EVENT_STT_ERROR,
    # Settings
    "settings_changed": EVENT_SETTINGS_CHANGED,
    "settings_reset": EVENT_SETTINGS_RESET,
    "settings_saved": EVENT_SETTINGS_SAVED,
    # History
    "history_refresh": EVENT_HISTORY_REFRESH,
    "history_clear": EVENT_HISTORY_CLEAR,
    "history_select": EVENT_HISTORY_SELECT,
    "history_delete": EVENT_HISTORY_DELETE,
    # Status
    "status_update": EVENT_STATUS_UPDATE,
    "status_error": EVENT_STATUS_ERROR,
    "status_clear": EVENT_STATUS_CLEAR,
    # System tray
    "tray_show": EVENT_TRAY_SHOW,
    "tray_hide": EVENT_TRAY_HIDE,
    "tray_exit": EVENT_TRAY_EXIT,
    # Tab
    "tab_changed": EVENT_TAB_CHANGED,
    # Indicator
    "indicator_show": EVENT_INDICATOR_SHOW,
    "indicator_hide": EVENT_INDICATOR_HIDE,
    "indicator_update": EVENT_INDICATOR_UPDATE,
}
