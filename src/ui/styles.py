"""Theme configuration for the Vox desktop application.

This module provides ttkbootstrap theme configuration and style constants
for consistent visual appearance across all UI components.
"""

import logging
from typing import Final

import ttkbootstrap as ttk

logger = logging.getLogger(__name__)

# Theme configuration - Light mode using litera theme
THEME_NAME: Final[str] = "litera"

# Font family - Windows 11 native look
FONT_FAMILY: Final[str] = "Segoe UI Variable"

# Color palette (aligned with ttkbootstrap litera light theme)
COLORS: Final[dict[str, str]] = {
    "primary": "#4582ec",  # Blue (actions, links)
    "secondary": "#6c757d",  # Gray (secondary actions)
    "success": "#02b875",  # Green (success states)
    "info": "#17a2b8",  # Cyan (informational)
    "warning": "#f0ad4e",  # Orange (warnings)
    "danger": "#d9534f",  # Red (errors, recording indicator)
    "background": "#ffffff",  # White (main background)
    "surface": "#f8f9fa",  # Light gray (cards, panels)
    "foreground": "#333333",  # Dark gray (primary text)
    "muted": "#6c757d",  # Gray (secondary text)
    "border": "#dee2e6",  # Light border color
}

# Font configuration with Windows 11 native font
FONTS: Final[dict[str, tuple[str, int]]] = {
    "heading": (FONT_FAMILY, 14),
    "body": (FONT_FAMILY, 10),
    "small": (FONT_FAMILY, 9),
    "mono": ("Consolas", 10),
}

# Spacing constants (pixels)
PADDING: Final[dict[str, int]] = {
    "small": 5,
    "medium": 10,
    "large": 15,
    "xlarge": 20,
}

# Window dimensions
WINDOW_SIZE: Final[dict[str, int]] = {
    "width": 600,
    "height": 500,
    "min_width": 400,
    "min_height": 350,
}


def create_themed_window(title: str = "Vox") -> ttk.Window:
    """Create a new themed ttkbootstrap window.

    Args:
        title: Window title

    Returns:
        Configured ttkbootstrap Window instance
    """
    window = ttk.Window(
        title=title,
        themename=THEME_NAME,
        size=(WINDOW_SIZE["width"], WINDOW_SIZE["height"]),
        minsize=(WINDOW_SIZE["min_width"], WINDOW_SIZE["min_height"]),
    )

    # Center window on screen
    window.place_window_center()

    logger.debug(f"Created themed window: {title}")
    return window


def configure_styles(style: ttk.Style) -> None:
    """Configure custom styles for the application.

    Args:
        style: ttkbootstrap Style instance to configure
    """
    # Custom style for history list items (light background)
    style.configure(
        "History.TFrame",
        background=COLORS["surface"],
    )

    # Custom style for section headers
    style.configure(
        "Header.TLabel",
        font=FONTS["heading"],
        foreground=COLORS["foreground"],
    )

    # Custom style for muted/secondary text
    style.configure(
        "Muted.TLabel",
        font=FONTS["small"],
        foreground=COLORS["muted"],
    )

    # Custom style for monospace text (hotkey display)
    style.configure(
        "Mono.TLabel",
        font=FONTS["mono"],
        foreground=COLORS["primary"],
    )

    # Light theme status styles
    style.configure(
        "Success.TLabel",
        foreground=COLORS["success"],
    )

    style.configure(
        "Danger.TLabel",
        foreground=COLORS["danger"],
    )

    style.configure(
        "Primary.TLabel",
        foreground=COLORS["primary"],
    )

    logger.debug("Custom styles configured for light theme")
