

# Installer script:
>pip install -r requirements.txt

## Requires Tesseract:
### Linux: 
>sudo apt-get install tesseract-ocr

### Mac: 
>brew install tesseract

### Windows:

Install Python:
If you haven't already, download and install Python for Windows from the official Python website (https://www.python.org/downloads/windows/). Make sure to select the option to add Python to your PATH during installation.
Install Tesseract:
Tesseract is used for optical character recognition (OCR) in your script. To install Tesseract on Windows, follow these steps:

Download the Tesseract installer for Windows from the Tesseract GitHub page (https://github.com/UB-Mannheim/tesseract/wiki). Look for the Windows installer and download the executable file.

Run the Tesseract installer, and during installation, make sure to check the option to add Tesseract to your system PATH. This is crucial for your script to find Tesseract.

After installation, open a new command prompt and run 
>tesseract --version
to verify that Tesseract is installed and accessible from the command line.

Install Poppler:
Your script uses Poppler for processing PDF files. To install Poppler on Windows, you can follow these steps:

Visit the Poppler for Windows download page: https://github.com/oschwartz10612/poppler-windows/releases.

Download the latest release of Poppler for Windows, which includes both the executable files and the necessary DLLs.

Extract the contents of the downloaded zip file to a directory of your choice.

Add the path to the directory containing the Poppler executable files (e.g., bin folder) to your system PATH. This allows your script to find the Poppler utilities.

Install Python Libraries:
Open a command prompt or terminal and use pip to install the required Python libraries for your script. Run the following commands:

>pip install pdf2image
>pip install opencv-python
>pip install pytesseract
>pip install alive-progress

Install Visual Studio build tools:
https://visualstudio.microsoft.com/downloads/
Install the C++ Desktop


# Usage
Run Your Script:
With all the dependencies installed, you can now run your Python script. Open a command prompt, navigate to the directory where your script is located, and execute it using the following command:

>python headless.py -p your_pdf_file.pdf

If you'd like to specify output path:
>python headless.py -p your_pdf_file.pdf -o output_file_path
# GUI
If you'd like to use the GUI, run the following script from within the project:
> python gui.py




