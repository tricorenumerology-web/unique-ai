✦ Unique Local AI

Unique is a lightweight offline AI assistant for Termux on Android, powered by Qwen2.5-1.5B and "llama.cpp".

It provides a simple terminal interface inspired by modern AI coding assistants, while keeping the AI model running locally on your device.

Features

- Fully offline AI
- Qwen2.5-1.5B-Instruct
- Q4_K_M GGUF model
- "llama.cpp" backend
- Simple terminal UI
- Streaming AI responses
- Local conversation memory
- No web UI
- No cloud API required
- One-command installation
- One-command startup
- Designed for Android + Termux

---

Requirements

Before installing Unique, you need:

- Android device
- Termux
- Internet connection for the initial installation
- Approximately 2–3 GB of free storage
- Enough available RAM to run the Qwen model

After the model and required software are installed, AI inference works locally/offline.

---

Installation

Open Termux and run:

curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash

The installer will:

1. Check that you're running Termux
2. Install required packages
3. Install Python and Rich
4. Download/build "llama.cpp" if required
5. Download the Qwen2.5-1.5B Q4_K_M model
6. Install Unique
7. Create the "unique" command
8. Start Unique

The first installation can take some time because "llama.cpp" may need to be built and the Qwen model is approximately 1 GB.

---

Start Unique After Installation

Once installation is complete, simply run:

unique

That's it.

You don't need to manually start "llama-server".

You don't need to manually start Python.

You don't need to open a web browser.

Your normal workflow is:

Termux
   ↓
unique
   ↓
✦ Unique
   ↓
Start Chat
   ↓
Qwen2.5-1.5B

---

First Launch

After installation, you can start Unique with:

unique

You should see the Unique interface:

✦ Welcome to Unique

██    ██ ███    ██ ██  ██████ ██    ██ ███████
██    ██ ████   ██ ██ ██      ██    ██ ██
██    ██ ██ ██  ██ ██ ██      ██    ██ █████
██    ██ ██  ██ ██ ██ ██      ██    ██ ██
 ██████  ██   ████ ██  ██████  ██████  ███████

Unique Local AI
Qwen 2.5 1.5B • Offline

Select an option:

› 1. Start Chat
  2. Open Workspace
  3. Settings
  4. Exit

›

Select:

1

to start chatting.

---

Chat Commands

Inside Unique:

/new

Start a new conversation.

/clear

Clear the terminal screen.

/help

Show available commands.

/exit

Exit the current chat and return to the Unique menu.

---

Example

You › Hello

Unique › Hello! How can I help you today?

You › Write a Python calculator

Unique › Sure. Here's a simple Python calculator...

Responses are streamed as the model generates them.

---

How Unique Works

                UNIQUE
                   │
                   ▼
            Terminal UI
                   │
                   ▼
             llama-server
                   │
                   ▼
        Qwen2.5-1.5B Q4_K_M
                   │
                   ▼
             Android / Termux

The model runs locally on your Android device.

---

Model

Unique currently uses:

Qwen2.5-1.5B-Instruct

Quantization:

Q4_K_M

The model is downloaded during installation rather than stored inside this GitHub repository.

---

Storage

Unique stores the model locally on the device.

The default model location is:

~/MyAI/models/

The application is installed under:

~/UniqueAI/

The "unique" command is created under:

~/.termux/bin/

---

Troubleshooting

"unique: command not found"

Run:

source ~/.bashrc

Then:

unique

If necessary, run:

export PATH="$HOME/.termux/bin:$PATH"

Then:

unique

Check whether llama-server exists

ls ~/llama.cpp/build/bin/llama-server

Check whether the model exists

ls ~/MyAI/models/

You should see:

Qwen2.5-1.5B-Instruct-Q4_K_M.gguf

Check available memory

free -h

If Unique fails to load the model, make sure your device has sufficient available memory.

---

Updating Unique

To get the latest version, run the installer again:

curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash

The installer will reuse the existing model if it is already present.

---

Project Structure

unique-ai/
│
├── install.sh
├── unique.py
├── README.md
├── LICENSE
│
└── config/
    └── system.txt

---

Roadmap

Planned features:

- [ ] Persistent conversation history
- [ ] "/history"
- [ ] "/save"
- [ ] "/load"
- [ ] Code Agent mode
- [ ] Workspace support
- [ ] Local file reading
- [ ] File creation/editing
- [ ] Safe terminal commands
- [ ] Better Markdown rendering
- [ ] Code syntax highlighting
- [ ] Model selection
- [ ] Custom system prompts
- [ ] "/update"
- [ ] Model download manager
- [ ] More lightweight models

---

License

This project is licensed under the MIT License.

See ""LICENSE"" (LICENSE) for details.

The Qwen model has its own applicable license and terms. The project's MIT license applies to the Unique source code, not automatically to third-party models.

---

Author

TriCore Numerology Web

GitHub:

https://github.com/tricorenumerology-web

---

Quick Start

For a fresh Termux installation:

curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash

After installation:

unique

That's all you need to start Unique.
