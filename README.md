# Jarvis

Jarvis is a Linux desktop assistant project. The long-term goal is to create a personal assistant that can understand text and voice commands, control desktop applications, navigate the filesystem, report system information, interact with a local LLM, and show its current state through an animated orb interface.

The project is being developed incrementally. The current implementation focuses on the command engine and a standalone PySide6 orb prototype.

## Current Capabilities

The command engine currently supports:

- Opening and closing configured applications
- Opening files and directories with `xdg-open`
- Recursive filename search
- Volume up, volume down, and mute
- Screen locking
- Suspending and restarting the system
- Increasing and decreasing screen brightness
- Selecting a file when a search returns multiple results

Commands are currently text-based and use a small rule-based parser. Voice input, natural-language understanding, and LLM integration are planned but are not implemented yet.

## Architecture

```text
User command
     |
     v
  parser.py       Converts text into a structured intent
     |
     v
  executer.py     Validates the intent and dispatches the action
     |
     +------------------+------------------+
     v                  v                  v
 system/app.py    system/files.py   system/systems.py
 Applications     Filesystem        Linux controls
```

The orb currently runs as a separate UI prototype:

```text
window.py -> PySide6 transparent always-on-top window -> animated orb
```

The intended future flow is:

```text
Voice or text input
	|
	v
Command parser or local LLM
	|
	v
Validation
	|
	v
Executor
	|
	v
Linux action + orb state update
```

The executor should remain responsible for performing actions. An LLM should produce structured commands, not receive unrestricted shell access.

## Project Structure

```text
jarvis/
├── executer.py          Dispatches parsed commands
├── main.py              Reserved for the future application entry point
├── parser.py            Rule-based text command parser
├── test.py              Small manual execution example
├── window.py            Standalone animated orb window
├── Jarvis_Roadmap.md    Detailed development roadmap
└── system/
    ├── app.py           Application aliases and application control
    ├── files.py         File opening and recursive search utilities
    └── systems.py       Volume, brightness, power, and lock commands
```

## Requirements

Jarvis currently targets Linux and expects the following:

- Python 3
- A working desktop session with `xdg-open`
- `amixer` for audio controls
- `brightnessctl` for brightness controls
- `loginctl` and `systemctl` for lock, suspend, and restart commands
- The applications configured in `system/app.py`
- PySide6 for the orb UI

The repository contains a project virtual environment at `venv/`. To install the UI dependency into a new environment:

```bash
python3 -m venv venv
venv/bin/pip install PySide6
```

The system commands are platform-specific and may need to be changed for another Linux distribution or desktop environment.

## Running the Orb

Run the orb with the Jarvis project interpreter:

```bash
venv/bin/python window.py
```

The window is frameless, transparent, always on top, and positioned near the bottom-right of the primary screen. The current visual uses a layered radial glow, volumetric shading, rotating energy arcs, drifting particles, and a subtle breathing pulse.

The orb is currently visual-only. It does not yet receive state changes from the command engine.

## Running the Command Engine

From the project directory, the manual example can be run with:

```bash
venv/bin/python test.py
```

The example searches for `bot.py` inside `~/Downloads` and opens the result when exactly one match is found. For direct use from Python:

```python
from executer import execute_command

execute_command("open Downloads")
execute_command("volume up")
execute_command("find bot.py in Downloads")
```

## Supported Command Forms

### Applications

```text
open firefox
close firefox
open vscode
close terminal
```

Application names and executable mappings are defined in `system/app.py`. The available aliases currently include Firefox, Chrome/browser, VS Code/code, Antigravity, and terminal.

### Files and directories

```text
open Downloads
open /home/user/Documents/report.pdf
find report.pdf in Downloads
```

File searches are recursive and currently match filenames. If multiple paths match, Jarvis prints the results and asks for a selection.

### System controls

```text
volume up
volume down
mute
brightness up
brightness down
lock
sleep
restart
```

Power commands affect the current Linux session immediately, so they should be used carefully.

## Development Status

### Implemented

- Rule-based command parsing
- Application open and close operations
- File and directory opening
- Recursive file search
- Basic Linux audio, brightness, lock, suspend, and restart controls
- Initial error handling and multiple-result selection
- Standalone animated orb prototype

### Planned

- Better handling of ambiguous file results
- System information such as CPU, RAM, GPU, battery, storage, network, and temperature
- More natural filesystem navigation
- Application focus and launch arguments
- Wake word and speech recognition
- Text-to-speech
- Local LLM command interpretation with structured output and validation
- Orb states for idle, wake, listening, thinking, executing, success, and error
- Integration of the orb with voice, command, and executor state

See [Jarvis_Roadmap.md](Jarvis_Roadmap.md) for the complete phased plan.

## Safety and Scope

Jarvis can run commands that lock, suspend, restart, or open applications. Keep the executor explicit and validated as the project grows. In particular, future LLM integration should use a restricted set of structured tools instead of passing arbitrary generated shell commands to the operating system.

## License

No project license has been declared yet.
