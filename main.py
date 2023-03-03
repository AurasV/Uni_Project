from tkinter import filedialog
import subprocess
import shutil

fileopen = filedialog.askopenfilename(  # get file path
    initialdir="C:/",  # initial dir = root folder (windows folder)
    title="Select audio file",  # title of the search window
    filetypes=(  # allowed formats
        ("any", "*"),
    ))

filesave = filedialog.askdirectory(
    initialdir="C:/",  # initial dir = root folder (windows folder)
    title="Select where to save the split files"  # title of the search window
)

amount = 5
command = "python -m spleeter separate -p spleeter:" + str(amount) + "stems -o " + filesave + " " + fileopen
subprocess.run(command)
archive = shutil.make_archive(filesave, 'zip', filesave)
# https://github.com/deezer/spleeter
