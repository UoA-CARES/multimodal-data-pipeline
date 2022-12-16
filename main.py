import os
import time
from multiprocessing import Process,  Value
from pathlib import Path
from shutil import rmtree
import shutil

from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

def extract():
    os.system("python extractFrames.py")

def generate():
    os.system("python genMultimodal.py")

inputFolder = "inputFolder"
inputVideos = "inputVideos"
outputFolder ="output"
os.system("python clean.py")


inputFolders = onlyfolders(inputFolder)
print("Found input folders: ", inputFolders)

for folder in inputFolders:
    files = onlyfiles(folder)
    print("Found %i files in %s folder"%(len(files), folder.split(os.sep)[-1]))
    for file in files:
        shutil.move(file, inputVideos + os.sep + file.split(os.sep)[-1])
    removeAllFiles(folder)
    extractor = Process(target= extract)
    extractor.start()
    generator = Process(target = generate)
    generator.start()
    generator.join()
    # move output files back into same folder structure as input (in finalOutput)
    try:
        os.mkdir("finalOutput")
    except:
        pass
    try:
        os.mkdir("finalOutput" + os.sep + folder.split(os.sep)[-1])
    except:
        pass
    outputs = onlyfiles(outputFolder)
    for o in outputs:
        print(o, "finalOutput"+ os.sep + o.split(os.sep)[-1] )
        shutil.move(o, "finalOutput"+ os.sep + folder.split(os.sep)[-1] + os.sep + o.split(os.sep)[-1] )
