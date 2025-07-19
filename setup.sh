#!/bin/bash

# This script sets up the necessary environment and dependencies for the SVGNim project on Linux.

set -e # Exit immediately if a command exits with a non-zero status.

echo "--- SVGNim Linux Setup ---"

# 1. Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed. Please install it to continue."
    exit 1
fi

# 2. Check for pip
if ! python3 -m pip --version &> /dev/null; then
    echo "❌ Error: pip for Python 3 is not installed. Please install python3-pip."
    exit 1
fi

# 3. Create a virtual environment
VENV_DIR=".venv"
if [ -d "$VENV_DIR" ]; then
    echo "✅ Virtual environment already exists at '$VENV_DIR'."
else
    echo "🐍 Creating Python virtual environment at '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
fi

# 4. Activate the virtual environment for this script
source "$VENV_DIR/bin/activate"

# 5. Install uv (a fast package installer)
echo "📦 Installing 'uv' package manager..."
pip install uv

# 6. Install project dependencies using uv
echo "📦 Installing project dependencies from pyproject.toml..."
uv pip install .

echo ""
echo "✅ --- Setup Complete! ---"
echo ""
echo "To activate the virtual environment in your shell, run:"
echo "source $VENV_DIR/bin/activate"
echo ""
echo "You can then run the GUI with:"
echo "python gui.py"
echo ""
