import os
import sys
import json
import time
import signal
import subprocess
import urllib.request

from rich.console import Console
from rich.text import Text

console = Console()

# ============================================================
# UNIQUE CONFIG
# ============================================================

HOME = os.path.expanduser("~")

MODEL = os.path.join(
    HOME,
    "MyAI",
    "models",
    "Qwen2.5-1.5B-Instruct-Q4_K_M.gguf"
)

LLAMA_SERVER = os.path.join(
    HOME,
    "llama.cpp",
    "build",
    "bin",
    "llama-server"
)

HOST = "127.0.0.1"
PORT = 8080

API_URL = f"http://{HOST}:{PORT}/v1/chat/completions"
HEALTH_URL = f"http://{HOST}:{PORT}/health"

LOG_FILE = os.path.join(
    HOME,
    "MyAI",
    "server.log"
)

# Android-friendly settings
CONTEXT = "1024"
THREADS = "4"
BATCH = "128"
UBATCH = "64"

server_process = None
started_by_unique = False

messages = []


# ============================================================
# CLEAR
# ============================================================

def clear():
    os.system("clear")


# ============================================================
# UNIQUE ASCII LOGO
# ============================================================

def show_logo():

    console.print()

    logo = r"""
██    ██ ███    ██ ██  ██████ ██    ██ ███████
██    ██ ████   ██ ██ ██      ██    ██ ██
██    ██ ██ ██  ██ ██ ██      ██    ██ █████
██    ██ ██  ██ ██ ██ ██      ██    ██ ██
 ██████  ██   ████ ██  ██████  ██████  ███████
"""

    console.print(
        Text(
            logo,
            style="bold cyan"
        )
    )


# ============================================================
# WELCOME SCREEN
# ============================================================

def welcome_screen():

    clear()

    console.print()

    console.print(
        "╭──────────────────────────────╮"
    )

    console.print(
        "│ ✦ Welcome to Unique          │",
        style="cyan"
    )

    console.print(
        "╰──────────────────────────────╯"
    )

    show_logo()

    console.print(
        "Unique can now be used completely "
        "offline with your local Qwen model."
    )

    console.print()

    console.print(
        "Model: Qwen2.5-1.5B"
    )

    console.print(
        "Engine: llama.cpp"
    )

    console.print(
        "Mode: Offline"
    )

    console.print()


# ============================================================
# SERVER CHECK
# ============================================================

def server_ready():

    try:

        request = urllib.request.Request(
            HEALTH_URL,
            method="GET"
        )

        with urllib.request.urlopen(
            request,
            timeout=2
        ) as response:

            return response.status == 200

    except Exception:

        return False


# ============================================================
# START SERVER
# ============================================================

def start_server():

    global server_process
    global started_by_unique

    if server_ready():
        return True

    if not os.path.isfile(MODEL):

        console.print(
            "\n[red]Model not found:[/red]"
        )

        console.print(MODEL)

        return False

    if not os.path.isfile(LLAMA_SERVER):

        console.print(
            "\n[red]llama-server not found:[/red]"
        )

        console.print(LLAMA_SERVER)

        return False

    console.print()

    console.print(
        "  Loading Unique AI...",
        style="yellow"
    )

    try:

        log = open(
            LOG_FILE,
            "w",
            encoding="utf-8"
        )

        server_process = subprocess.Popen(
            [
                LLAMA_SERVER,

                "-m",
                MODEL,

                "-c",
                CONTEXT,

                "-t",
                THREADS,

                "-b",
                BATCH,

                "-ub",
                UBATCH,

                "--host",
                HOST,

                "--port",
                str(PORT),

                "--log-disable"
            ],

            stdin=subprocess.DEVNULL,

            stdout=log,

            stderr=log,

            start_new_session=True
        )

        started_by_unique = True

    except Exception as error:

        console.print(
            f"\n[red]Could not start AI:[/red] {error}"
        )

        return False

    for i in range(180):

        if server_ready():

            console.print(
                "  [green]● Unique AI ready[/green]"
            )

            time.sleep(0.5)

            return True

        if server_process.poll() is not None:

            console.print(
                "\n[red]Unique AI failed to start.[/red]"
            )

            return False

        time.sleep(1)

    console.print(
        "\n[red]AI startup timed out.[/red]"
    )

    return False


# ============================================================
# STOP SERVER
# ============================================================

def stop_server():

    global server_process

    if not started_by_unique:
        return

    if server_process is None:
        return

    try:

        if server_process.poll() is None:

            server_process.terminate()

            try:

                server_process.wait(
                    timeout=5
                )

            except subprocess.TimeoutExpired:

                server_process.kill()

    except Exception:
        pass


# ============================================================
# STREAM RESPONSE
# ============================================================

def ask_unique(prompt):

    global messages

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    payload = {
        "messages": messages,
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 512,
        "stream": True
    }

    data = json.dumps(
        payload
    ).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    full_answer = ""

    try:

        with urllib.request.urlopen(
            request,
            timeout=300
        ) as response:

            console.print()

            console.print(
                "Unique › ",
                style="bold cyan",
                end=""
            )

            for raw_line in response:

                line = raw_line.decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

                if not line:
                    continue

                if not line.startswith("data:"):
                    continue

                data_line = line[5:].strip()

                if data_line == "[DONE]":
                    break

                try:

                    chunk = json.loads(
                        data_line
                    )

                except json.JSONDecodeError:

                    continue

                choices = chunk.get(
                    "choices",
                    []
                )

                if not choices:
                    continue

                delta = choices[0].get(
                    "delta",
                    {}
                )

                token = delta.get(
                    "content",
                    ""
                )

                if not token:
                    continue

                full_answer += token

                console.print(
                    token,
                    end="",
                    markup=False
                )

                sys.stdout.flush()

        console.print()
        console.print()

        messages.append(
            {
                "role": "assistant",
                "content": full_answer
            }
        )

        return full_answer

    except Exception as error:

        console.print()

        console.print(
            f"[red]Unique error:[/red] {error}"
        )

        return ""


# ============================================================
# CHAT
# ============================================================

def chat():

    global messages

    messages = []

    clear()

    console.print()

    console.print(
        "✦ UNIQUE",
        style="bold cyan"
    )

    console.print(
        "Qwen 2.5 1.5B • Offline",
        style="dim"
    )

    console.print()

    while True:

        try:

            prompt = console.input(
                "You › "
            ).strip()

        except KeyboardInterrupt:

            console.print()

            return

        except EOFError:

            return

        if not prompt:
            continue

        command = prompt.lower()

        if command == "/exit":

            return

        if command == "/new":

            messages = []

            console.print(
                "\n[dim]New conversation started.[/dim]\n"
            )

            continue

        if command == "/clear":

            clear()

            continue

        if command == "/help":

            console.print()

            console.print(
                "/new    New conversation"
            )

            console.print(
                "/clear  Clear screen"
            )

            console.print(
                "/help   Show commands"
            )

            console.print(
                "/exit   Return to menu"
            )

            console.print()

            continue

        ask_unique(prompt)


# ============================================================
# MENU
# ============================================================

def menu():

    while True:

        welcome_screen()

        console.print(
            "Select an option:"
        )

        console.print()

        console.print(
            "› 1. Start Chat",
            style="cyan"
        )

        console.print(
            "  2. Open Workspace"
        )

        console.print(
            "  3. Settings"
        )

        console.print(
            "  4. Exit"
        )

        console.print()

        try:

            choice = console.input(
                "› "
            ).strip()

        except KeyboardInterrupt:

            return

        if choice == "1":

            if start_server():

                chat()

        elif choice == "2":

            console.print()

            console.print(
                "Workspace will be added next.",
                style="yellow"
            )

            input(
                "\nPress ENTER to continue..."
            )

        elif choice == "3":

            console.print()

            console.print(
                "Settings will be added next.",
                style="yellow"
            )

            input(
                "\nPress ENTER to continue..."
            )

        elif choice == "4":

            return

        else:

            console.print(
                "\nInvalid option.",
                style="red"
            )

            time.sleep(1)


# ============================================================
# SIGNAL
# ============================================================

def signal_handler(
    signum,
    frame
):

    stop_server()

    sys.exit(0)


signal.signal(
    signal.SIGINT,
    signal_handler
)

signal.signal(
    signal.SIGTERM,
    signal_handler
)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        menu()

    finally:

        stop_server()
