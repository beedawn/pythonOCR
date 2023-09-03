import subprocess
import multiprocessing
import time
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
    if len(output.get()) > 0:
        cmd = f"python3 ./firstocr.py -p '{item.get()}' -o '{output.get()}'"
    else:
        cmd = f"python3 ./firstocr.py -p '{item.get()}'"

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

if __name__ == "__main__":
    pb = ttk.Progressbar(frm, orient='horizontal', mode='indeterminate', length=280)
    pb.grid(column=0, row=5)

    Button(root, text='Process', command=lambda: [pb_start(), multiprocessing.Process(target=process_file).start()]).grid(column=2, row=2)

    ttk.Label(frm, text="File Input").grid(column=0, row=1)
    ttk.Button(frm, text="Open", command=lambda: open_file()).grid(column=1, row=1)
    ttk.Label(frm, textvariable=item, width=40).grid(column=2, row=1)
    ttk.Label(frm, text="Output").grid(column=0, row=2)
    ttk.Button(frm, text="Select", command=lambda: select_file()).grid(column=1, row=2)
    ttk.Label(frm, textvariable=output, width=40).grid(column=2, row=2)
    ttk.Label(frm, textvariable=console_out).grid(column=0, row=3)

    root.mainloop()