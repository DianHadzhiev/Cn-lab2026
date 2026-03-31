#!/bin/bash

mkdir -p "$HOME/.local/{bin,share}"
export PATH="$HOME/.local/bin:$PATH"

# check if uv exists, if not install it
if ! command -v uv &>/dev/null; then
    echo "uv could not be found, installing..."
    if command -v wget &>/dev/null; then
        wget -qO- https://astral.sh/uv/install.sh | sh
    elif command -v curl &>/dev/null; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
    elif command -v pip &>/dev/null; then
        pip install uv
    else
        echo "Error: Could not find wget, curl, or pip to install uv. Please install one of these tools and try again."
        exit 1
    fi
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install uv. Please check the installation logs and try again."
        exit 1
    fi
else
    echo "uv is already installed."
fi

if ! command -v uv &>/dev/null; then
    echo "Error: uv is not installed. Please install uv and try again."
    exit 1
fi

# check if .venv exists, if not create it
if [ ! -d ".venv" ]; then
    uv venv --python 3.11.11
else
    echo ".venv already exists."
fi

# activate the virtual environment
source .venv/bin/activate
