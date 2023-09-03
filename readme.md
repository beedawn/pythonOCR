

Installer script:
pip install -r requirements.txt



Requires Tesseract:
on Linux: sudo apt-get install tesseract-ocr

on mac: brew install tesseract

on windows please visit: https://github.com/tesseract-ocr/tessdoc for the binary file

https://github.com/UB-Mannheim/tesseract/wiki


https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe

https://digi.bib.uni-mannheim.de/tesseract/




WINDOWS:



To run your Python script on Windows, you'll need to ensure that you have the necessary dependencies installed and configured correctly. Here's a step-by-step guide to help you get your script up and running on a Windows system:

Install Python:
If you haven't already, download and install Python for Windows from the official Python website (https://www.python.org/downloads/windows/). Make sure to select the option to add Python to your PATH during installation.
Install Tesseract:
Tesseract is used for optical character recognition (OCR) in your script. To install Tesseract on Windows, follow these steps:

Download the Tesseract installer for Windows from the Tesseract GitHub page (https://github.com/UB-Mannheim/tesseract/wiki). Look for the Windows installer and download the executable file.

Run the Tesseract installer, and during installation, make sure to check the option to add Tesseract to your system PATH. This is crucial for your script to find Tesseract.

After installation, open a new command prompt and run tesseract --version to verify that Tesseract is installed and accessible from the command line.

Install Poppler:
Your script uses Poppler for processing PDF files. To install Poppler on Windows, you can follow these steps:

Visit the Poppler for Windows download page: https://github.com/oschwartz10612/poppler-windows/releases.

Download the latest release of Poppler for Windows, which includes both the executable files and the necessary DLLs.

Extract the contents of the downloaded zip file to a directory of your choice.

Add the path to the directory containing the Poppler executable files (e.g., bin folder) to your system PATH. This allows your script to find the Poppler utilities.

Install Python Libraries:
Open a command prompt or terminal and use pip to install the required Python libraries for your script. Run the following commands:


pip install pdf2image
pip install opencv-python
pip install pytesseract
pip install alive-progress

Install Visual Studio build tools:
https://visualstudio.microsoft.com/downloads/
Install the C++ Desktop


Run Your Script:
With all the dependencies installed, you can now run your Python script. Open a command prompt, navigate to the directory where your script is located, and execute it using the following command:

python your_script_name.py -p your_pdf_file.pdf
Replace your_script_name.py with the actual name of your Python script and your_pdf_file.pdf with the path to the PDF file you want to process.





