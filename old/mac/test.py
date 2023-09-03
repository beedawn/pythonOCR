import subprocess

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
item=StringVar()
output=StringVar()
console_out=StringVar()

root.title("pythonOCR")

def select_file():
    file = asksaveasfile(filetypes =[('TXT', '*.txt')])
    
    if file is not None:
        #content = file.read()
        #print(content)
        print(file.name)
        output.set(file.name)
        file.close()




def open_file():
    file = askopenfile(mode ='r', filetypes =[('PDF', '*.pdf')])
    if file is not None:
        #content = file.read()
        #print(content)
        print(file.name)
        item.set(file.name)
        
def save_file():
    console_out.set("")
    print(output.get()) 
    print(len(output.get()))
    console_out.set("Processing")
    if len(output.get()) >0:
        process = subprocess.run("python3 ./firstocr.py -p '"+item.get()+"' -o '"+output.get()+"'", shell=True, text=True)
        if process.returncode==0:
            console_out.set("Complete.")
        else:
            console_out.set(process.stdout)
    else:
        process = subprocess.run("python3 ./firstocr.py -p '"+item.get()+"'", shell=True, text=True)
        if process.returncode==0:
            console_out.set("Complete.")
        else:
            console_out.set(process.stdout)

Button(root, text ='Process', command = lambda:save_file()).grid(column=2,row=2)

#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="File Input").grid(column=0,row=1)
ttk.Button(frm, text="Open", command= lambda:open_file()).grid(column=1,row=1)
ttk.Label(frm, textvariable = item, width=40).grid(column=2,row=1)
ttk.Label(frm, text="Output").grid(column=0,row=2)
ttk.Button(frm, text="Select", command= lambda:select_file()).grid(column=1,row=2)
ttk.Label(frm, textvariable = output, width=40).grid(column=2,row=2)
ttk.Label(frm, textvariable= console_out).grid(column=0,row=3)

root.mainloop()
