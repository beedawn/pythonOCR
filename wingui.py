import subprocess
import threading
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

selected_input_file = ""  # Store the selected input file name
selected_output_file = ""  # Store the selected output file name

def select_file():
    global selected_output_file
    file = asksaveasfile(filetypes=[('TXT', '*.txt')])

    if file is not None:
        selected_output_file = file.name  # Store the selected output file name
        print(selected_output_file)
        output.set(selected_output_file)
        file.close()

def open_file():
    global selected_input_file
    file = askopenfile(mode='r', filetypes=[('PDF', '*.pdf')])
    if file is not None:
        selected_input_file = file.name  # Store the selected input file name
        print(selected_input_file)
        item.set(selected_input_file)

def process_file(pb):
    console_out.set("")
    console_out.set("Processing")
    script_path = r".\firstocr.py"  # Use raw string or double backslashes for Windows paths
    input_path = selected_input_file
    output_path = selected_output_file
    
    if len(output_path) > 0:
        cmd = f"python {script_path} -p '{input_path}' -o '{output_path}'"
    else:
        cmd = f"python {script_path} -p '{input_path}'"

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    while process.poll() is None:
        pb.update()
        time.sleep(0.1)

    if process.returncode == 0:
        console_out.set("Complete.")
    else:
        console_out.set(process.stdout)
    
    pb.stop()

def pb_start(pb):
    pb.start()

def pb_stop(pb):
    pb.stop()

pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
pb.grid(column=0, row=2)

Button(root, text='Process', command=lambda: [pb_start(pb), threading.Thread(target=process_file, args=(pb,)).start()]).grid(column=0, row=4)

ttk.Label(frm, text="File Input").grid(column=0, row=1)
ttk.Button(frm, text="Open", command=lambda: open_file()).grid(column=1, row=1)
ttk.Label(frm, textvariable=item, width=40).grid(column=2, row=1)
ttk.Label(frm, text="Output").grid(column=0, row=2)
ttk.Button(frm, text="Select", command=lambda: select_file()).grid(column=1, row=2)
ttk.Label(frm, textvariable=output, width=40).grid(column=2, row=2)
ttk.Label(root, textvariable=console_out).grid(column=0, row=3)

root.mainloop()
