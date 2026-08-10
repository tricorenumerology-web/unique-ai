✦ Unique Local AI

<p align="center">
  <strong>A lightweight offline AI assistant for Android & Termux.</strong>
</p><p align="center">
  Powered by <strong>Qwen2.5-1.5B</strong> + <strong>llama.cpp</strong>
</p><p align="center">"Platform" (https://img.shields.io/badge/Platform-Android-green)
"Environment" (https://img.shields.io/badge/Environment-Termux-blue)
"AI Model" (https://img.shields.io/badge/Model-Qwen2.5--1.5B-purple)
"Mode" (https://img.shields.io/badge/Mode-Offline-orange)
"License" (https://img.shields.io/badge/License-MIT-yellow)

</p>---

Overview

Unique is a lightweight local AI assistant designed to run directly on Android through Termux.

It uses a quantized Qwen2.5-1.5B-Instruct model with "llama.cpp" as the local inference engine.

No web interface.
No cloud API.
No subscription.

Once the model is installed, Unique can generate responses locally on your device.

---

✨ Features

- 🤖 Qwen2.5-1.5B-Instruct
- ⚡ GGUF Q4_K_M quantization
- 🔒 Local/offline inference
- 📱 Designed for Android + Termux
- 💻 Clean terminal interface
- 🌊 Streaming AI responses
- 💬 Conversation memory during a chat
- 🚀 One-command installation
- ▶️ One-command startup
- 🌐 No web UI
- ☁️ No cloud API required

---

🚀 Quick Start

1. Install Unique

Open Termux and run:

curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash

The command above installs the required components and launches Unique when installation finishes.

What the installer does

The installer automatically:

1. Checks that you're using Termux
2. Installs required packages
3. Installs Python and Rich
4. Downloads/builds "llama.cpp" if necessary
5. Downloads the Qwen2.5-1.5B Q4_K_M model
6. Installs the Unique application
7. Creates the "unique" command
8. Launches Unique

«First installation may take some time. "llama.cpp" may need to be compiled and the Qwen model is approximately 1 GB.»

---

▶️ Start Unique

After installation, start Unique anytime with:

unique

That's all.

You do not need to manually start:

- Python
- "llama-server"
- the Qwen model
- a web browser

Your workflow is simply:

Termux
  │
  └── unique
        │
        ▼
   ✦ Unique
        │
        ▼
    Start Chat
        │
        ▼
   Qwen2.5-1.5B

---

💬 Using Unique

After running:

unique

you'll see the Unique terminal interface.

Example:

✦ Welcome to Unique

██    ██ ███    ██ ██  ██████ ██    ██ ███████
██    ██ ████   ██ ██ ██      ██    ██ ██
██    ██ ██ ██  ██ ██ ██      ██    ██ █████
██    ██ ██  ██ ██ ██      ██    ██ ██
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

Then start chatting.

Example:

You › Hello

Unique › Hello! How can I help you today?

You › Write a Python calculator

Unique › Sure. Here's a simple Python calculator...

Responses are streamed while the local model generates them.

---

⌨️ Chat Commands

Inside a Unique chat:

New conversation

/new

Starts a fresh conversation.

Clear screen

/clear

Clears the terminal screen.

Help

/help

Displays available commands.

Exit chat

/exit

Returns to the Unique main menu.

---

🧠 Model

Unique currently uses:

Qwen2.5-1.5B-Instruct

Quantization:

Q4_K_M

Format:

GGUF

The model is downloaded automatically during installation and is not stored inside this GitHub repository.

This keeps the GitHub repository lightweight.

---

⚙️ Architecture

                ✦ UNIQUE
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

The AI model runs locally on your Android device.

---

📁 File Structure

unique-ai/
│
├── install.sh
├── unique.py
├── README.md
├── LICENSE
│
└── config/
    └── system.txt

"install.sh"

One-command installer for Termux.

"unique.py"

Main Unique application and terminal interface.

"config/system.txt"

Default system instructions for Unique.

"LICENSE"

MIT license for the project source code.

---

💾 Installation Locations

After installation, Unique uses the following locations:

Application

~/UniqueAI/

Model

~/MyAI/models/

Qwen model

~/MyAI/models/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf

Command

~/.termux/bin/unique

---

🔄 Update Unique

To install the latest version from this repository, run:

curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash

If the Qwen model is already downloaded, the installer will reuse the existing model instead of downloading it again.

Then start:

unique

---

🛠️ Troubleshooting

"unique: command not found"

Run:

source ~/.bashrc

Then:

unique

If necessary:

export PATH="$HOME/.termux/bin:$PATH"

Then:

unique

---

Check llama-server

Run:

ls ~/llama.cpp/build/bin/llama-server

If the file exists, "llama.cpp" is installed.

---

Check the Qwen model

Run:

ls ~/MyAI/models/

You should see:

Qwen2.5-1.5B-Instruct-Q4_K_M.gguf

---

Check available RAM

Run:

free -h

Running a local AI model requires sufficient available memory.

If the model fails to load, close other applications and try again.

---

📱 Requirements

Minimum

- Android device
- Termux
- Internet connection for initial installation
- Approximately 2–3 GB free storage
- Sufficient RAM for local inference

Internet requirement

Internet is required for the initial installation to download dependencies, "llama.cpp", and the model.

After everything has been installed, the AI inference itself runs locally.

---

🗺️ Roadmap

Unique is still under active development.

Planned features:

- [ ] Persistent chat history
- [ ] "/history"
- [ ] "/save"
- [ ] "/load"
- [ ] Code Agent mode
- [ ] Workspace support
- [ ] Local file reading
- [ ] File creation
- [ ] File editing
- [ ] Safe terminal command execution
- [ ] Better Markdown rendering
- [ ] Code syntax highlighting
- [ ] Model selection
- [ ] Custom system prompts
- [ ] "/update"
- [ ] Model manager
- [ ] More lightweight models
- [ ] Better Android memory optimization

---

🔐 Privacy

Unique is designed around local inference.

Your prompts are sent to the local AI engine running on your device rather than a cloud AI API.

Unique does not require an OpenAI, Gemini, Claude, or other cloud API key.

«Internet access is only needed during installation/downloads unless you add your own external services.»

---

📜 License

This project is licensed under the MIT License.

See ""LICENSE"" (LICENSE) for the full license text.

The MIT license applies to the Unique source code. Third-party models and dependencies may have their own licenses and terms.

---

👨‍💻 Project

Unique Local AI

Developed by TriCore Numerology Web

GitHub:

https://github.com/tricorenumerology-web/unique-ai

---

⭐ Support the Project

If you find Unique useful:

- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Contribute improvements
- 📢 Share the project

---

⚡ Quick Commands

Install

curl -fsSL https://raw.githubusercontent.com/tricorenumerology-web/unique-ai/main/install.sh | bash

Start

unique

Fix command not found

source ~/.bashrc

Check RAM

free -h

---

<p align="center">✦ Unique — Private. Local. Yours.

</p>
