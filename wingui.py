import subprocess
import threading
import time
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
item = StringVar()
output = StringVar()
console_out = StringVar()

root.title("pythonOCR")

def select_file():
    file = asksaveasfile(filetypes=[('TXT', '*.txt')])

    if file is not None:
        print(file.name)
        output.set(file.name)
        file.close()

def open_file():
    file = askopenfile(mode='r', filetypes=[('PDF', '*.pdf')])
    if file is not None:
        print(file.name)
        item.set(file.name)

def process_file():
    console_out.set("")
    console_out.set("Processing")
    script_path = os.path.join(os.path.dirname(__file__), "firstocr.py")
    input_path = item.get()
    output_path = output.get()
    
    if len(output_path) > 0:
        cmd = f"{sys.executable} {script_path} -p '{input_path}' -o '{output_path}'"
    else:
        cmd = f"{sys.executable} {script_path} -p '{input_path}'"

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    while process.poll() is None:
        pb.update()
        time.sleep(0.1)

    if process.returncode == 0:
        console_out.set("Complete.")
    else:
        console_out.set(process.stdout)
    
    pb.stop()

def pb_start():
    pb.start()

def pb_stop():
    pb.stop()

pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
pb.grid(column=0, row=2)

Button(root, text='Process', command=lambda: [pb_start(), threading.Thread(target=process_file).start()]).grid(column=0, row=4)

ttk.Label(frm, text="File Input").grid(column=0, row=1)
ttk.Button(frm, text="Open", command=lambda: open_file()).grid(column=1, row=1)
ttk.Label(frm, textvariable=item, width=40).grid(column=2, row=1)
ttk.Label(frm, text="Output").grid(column=0, row=2)
ttk.Button(frm, text="Select", command=lambda: select_file()).grid(column=1, row=2)
ttk.Label(frm, textvariable=output, width=40).grid(column=2, row=2)
ttk.Label(root, textvariable=console_out).grid(column=0, row=3)

root.mainloop()
