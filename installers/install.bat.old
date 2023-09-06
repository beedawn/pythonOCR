@echo off
setlocal enabledelayedexpansion

REM Define the Tesseract, Poppler, VC++ redistributable, and Python URLs and installation directories
set "tesseractURL=https://github.com/UB-Mannheim/tesseract/wiki"
set "tesseractDir=C:\Program Files\Tesseract-OCR"
set "popplerURL=https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip"
set "popplerDir=C:\Program Files\Poppler"
set "vcRedist64URL=https://aka.ms/vs/17/release/vc_redist.x64.exe"
set "vcRedist32URL=https://aka.ms/vs/17/release/vc_redist.x86.exe"
set "vcRedistARM64URL=https://aka.ms/vs/17/release/vc_redist.arm64.exe"
set "pythonURL=https://www.python.org/ftp/python/3.8.12/python-3.8.12-amd64.exe"
set "requirementsFile=requirements.txt"

REM Check the system architecture
for /f "delims=" %%a in ('wmic os get osarchitecture ^| findstr "64"') do (
    set "is64bit=true"
)

REM Install Python if not already installed
if not exist "%ProgramFiles%\Python38\python.exe" (
    echo Installing Python...
    powershell -command "(New-Object Net.WebClient).DownloadFile('%pythonURL%', 'python-installer.exe')"
    start /wait python-installer.exe
    del python-installer.exe
) else (
    echo Python is already installed.
)

REM Install Tesseract if not already installed
if not exist "%tesseractDir%\tesseract.exe" (
    echo Installing Tesseract...
    mkdir "%tesseractDir%" 2>nul
    pushd "%tesseractDir%"
    powershell -command "(New-Object Net.WebClient).DownloadFile('%tesseractURL%', 'tesseract_installer.exe')"
    start /wait tesseract_installer.exe
    del tesseract_installer.exe
    popd
) else (
    echo Tesseract is already installed.
)

REM Add Tesseract to PATH
setx PATH "%tesseractDir%;%PATH%" /M

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
setx PATH "%popplerDir%\bin;%PATH%" /M

REM Install the appropriate VC++ redistributable package
if "%is64bit%"=="true" (
    echo Installing VC++ Redistributable (64-bit)...
    powershell -command "(New-Object Net.WebClient).DownloadFile('%vcRedist64URL%', 'vc_redist.exe')"
    start /wait vc_redist.exe
    del vc_redist.exe
) else (
    echo Installing VC++ Redistributable (32-bit or ARM64)...
    powershell -command "(New-Object Net.WebClient).DownloadFile('%vcRedist32URL%', 'vc_redist.exe')"
    start /wait vc_redist.exe
    del vc_redist.exe
)

REM Install Python packages from requirements.txt
echo Installing Python packages from %requirementsFile%...
pip install -r %requirementsFile%

echo Installation complete.
