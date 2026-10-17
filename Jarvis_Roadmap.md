# Jarvis Development Roadmap

## Project Goal

Build a personal AI assistant for the laptop that can understand text and voice commands, control the desktop, navigate files, use applications, interact with an LLM, and present its state through a small animated orb UI.

---

# Architecture

```text
                         JARVIS
                            │
                    ┌───────┴───────┐
                    │      LLM      │
                    └───────┬───────┘
                            ↓
                     Command Parser
                            ↓
                        Executor
                            ↓
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
            Apps          Files         System
              │             │             │
              └─────────────┼─────────────┘
                            ↓
                           Linux
```

The LLM should generate structured commands, while the executor remains responsible for actually performing actions. The LLM should not receive unrestricted shell access.

---

# Phase 1: Core Command Engine

**Status: In progress**

## Completed

- [x] Command parser
- [x] App opening
- [x] App closing
- [x] File opening
- [x] Directory opening
- [x] Recursive file search
- [x] Volume up
- [x] Volume down
- [x] Mute
- [x] Lock
- [x] Sleep
- [x] Restart
- [x] Brightness up
- [x] Brightness down
- [x] Better error handling
- [-] Command aliases (skipped for now)
- [x] Cleaner parser structure
- [x] Handle ambiguous file results

phase 1 completed on oct 17th 

## Remaining

---

# Phase 2: System Information

Jarvis should be able to retrieve information about the laptop.

Commands/features:

- [ ] Battery status
- [ ] CPU usage
- [ ] RAM usage
- [ ] GPU information
- [ ] GPU usage
- [ ] Storage usage
- [ ] Network information
- [ ] Operating system information
- [ ] CPU temperature
- [ ] GPU temperature

Suggested structure:

```text
system/
├── system.py
├── hardware.py
└── files.py
```

---

# Phase 3: Filesystem & Navigation

Goal: make Jarvis capable of finding and navigating files naturally.

Examples:

```text
open Downloads
find test.py
find all PDFs
open my Jarvis project
find the ResNet report
open the latest PDF
```

Features:

- [ ] Search by filename *
- [ ] Search by extension *
- [ ] Recursive search *
- [ ] Directory navigation **will be done by Local llm maybe**
- [ ] Search from home directory **will be done by Local llm maybe**
- [ ] Search from current directory **will be done by Local llm maybe**
- [ ] Open recent files **will be done by Local llm maybe**
- [ ] Handle multiple matching files **will be done by Local llm maybe**
- [ ] Natural-language file queries **will be done by Local llm maybe**

Example:

```text
User:
    open the satellite dataset

Jarvis:
    searches known locations
    ↓
    finds matching files/directories
    ↓
    asks for clarification if ambiguous
    ↓
    opens selected result
```

---

# Phase 4: Application Control

Expand beyond simple open/close commands.

Examples:

```text
open Firefox
close VS Code
open my project in VS Code
open terminal here
focus Firefox
```

Features:

- [ ] Detect running applications
- [ ] Focus an application
- [ ] Open application
- [ ] Close application
- [ ] Launch applications with arguments
- [ ] Open a file with a specific application
- [ ] Open application in a specific directory

---

# Phase 5: Voice Interface

Only add the voice layer after the text-command system is reliable.

Architecture:

```text
Microphone
    ↓
Speech-to-Text
    ↓
Command / LLM
    ↓
Executor
    ↓
Action
    ↓
Text-to-Speech
```

Features:

- [ ] Wake word
- [ ] Speech recognition
- [ ] Listening state
- [ ] Command processing
- [ ] Text-to-speech
- [ ] Stop/cancel command
- [ ] Voice error handling
- [ ] Background listening

Possible wake words:

```text
Jarvis
Hey Jarvis
Custom wake word
```

---

# Phase 6: Local LLM

Run a local LLM for natural-language understanding.

Initial target:

- Small local model suitable for available VRAM
- Structured output
- Tool/function calling
- Command interpretation
- Context handling

Architecture:

```text
User
 ↓
LLM
 ↓
Structured command
 ↓
Validation
 ↓
Executor
 ↓
System action
```

Example:

```text
User:
    "Could you open that satellite dataset I was working on?"

LLM:
    {
        "intent": "find_file",
        "query": "satellite dataset",
        "location": "~/"
    }

Executor:
    searches filesystem
    ↓
    opens result
```

Important rule:

**The LLM interprets intent. The executor controls the machine.**

---

# Phase 7: Memory & Context

Make Jarvis capable of maintaining useful context.

Features:

- [ ] Short-term conversation context
- [ ] Recent commands
- [ ] Current directory
- [ ] Current applications
- [ ] User preferences
- [ ] Project context
- [ ] Persistent memory
- [ ] Context-aware commands

Example:

```text
User:
    Open the Jarvis project.

Jarvis:
    Opens the project.

User:
    Run the test.

Jarvis:
    Understands that "the test" refers to the Jarvis project.
```

---

# Phase 8: Productivity

Add useful personal-assistant capabilities.

Features:

- [ ] Generate custom emails
- [ ] Draft emails
- [ ] Read selected emails
- [ ] Calendar integration
- [ ] Reminders
- [ ] Notes
- [ ] Clipboard management
- [ ] Web search
- [ ] Summarization
- [ ] Document handling

Example:

```text
Write an email to my professor explaining that I missed the form deadline.
```

Jarvis should generate the draft, but sending should require deliberate user control.

---

# Phase 9: Developer Mode

Make Jarvis useful for engineering and programming work.

Potential capabilities:

```text
open my ROS project
run the simulation
find the URDF
open VS Code
run this Python script
show git status
commit these changes
search my code
explain this error
```

Potential integrations:

- [ ] Git
- [ ] Python
- [ ] ROS2
- [ ] VS Code
- [ ] Terminal
- [ ] Docker
- [ ] MATLAB
- [ ] C/C++
- [ ] Project-specific tools

---

# Phase 10: Orb UI

Build the animated Jarvis orb.

The orb should visually represent the assistant's state.

## States

```text
IDLE
  ↓
WAKE
  ↓
LISTENING
  ↓
THINKING
  ↓
EXECUTING
  ↓
SUCCESS / ERROR
  ↓
IDLE
```

## Animation concepts

### Idle

- Very subtle animation
- Mostly transparent
- Low visual activity

### Wake

- Orb appears
- Expands/pulses
- Indicates that the wake word was detected

### Listening

- Reacts to microphone input
- Shows active listening state

### Thinking

- Internal movement
- Rotating or flowing animation

### Executing

- More active animation
- Represents an action being performed

### Success

- Brief confirmation animation
- Returns to idle

### Error

- Distinct warning/error animation
- Returns to idle

---

# Phase 11: Full Integration

Final architecture:

```text
                         ┌─────────────┐
                         │   ORB UI    │
                         └──────┬──────┘
                                │
                         Voice / Text
                                │
                                ↓
                         ┌─────────────┐
                         │     LLM     │
                         └──────┬──────┘
                                ↓
                       Structured Intent
                                │
                                ↓
                         ┌─────────────┐
                         │   Parser    │
                         └──────┬──────┘
                                ↓
                         ┌─────────────┐
                         │  Executor   │
                         └──────┬──────┘
                                │
             ┌──────────────────┼──────────────────┐
             ↓                  ↓                  ↓
          Apps               Files              System
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ↓
                              Linux
```

---

# Recommended Development Order

1. Core parser/executor
2. System controls
3. Filesystem/navigation
4. System information
5. Application control
6. Voice input/output
7. Local LLM
8. Memory/context
9. Productivity integrations
10. Developer tools
11. Orb UI integration
12. Security, error handling, and polish

---

# Current Project Status

## Completed

```text
[x] Parser foundation
[x] Application opening
[x] Application closing
[x] File opening
[x] Directory opening
[x] Recursive file search
[x] Volume control
[x] Mute
[x] Lock
[x] Sleep
[x] Restart
```

## Current next task

```text
→ Brightness control
```

After brightness:

```text
→ System information
→ Better filesystem/navigation
→ Application control
→ Voice
→ Local LLM
→ Memory
→ Productivity
→ Developer mode
→ Orb UI
```

---

# Design Principles

1. Keep individual modules small.
2. Don't solve problems that don't exist yet.
3. Test each layer independently.
4. Keep the executor deterministic.
5. Let the LLM interpret commands, not directly control the OS.
6. Validate dangerous commands.
7. Prefer structured intents over arbitrary shell commands.
8. Add complexity only when the current layer works reliably.
9. Build features incrementally instead of creating a giant monolithic assistant.
10. Keep the system debuggable.
