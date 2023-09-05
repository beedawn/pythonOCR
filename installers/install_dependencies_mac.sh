#!/bin/bash

# Define the Tesseract, Poppler, and Python URLs
tesseractURL="https://github.com/UB-Mannheim/tesseract/wiki"
popplerURL="https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip"
pythonURL="https://www.python.org/ftp/python/3.8.12/python-3.8.12-macosx10.9.pkg"
requirementsFile="requirements.txt"

# Install Homebrew if not already installed
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
fi

# Install Tesseract and Poppler via Homebrew
echo "Installing Tesseract and Poppler via Homebrew..."
brew install tesseract poppler

# Install Python if not already installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python..."
    curl -o python.pkg "$pythonURL"
    sudo installer -pkg python.pkg -target /
    rm python.pkg
fi

# Install Python packages from requirements.txt
echo "Installing Python packages from $requirementsFile..."
pip3 install -r "$requirementsFile"

echo "Installation complete."
