import os
import shutil
from send2trash import send2trash
from tkinter import Tk
from tkinter.filedialog import askdirectory


img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif", ".HEIC")

doc = (".docx", ".doc", ".pdf", ".pptx", ".ppt")

def is_doc(file):
    return os.path.splitext(file)[1] in doc

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

def is_apps(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and "apps" in name.lower()

def is_swi(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and "swi" in name.lower()

def is_oop(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and "oop" in name.lower()

def is_cvut(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and "cvut" in name.lower()

def is_alg(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and "alg" in name.lower()

def is_ss(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and ("ss" or "std") in name.lower()

Tk().withdraw()  
selected_folder = askdirectory(title="Select a folder to organize")

if selected_folder:
    os.chdir(selected_folder)
    for file in os.listdir():
        if is_doc(file):
            if is_apps(file):
                shutil.move(file, "/Users/benjaminbaranovic/Desktop/APPS")
            elif is_oop(file):
                shutil.move(file, "/Users/benjaminbaranovic/Desktop/OOP")
            elif is_swi(file):
                shutil.move(file, "/Users/benjaminbaranovic/Desktop/SWI")
            elif is_cvut(file):
                shutil.move(file, "/Users/benjaminbaranovic/Desktop/CVUT")
            elif is_alg(file):
                shutil.move(file, "/Users/benjaminbaranovic/Desktop/ALG")
            elif is_ss(file):
                shutil.move(file, "/Users/benjaminbaranovic/Desktop/SS + STD")
            else:
                send2trash(file)
        elif is_image(file):
            if is_screenshot(file):
                shutil.move(file, "/Users/benjaminbaranovic/Pictures/screenshots")
            else:
                shutil.move(file, "/Users/benjaminbaranovic/Pictures/")
        else:
            send2trash(file)
else:
    print("No folder was selected.")