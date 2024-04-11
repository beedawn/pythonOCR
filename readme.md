
# pythonOCR

This script will take a PDF file and turn it into raw text using OpenCV and TesseractOCR. The application chunks the PDF processing into 10 images at a time, to avoid memory overflow issues on machines with limited memory.


# Installation:


## Linux: 
>sudo apt-get install tesseract-ocr

>sudo apt-get install poppler

>pip install -r requirements.txt


### Mac: 
Requires Python 3.10+ 

Install homebrew: https://brew.sh/
Run these after installing homebrew, or after your first run of install_dependencies_mac.sh:
>(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/$USER/.zprofile

>eval "$(/opt/homebrew/bin/brew shellenv)"

After installing homebrew, you can use the installers/install_dependencies_mac.sh script to install dependencies. The script installs Python 3.10.11, tesseract, poppler, and homebrew. It then asks for the path for requirements.txt and attempts to install those.

### Windows:

The batch file can be used at installers/install_dependencies_win.bat. Please run the script in both regular and administrator mode.
Before running the script, ensure you have Python in your PATH variable. After running the script you will need to add the poppler/library/bin and Tesseract to your path.


Install Python:
If you haven't already, download and install Python for Windows from the official Python website (https://www.python.org/downloads/windows/). Make sure to select the option to add Python to your PATH during installation.
Install Tesseract:
Tesseract is used for optical character recognition (OCR) in your script. To install Tesseract on Windows, follow these steps:

Download the Tesseract installer for Windows from the Tesseract GitHub page (https://github.com/UB-Mannheim/tesseract/wiki). Look for the Windows installer and download the executable file.

Run the Tesseract installer, and during installation, make sure to check the option to add Tesseract to your system PATH. This is crucial for your script to find Tesseract.

After installation, open a new command prompt and run 
>tesseract --version
to verify that Tesseract is installed and accessible from the command line.


Install Visual Studio build tools:
https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170 (leaner)

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



# Usage
Run Your Script:
With all the dependencies installed, you can now run your Python script. Open a command prompt, navigate to the directory where your script is located, and execute it using the following command:

>python headless.py -p your_pdf_file.pdf

If you'd like to specify output path:
>python headless.py -p your_pdf_file.pdf -o output_file_path
# GUI
If you'd like to use the GUI, run the following script from within the project directory:
> python gui/gui.py




