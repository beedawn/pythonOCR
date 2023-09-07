import subprocess
import threading
import time
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile
from headless import main
current_working_directory = os.path.dirname(os.path.abspath(__file__))

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
item = StringVar()
output = StringVar()
console_out = StringVar()
headless_script = "headless.py"
root.title("pythonOCR")


def select_file():
    file = asksaveasfile(filetypes=[('TXT', '*.txt')])

    if file is not None:
        # print(file.name)
        output.set(file.name)
        file.close()


def open_file():
    file = askopenfile(mode='r', filetypes=[('PDF', '*.pdf')])
    if file is not None:
        # print(file.name)
        item.set(file.name)


def process_file():
    console_out.set("")
    console_out.set("Processing")
    if len(output.get()) > 0:
        try:
            # Call the main function directly
            main(item.get(), console_out, output.get())
            console_out.set("Complete.")
        except Exception as e:
            console_out.set(str(e))
    else:
        # cmd = [sys.executable, os.path.join(current_working_directory, headless_script), '-p', item.get()]
        try:
            # Call the main function directly
            main(item.get(), console_out)
            console_out.set("Complete.")
        except Exception as e:
            console_out.set(str(e))

    pb_stop()


def pb_start():
    pb.start()


def pb_stop():
    pb.stop()


pb = ttk.Progressbar(root, orient='horizontal',
                     mode='indeterminate', length=280)
pb.grid(column=0, row=2)

Button(root, text='Process', command=lambda: [pb_start(), threading.Thread(
    target=process_file).start()]).grid(column=0, row=4)

ttk.Label(frm, text="File Input").grid(column=0, row=1)
ttk.Button(frm, text="Open", command=lambda: open_file()).grid(column=1, row=1)
ttk.Label(frm, textvariable=item, width=40).grid(column=2, row=1)
ttk.Label(frm, text="Output").grid(column=0, row=2)
ttk.Button(frm, text="Select", command=lambda: select_file()
           ).grid(column=1, row=2)
ttk.Label(frm, textvariable=output, width=40).grid(column=2, row=2)
ttk.Label(root, textvariable=console_out).grid(column=0, row=3)
ttk.Button(root, text='Quit', command=root.destroy).grid(column=0, row=6)
root.mainloop()