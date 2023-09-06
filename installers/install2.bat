@echo off
setlocal enabledelayedexpansion

REM Define the Tesseract, Poppler, VC++ redistributable, and Python URLs and installation directories
set "tesseractURL=https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe"
set "tesseractDir=C:\Program Files\Tesseract-OCR"
set "popplerURL=https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip"
set "popplerDir=C:\Program Files\"
set "vcRedist64URL=https://aka.ms/vs/17/release/vc_redist.x64.exe"
set "vcRedist32URL=https://aka.ms/vs/17/release/vc_redist.x86.exe"
set "vcRedistARM64URL=https://aka.ms/vs/17/release/vc_redist.arm64.exe"
set "pythonURL=https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64.exe"
set "requirementsFile=requirements.txt"


REM Install Python if not already installed
if not exist "%LocalAppData%\Programs\Python\Python37\python.exe" (
    echo Installing Python...
    powershell -command "(New-Object Net.WebClient).DownloadFile('%pythonURL%', 'python-3.7.8-amd64.exe')"
    start /wait python-3.7.8-amd64.exe
    del python-3.7.8-amd64.exe
) else (
    echo Python is already installed.
)

REM Add Python to PATH
setx PATH "%PATH%;%LocalAppData%\Programs\Python\Python37\" /M
echo %tesseractDir%
REM Install Tesseract if not already installed
if not exist "%tesseractDir%\tesseract.exe" (
    echo Installing Tesseract...
    mkdir "%tesseractDir%" 2>nul
    pushd "%tesseractDir%"
    powershell -command "(New-Object Net.WebClient).DownloadFile('%tesseractURL%', 'tesseract-ocr-w64-setup-5.3.1.20230401.exe')"
    start /wait tesseract-ocr-w64-setup-5.3.1.20230401.exe
    del tesseract-ocr-w64-setup-5.3.1.20230401.exe
    popd
) else (
    echo Tesseract is already installed.
)

REM Add Tesseract to PATH
setx PATH "%PATH%;%tesseractDir%" /M

REM Install Poppler if not already installed
if not exist "%popplerDir%\bin\pdftotext.exe" (
    echo Installing Poppler...
    mkdir "%popplerDir%" 2>nul
    pushd "%popplerDir%"
    powershell -command "(New-Object Net.WebClient).DownloadFile('%popplerURL%', 'poppler.zip')"
    tar -xf poppler.zip
    del poppler.zip
    popd
) else (
    echo Poppler is already installed.
)

REM Add Poppler to PATH
setx PATH "%PATH%;%popplerDir%\poppler-23.08.0\Library\bin" /M

REM Install the appropriate VC++ redistributable package

echo Installing VC++ Redistributable (64-bit)...
powershell -command "(New-Object Net.WebClient).DownloadFile('%vcRedist64URL%', 'VC_redist.x64.exe')"
start /wait VC_redist.x64.exe
del VC_redist.x64.exe
pause


REM Install Python packages from requirements.txt
echo Installing Python packages from %requirementsFile%...
pip install -r %requirementsFile%

echo Installation complete.
pause