import pytesseract
import os
import os.path
import argparse
import cv2
import tempfile
import os
from pdf2image import convert_from_path, pdfinfo_from_path
from alive_progress import alive_bar



#checks if tesseract is installed
try:
    pytesseract.get_tesseract_version() 
except:
    print("Please install Tesseract.")
    print("See readme for details.")
    exit()
        



#creates temp dir for image storage
temp_dir = tempfile.TemporaryDirectory()
temp_dir_final = temp_dir.name

#parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p","--pdf",required=True, help="path to pdf")
args=vars(ap.parse_args())

pdf_file=args["pdf"]

if os.path.isfile(pdf_file)!=True:
    print("Invalid filepath")
    exit()
    


try:
   pdfinfo_from_path(pdf_file, userpw=None)
except:
    print("Please install poppler")
    exit()



pdfinfo=pdfinfo_from_path(pdf_file, userpw=None)
maxPages = pdfinfo["Pages"]




def wipeOutput():
    #could be prompt for rewrite of old output file here
    f=open("output.txt","w")
    f.write("")
    f.close()

wipeOutput()
def processpage(images,page):
   # saves images
        for i in range(len(images)):
            images[i].save(temp_dir_final+'/page'+str(i+page)+'.jpg','JPEG')
            #progress bar updater
            bar(((i+page)/maxPages)/4)


def converttext():
    f=open("output.txt","a")
    #array so we can add file names to it, to sort
    file_list=[]
    #go through array and add to file_list
    for filename in os.listdir(temp_dir_final):
        file_list.append(filename)
    #reverse list of names since they seem to be backwards initially
    file_list.reverse()  
    #i counter helps with progress bar
    i=0;
    #convert jpg to text
   # with alive_bar(maxPages, manual=True) as bar:
    for filename in file_list:    
        try:
            image = cv2.imread(temp_dir_final+"/"+filename)
            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(image)
            f.write(text)
        except:
            print("An error occured")
        i=i+1 #iterate i to help with progress bar
        bar(((i/maxPages)*.75)+.25)
    f.close()



print("Converting PDF to JPEG")


with alive_bar(100, manual=True) as bar:
    for x in range(1):
        for page in range(1, maxPages+1,10):
            #converts pdfs to jpeg
            images = convert_from_path(pdf_file, dpi=200, first_page=page, last_page= min(page+10-1,maxPages))            
            processpage(images,page)
     
    print("Converting JPEG to Text via Tesseract")
    converttext()
temp_dir.cleanup()
