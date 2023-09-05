#!/bin/bash

# Define the Tesseract, Poppler, and Python URLs
tesseractURL="https://github.com/UB-Mannheim/tesseract/wiki"
popplerURL="https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip"
pythonURL="https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz"
requirementsFile="requirements.txt"

# Install Tesseract and Poppler via apt
echo "Installing Tesseract and Poppler via apt..."
sudo apt-get update
sudo apt-get install -y tesseract-ocr poppler-utils

# Install Python if not already installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python..."
    curl -o python.tar.gz "$pythonURL"
    tar -xzvf python.tar.gz
    cd Python-3.8.12
    ./configure
    make -j$(nproc)
    sudo make altinstall
    cd ..
    rm -rf Python-3.8.12 python.tar.gz
fi

# Install Python packages from requirements.txt
echo "Installing Python packages from $requirementsFile..."
pip3 install -r "$requirementsFile"

echo "Installation complete."
