# GRACE - Advanced Tkinter UI Framework

**Original Concept:** 2019  
**Developer:** Berith Jeshurun (GliTCH)  
**Language:** Python 3.x  
**Libraries Used:** `tkinter`, `PIL (Pillow)`, `pygame`, `requests`, `keyboard`, `threading`

---

## Overview

GRACE is a **highly customized Tkinter-based UI framework** designed to demonstrate advanced desktop interface capabilities in Python. Originally developed in 2019, it showcases:

- Multi-frame layouts
- Animated network signals
- Tile-based mini-app navigation
- Command-line style input with paste support
- Dynamic image and font handling
- Threaded network and animation updates
- Dark theme integration via `azure.tcl`

---

## Features

### 1. Multi-Layered UI

- **Header Frame (`frame_head`)**: Displays app title and primary visuals.
- **Navigation/Title Bar (`nav_title_head`)**: Hosts tiles and server status.
- **Lower Panel (`frame_down`)**:
  - `frame_down_a` → Animations and system feedback
  - `frame_down_b` → Command-line input interface
  - `frame_down_c` → File system/status display

### 2. Tile-Based Mini Apps

- Supports multiple interactive tiles (`TILE_APP_1`, `TILE_APP_2`, `TILE_APP_3`) with:
  - Keyboard navigation (`Left` / `Right`)
  - Toggle state via `<Control-w>`
  - Visual feedback with active tile highlighting

### 3. Animated Signal System

- Dynamically checks network/server status using threads
- Color-coded signal indicator:
  - **Green** → Online/Connected
  - **Red** → Offline/Disconnected
  - **Yellow** → Backup/Intermediate
- Sequential animated images represent the signal state

### 4. Command-Line Input

- Supports manual command entry
- `<Return>` executes command
- `<Button-3>` triggers system paste
- Entry field can be toggled based on active tile mode

### 5. Dynamic Assets

- Fonts: `Chianti XBd BT`, `Consolas`, `Vudotronic`, `Fruity microfont`
- Images: Sequentially loaded to allow animation (`img_a_a_0` → `img_a_a_21`)
- Sound playback via `pygame.mixer.Sound`

### 6. Miscellaneous

- Dark theme using Azure TCL theme
- Window centered on screen with fixed dimensions
- Thread-safe animations using `Tk.after()`
- Built-in pseudo-console for real-time logging

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/berithjeshurun/GRACE.git
cd GRACE
