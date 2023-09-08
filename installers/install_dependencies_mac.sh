#!/bin/bash

# Define the Tesseract, Poppler, and Python URLs
tesseractURL="https://github.com/UB-Mannheim/tesseract/wiki"
popplerURL="https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip"
pythonURL="https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg"
requirementsFile="requirements.txt"

# Install Homebrew if not already installed
if ! command brew -v &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    echo "Please run these commands, and run the installer again."
    echo "(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/$USER/.zprofile"
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"'
    exit 0
fi


# Install Tesseract and Poppler via Homebrew
if ! brew list tesseract &> /dev/null; then
    echo "Installing Tesseract via Homebrew..."
    brew install tesseract
fi

if ! brew list poppler &> /dev/null; then
    echo "Installing Poppler via Homebrew..."
    brew install poppler
fi


# Get the Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')

# Check if the version is greater than or equal to 3.10
if [ "$(printf '%s\n' "3.10" "$python_version" | sort -V | head -n 1)" = "3.10" ]; then
    echo "Python version $python_version is at least 3.10."
else
    echo "Python version $python_version is below 3.10."
    echo "Installing Python 3.10.11..."
    #curl -o python-3.10.11-macos11.pkg "$pythonURL"
    #sudo installer -pkg python-3.10.11-macos11.pkg -target /
    #rm python-3.10.11-macos11.pkg
    brew install python@3.10
fi


# Install Python if not already installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python..."
    #curl -o python-3.10.11-macos11.pkg "$pythonURL"
    #sudo installer -pkg python-3.10.11-macos11.pkg -target /
    #rm python-3.10.11-macos11.pkg
fi

# Install Python packages from requirements.txt
echo "Enter requirements file path (e.g., ./requirements.txt):"
read requirementsFile
echo "Installing Python packages from $requirementsFile..."

pip3 install -r "$requirementsFile"

echo "Installation complete."
