# Data Model: App Modernization

**Feature**: 005-app-modernization  
**Date**: January 21, 2026

---

## Overview

This feature primarily refactors existing code and updates UI—**no new data models are introduced**. This document describes the existing entities for reference and any minor modifications.

---

## Existing Entities (No Changes)

### AppState (Enum)

Represents the current state of the voice input system.

```
AppState
├── IDLE        # Ready for input
├── RECORDING   # Currently recording audio
├── TRANSCRIBING # Processing audio to text
├── PASTING     # Inserting text at cursor
└── ERROR       # Error state
```

### TranscriptionRecord

A saved transcription with metadata.

| Field      | Type     | Description                   |
| ---------- | -------- | ----------------------------- |
| id         | int      | Primary key                   |
| text       | str      | Transcribed text content      |
| timestamp  | datetime | When transcription occurred   |
| duration   | float    | Recording duration in seconds |
| word_count | int      | Number of words transcribed   |

### Setting

Key-value configuration storage.

| Field | Type | Description                                    |
| ----- | ---- | ---------------------------------------------- |
| key   | str  | Setting identifier (e.g., "hotkey")            |
| value | str  | Setting value (JSON-encoded for complex types) |

### Session (TTS)

A text-to-speech reading session.

| Field      | Type     | Description                                 |
| ---------- | -------- | ------------------------------------------- |
| id         | str      | UUID identifier                             |
| title      | str      | Session title (from URL or user)            |
| url        | str      | Source URL (optional)                       |
| text       | str      | Full text content                           |
| position   | int      | Current reading position (character offset) |
| created_at | datetime | Session creation time                       |
| updated_at | datetime | Last update time                            |

---

## Entity Relationships

```
┌─────────────────┐
│     User        │
└────────┬────────┘
         │
         │ configures
         ▼
┌─────────────────┐       creates        ┌─────────────────────┐
│    Settings     │◄────────────────────►│  TranscriptionRecord │
└─────────────────┘                      └─────────────────────┘
         │                                         │
         │ controls                                │ stored in
         ▼                                         ▼
┌─────────────────┐                      ┌─────────────────────┐
│   VoxDatabase   │◄─────────────────────│      SQLite DB      │
└─────────────────┘                      └─────────────────────┘
         │
         │ manages
         ▼
┌─────────────────┐
│    Sessions     │
└─────────────────┘
```

---

## Minor Model Additions

### UITheme (New - Configuration)

Added to Settings as a new configuration option.

| Key                | Type | Default    | Description             |
| ------------------ | ---- | ---------- | ----------------------- |
| `theme`            | str  | `"litera"` | ttkbootstrap theme name |
| `minimize_to_tray` | bool | `true`     | Close button behavior   |

**Storage**: Uses existing Settings key-value system:

```python
database.set_setting("theme", "litera")
database.set_setting("minimize_to_tray", "true")
```

---

## Validation Rules

### TranscriptionRecord

- `text`: Non-empty string, max 100,000 characters
- `duration`: Positive float, max 3600 seconds (1 hour)
- `word_count`: Non-negative integer

### Settings

- `hotkey`: Valid pynput key combination format
- `theme`: Must be valid ttkbootstrap theme name
- `minimize_to_tray`: "true" or "false" string

---

## State Transitions

### AppState Flow

```
          ┌──────────────────────────────────┐
          │                                  │
          ▼                                  │
       ┌──────┐    hotkey     ┌───────────┐  │
       │ IDLE │──────────────►│ RECORDING │  │
       └──────┘               └─────┬─────┘  │
          ▲                         │        │
          │                   hotkey│        │
          │                         ▼        │
          │               ┌──────────────┐   │
          │               │ TRANSCRIBING │   │
          │               └──────┬───────┘   │
          │                      │           │
          │                success           │
          │                      ▼           │
          │               ┌──────────┐       │
          │               │ PASTING  │───────┘
          │               └──────────┘
          │                      │
          │                   error
          │                      ▼
          │               ┌─────────┐
          └───────────────│  ERROR  │
             auto-reset   └─────────┘
```

---

## No Breaking Changes

All existing data remains compatible. The refactoring:

1. Does not modify database schema
2. Does not change data formats
3. Adds optional configuration keys with sensible defaults
