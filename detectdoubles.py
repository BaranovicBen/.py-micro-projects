from tkinter.filedialog import askdirectory
from tkinter import Tk
from send2trash import send2trash
import os , hashlib
from pathlib import Path
Tk().withdraw()
path =  askdirectory(title="Select a folder")

file_list = os.walk(path)

unique = dict()
for root,folders,files in file_list:
    for file in files:
        path = Path(os.path.join(root,file))
        fileHash = hashlib.md5(open(path,'rb').read()).hexdigest()
        print(len(fileHash))
        if fileHash not in unique:
            unique[fileHash] = path
        else:
            send2trash(str(path))
            print(f"{path} has been moved to the Trash")