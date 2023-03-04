from tkinter import filedialog  # save location and getting file
import shutil  # moving files after splitting
import subprocess  # running the spleeter command
import os  # deleting the folder it temporarily makes

fileopen = filedialog.askopenfilename(  # get file path
    initialdir="C:/",  # initial dir = root of C: folder (Windows folder)
    title="Select audio file",  # title of the search window
    filetypes=(
        ("Audio files", "*.mp3;*.wav;*.aiff;*.flac;*.m4v;*.ogg"),  # allowed file types
    ))

filesave = filedialog.askdirectory(
    initialdir="C:/",  # initial dir = root of C: folder (Windows folder)
    title="Select where to save the split files"  # title of the search window
)

amount = 5  # amount of split files
command = "python -m spleeter separate -p spleeter:" + str(amount) + "stems -o " + filesave + " " + fileopen
# prepare the command for running
subprocess.run(command)  # run the command

save_location = fileopen.split("/")[-1].split(".")[0]  # getting just the name of the file we opened (the audio file)
save_location_path = filesave + "/" + save_location
# adding the folder location and the audio file name to get the temporary folder path
for i in ["vocals", "drums", "bass", "piano", "other"]:  # running through each split file
    split_file_path = save_location_path + "/" + i + ".wav"  # getting the path where to move the split files
    shutil.move(split_file_path, filesave)  # moving the split audio files to save location

os.rmdir(save_location_path)
