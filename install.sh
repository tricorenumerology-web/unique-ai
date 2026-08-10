#!/data/data/com.termux/files/usr/bin/bash

set -e

REPO_DIR="$HOME/UniqueAI"
MYAI_DIR="$HOME/MyAI"
MODEL_DIR="$MYAI_DIR/models"

MODEL="$MODEL_DIR/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf"

LLAMA_DIR="$HOME/llama.cpp"
LLAMA_SERVER="$LLAMA_DIR/build/bin/llama-server"

echo
echo "=========================================="
echo "          ✦ UNIQUE LOCAL AI"
echo "=========================================="
echo
echo "Installing Unique..."
echo

# ------------------------------------------------
# Termux check
# ------------------------------------------------

if [ ! -d "$PREFIX" ]; then
    echo "ERROR: This installer is designed for Termux."
    exit 1
fi

# ------------------------------------------------
# Packages
# ------------------------------------------------

echo "[1/6] Installing dependencies..."

pkg update -y
pkg install -y \
    python \
    git \
    cmake \
    make \
    clang \
    curl \
    wget

python -m pip install --upgrade pip
python -m pip install rich

# ------------------------------------------------
# Directories
# ------------------------------------------------

mkdir -p "$MYAI_DIR"
mkdir -p "$MODEL_DIR"
mkdir -p "$HOME/.termux/bin"

# ------------------------------------------------
# llama.cpp
# ------------------------------------------------

echo
echo "[2/6] Checking llama.cpp..."

if [ ! -x "$LLAMA_SERVER" ]; then

    echo "llama.cpp not found."
    echo "Downloading source..."

    if [ -d "$LLAMA_DIR/.git" ]; then

        cd "$LLAMA_DIR"

        git pull

    else

        git clone \
            --depth 1 \
            https://github.com/ggml-org/llama.cpp.git \
            "$LLAMA_DIR"

    fi

    cd "$LLAMA_DIR"

    echo
    echo "Building llama.cpp..."
    echo "This may take several minutes."

    cmake -B build \
        -DGGML_NATIVE=OFF \
        -DLLAMA_CURL=OFF

    cmake --build build \
        -j2 \
        --target llama-server

else

    echo "✓ llama-server already installed."

fi

# ------------------------------------------------
# Model
# ------------------------------------------------

echo
echo "[3/6] Checking Qwen model..."

if [ -f "$MODEL" ]; then

    echo "✓ Qwen model already exists."

else

    echo "Downloading Qwen2.5 1.5B Q4_K_M..."
    echo "Approximately 1 GB."

    wget \
        --show-progress \
        -O "$MODEL" \
        "https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf"

fi

# ------------------------------------------------
# Copy application
# ------------------------------------------------

echo
echo "[4/6] Installing Unique..."

mkdir -p "$REPO_DIR"

cp unique.py "$REPO_DIR/unique.py"

mkdir -p "$REPO_DIR/config"

if [ -f config/system.txt ]; then
    cp config/system.txt "$REPO_DIR/config/system.txt"
fi

# ------------------------------------------------
# Launcher
# ------------------------------------------------

echo
echo "[5/6] Creating unique command..."

cat > "$REPO_DIR/start.sh" <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash

python "$HOME/UniqueAI/unique.py"
EOF

chmod +x "$REPO_DIR/start.sh"

ln -sf \
    "$REPO_DIR/start.sh" \
    "$HOME/.termux/bin/unique"

# Add PATH
if ! grep -q 'HOME/.termux/bin' "$HOME/.bashrc" 2>/dev/null; then

    echo 'export PATH="$HOME/.termux/bin:$PATH"' \
        >> "$HOME/.bashrc"

fi

export PATH="$HOME/.termux/bin:$PATH"

# ------------------------------------------------
# Finish
# ------------------------------------------------

echo
echo "[6/6] Installation complete."
echo
echo "=========================================="
echo "          UNIQUE IS READY"
echo "=========================================="
echo
echo "Model : Qwen2.5 1.5B"
echo "Mode  : Offline"
echo "UI    : Unique"
echo
echo "Start with:"
echo
echo "    unique"
echo
echo "=========================================="
echo

unique
