# Unique Local AI

> A lightweight, private, offline AI assistant for Android and Termux.

<p align="center">
  <strong>Qwen2.5-1.5B</strong> · <strong>llama.cpp</strong> · <strong>Termux</strong>
</p>

---

## Overview

**Unique Local AI** brings a private AI assistant directly to your Android device.

It runs the AI model locally using **Qwen2.5-1.5B-Instruct** and **llama.cpp**, with a clean terminal interface inspired by modern AI coding assistants.

No browser.  
No cloud API.  
No subscription.

Once installed, your normal startup command is simply:

```bash
unique
```

---

## Features

- Local AI inference
- Qwen2.5-1.5B-Instruct
- Q4_K_M GGUF model
- llama.cpp backend
- Android + Termux support
- Clean terminal interface
- Streaming AI responses
- Conversation memory
- No web UI
- No cloud AI API required
- No API key required
- One-command installation
- One-command startup

---

# Quick Start

## 1. Install Unique

Open **Termux** and run:

```bash
curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash
```

The installer automatically:

1. Checks that you are using Termux
2. Installs required packages
3. Installs Python
4. Installs Rich
5. Downloads/builds llama.cpp when required
6. Downloads the Qwen2.5-1.5B model
7. Installs Unique
8. Creates the `unique` command
9. Starts Unique

> The first installation may take several minutes because llama.cpp may need to be compiled and the Qwen model is approximately 1 GB.

---

# Start Unique

After installation, simply run:

```bash
unique
```

You do not need to manually start `llama-server`.

You do not need to manually start Python.

You do not need to open a browser.

Your normal workflow is:

```text
Termux
   │
   ▼
unique
   │
   ▼
Unique Local AI
   │
   ▼
Start Chat
   │
   ▼
Qwen2.5-1.5B
```

---

# Interface

When Unique starts, it provides a simple terminal interface:

```text
✦ Welcome to Unique

UNIQUE LOCAL AI

Qwen 2.5 1.5B • Offline

Select an option:

› 1. Start Chat
  2. Open Workspace
  3. Settings
  4. Exit

›
```

Select:

```text
1
```

to start chatting.

---

# Chat

Example:

```text
You › Hello

Unique › Hello! How can I help you today?

You › Write a Python calculator

Unique › Sure. Here's a simple Python calculator...
```

Unique streams the response while the local model generates it.

---

# Chat Commands

## New Conversation

Start a new conversation:

```text
/new
```

---

## Clear Screen

Clear the terminal:

```text
/clear
```

---

## Help

Show available commands:

```text
/help
```

---

## Exit

Exit the current chat:

```text
/exit
```

---

# How It Works

```text
                    UNIQUE
                       │
                       ▼
                 Terminal UI
                       │
                       ▼
                 llama-server
                       │
                       ▼
              Qwen2.5-1.5B
                       │
                       ▼
                Android / Termux
```

The AI inference engine runs locally on your Android device.

---

# Model

Unique currently uses:

**Model**

```text
Qwen2.5-1.5B-Instruct
```

**Format**

```text
GGUF
```

**Quantization**

```text
Q4_K_M
```

The model is downloaded automatically during installation.

The model is not stored inside this GitHub repository because of its large file size.

---

# Privacy

Unique is designed for local AI inference.

Your conversations are processed by the local AI model running on your device.

Unique does not require:

- OpenAI API
- Claude API
- Gemini API
- Cloud AI subscription

No cloud AI account is required for local inference.

> Internet access is required during the initial installation to download the required software and model.

After installation, the AI itself can run locally without a cloud AI service.

---

# Requirements

- Android device
- Termux
- Internet connection for initial installation
- Approximately 2–3 GB of free storage
- Sufficient RAM for local model inference

Performance depends on your Android device.

---

# Installation Details

Unique creates the following directories:

## Application

```text
~/UniqueAI/
```

## Model directory

```text
~/MyAI/models/
```

## Qwen model

```text
~/MyAI/models/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf
```

## Unique command

```text
~/.termux/bin/unique
```

---

# Repository Structure

```text
unique-ai/
│
├── install.sh
├── unique.py
├── README.md
├── LICENSE
│
└── config/
    └── system.txt
```

---

# Project Files

## install.sh

The main installation script.

It installs the required dependencies, prepares llama.cpp, downloads the model, configures the `unique` command, and starts Unique.

---

## unique.py

The main Unique application.

It provides:

- Terminal UI
- Chat interface
- Model communication
- Streaming responses
- Conversation handling
- Local AI interaction

---

## config/system.txt

Contains the default system instructions used by Unique.

You can customize this file to change Unique's personality and behavior.

---

## LICENSE

Contains the MIT License for the Unique source code.

Third-party software and AI models may have separate licenses.

---

# Troubleshooting

## `unique: command not found`

Run:

```bash
source ~/.bashrc
```

Then:

```bash
unique
```

If the command is still not found:

```bash
export PATH="$HOME/.termux/bin:$PATH"
```

Then:

```bash
unique
```

---

# Check llama.cpp

To check whether llama-server exists:

```bash
ls ~/llama.cpp/build/bin/llama-server
```

If the file exists, llama.cpp has been installed successfully.

---

# Check the Model

Run:

```bash
ls ~/MyAI/models/
```

You should see:

```text
Qwen2.5-1.5B-Instruct-Q4_K_M.gguf
```

---

# Check Available Memory

Run:

```bash
free -h
```

If the model fails to load, close other Android applications and try again.

Local AI models require RAM while generating responses.

---

# Update Unique

To install the latest version from GitHub, run:

```bash
curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash
```

Then start Unique:

```bash
unique
```

If the model already exists, the installer can reuse the existing model.

---

# Roadmap

Unique is actively being developed.

Planned features:

- [ ] Persistent conversation history
- [ ] `/history`
- [ ] `/save`
- [ ] `/load`
- [ ] Code Agent mode
- [ ] Workspace mode
- [ ] Local file reading
- [ ] File creation
- [ ] File editing
- [ ] Safe terminal commands
- [ ] Code syntax highlighting
- [ ] Markdown rendering
- [ ] Model selection
- [ ] Custom system prompts
- [ ] Automatic updates
- [ ] Model manager
- [ ] More lightweight models
- [ ] Better Android memory optimization
- [ ] Multiple model support

---

# Code Agent

The planned Code Agent will allow Unique to work with local projects.

Example:

```text
You › Inspect this project

Unique ›
Scanning project...

✓ Python files found
✓ Configuration found
✓ Project structure analyzed

What would you like me to change?
```

Future versions will support local file operations and safe command execution.

---

# Local Workspace

Unique is designed to eventually work directly with local projects.

Example:

```text
~/projects/myapp/
```

Unique will be able to understand project files and assist with development without sending the project to a cloud AI service.

---

# Security

Unique is designed to run locally.

Future terminal and file-management features will use confirmation prompts before potentially destructive operations.

For example:

```text
Unique wants to run:

rm -rf example/

Allow? [y/N]
```

---

# Performance

Unique uses the Q4_K_M quantized version of Qwen2.5-1.5B to reduce memory requirements.

Performance depends on:

- Device CPU
- Available RAM
- Android background processes
- Context size
- Number of CPU threads
- Model configuration

For better performance, close unnecessary applications before starting the model.

---

# Offline Mode

After installation, Unique can operate locally.

The basic architecture is:

```text
User
  │
  ▼
Unique UI
  │
  ▼
Local llama.cpp
  │
  ▼
Local Qwen Model
  │
  ▼
Response
```

No cloud AI API is required.

---

# Contributing

Contributions are welcome.

You can contribute by:

- Reporting bugs
- Suggesting features
- Improving the UI
- Improving performance
- Adding model support
- Improving Termux compatibility
- Improving documentation
- Submitting pull requests

---

# Bug Reports

If Unique does not work correctly, please include:

```bash
free -h
```

and:

```bash
ls ~/MyAI/models/
```

Also include the error message shown in Termux.

Do not post private information, API keys, passwords, or personal data.

---

# Project

**Unique Local AI**

Developed by:

**TriCore Numerology Web**

GitHub:

```text
https://github.com/tricorenumerology-web/unique-ai
```

---

# License

Unique Local AI source code is licensed under the MIT License.

See:

```text
LICENSE
```

for the complete license.

Third-party models and dependencies are subject to their respective licenses and terms.

---

# Quick Reference

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash
```

## Start

```bash
unique
```

## Fix `unique` command

```bash
source ~/.bashrc
```

## Check RAM

```bash
free -h
```

## Check Model

```bash
ls ~/MyAI/models/
```

## Check llama.cpp

```bash
ls ~/llama.cpp/build/bin/llama-server
```

---

<p align="center">

<strong>Unique — Private. Local. Yours.</strong>

</p>
