import pytesseract
import argparse
import cv2
import tempfile
import os
from pdf2image import convert_from_path, pdfinfo_from_path
from alive_progress import alive_bar


def main(gui_input, console_out, gui_output=None):
    current_working_directory = os.path.dirname(os.path.abspath(__file__))
    from sys import platform
    if platform == "linux" or platform == "linux2":
        # linux
        poppler_path = None
    elif platform == "darwin":
        # OS X
        poppler_path = None
    elif platform == "win32":
        # Windows...
        poppler_path = r'C:\Program Files\poppler-23.08.0\Library\bin'
    # checks if tesseract is installed
    try:
        pytesseract.get_tesseract_version()
    except:
        console_out.set("Please install Tesseract.")
        print("Please install Tesseract.")
        print("See readme for details.")

        print("Installer script: pip install -r requirements.txt\nRequires Tesseract: on Linux: sudo apt-get install tesseract-ocr\non mac: brew install tesseract\non windows please visit: https://github.com/tesseract-ocr/tessdoc for the binary file\nhttps://github.com/UB-Mannheim/tesseract/wiki\nhttps://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe\nhttps://digi.bib.uni-mannheim.de/tesseract/")

    # creates temp dir for image storage
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_final = temp_dir.name

    # parse arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-p","--pdf",required=True, help="path to pdf")
    # ap.add_argument("-o","--output",required=False, help="path to output")
    # args=vars(ap.parse_args())

    pdf_file = gui_input

    pdfinfo = pdfinfo_from_path(
        pdf_file, userpw=None, poppler_path=poppler_path)
    maxPages = pdfinfo["Pages"]

    if gui_output is not None:
        output_path = gui_output
        print("output def: " + output_path)
    else:
        output_path = current_working_directory+"/output.txt"
        print("ouput undef: "+output_path)

    def wipeOutput():
        # could be prompt for rewrite of old output file here
        f = open(output_path, "w")
        f.write("")
        f.close()

    wipeOutput()

    def processpage(images, page):
        # saves images
        for i in range(len(images)):
            images[i].save(temp_dir_final+'/page'+str(i+page)+'.jpg', 'JPEG')
            # progress bar updater
            # bar(((i+page)/maxPages)/4)
            # print(i)
            try:
                console_out.set(str(i) + "/" + str(maxPages))
            except Exception as e:
                console_out.set(str(e))

    def converttext():
        f = open(output_path, "a")
        # array so we can add file names to it, to sort
        file_list = []
        # go through array and add to file_list
        for filename in os.listdir(temp_dir_final):
            file_list.append(filename)
        # reverse list of names since they seem to be backwards initially
        file_list.reverse()
        # i counter helps with progress bar
        i = 0
        # convert jpg to text
    # with alive_bar(maxPages, manual=True) as bar:
        for filename in file_list:
            try:
                image = cv2.imread(temp_dir_final+"/"+filename)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                text = pytesseract.image_to_string(image)
                f.write(text)
            except:
                print("An error occured")
            i = i+1  # iterate i to help with progress bar
            # bar(((i/maxPages)*.75)+.25)
            # print(i)
            try:
                console_out.set(str(i) + "/"+str(maxPages))
            except Exception as e:
                console_out.set(str(e))
        f.close()

    print("Converting PDF to JPEG")

    # with alive_bar(100, manual=True) as bar:
    # for x in range(1):
    for page in range(1, maxPages+1, 10):
        # converts pdfs to jpeg
        images = convert_from_path(pdf_file, poppler_path=poppler_path,
                                   dpi=200, first_page=page, last_page=min(page+10-1, maxPages))
        processpage(images, page)

    print("Converting JPEG to Text via Tesseract")
    converttext()
    temp_dir.cleanup()
