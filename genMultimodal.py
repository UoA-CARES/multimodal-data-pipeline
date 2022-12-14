import os
import time
from multiprocessing import Process,  Value
from pathlib import Path
from shutil import rmtree
import shutil

from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

def findVideo(name,inputVideos):
    videos = onlyfiles(inputVideos)
    for video in videos:
        if( name in video):
            return video
    return ""
def runCodeFormer(found, weight = 0.8):
    os.chdir('CodeFormer')
    command = 'python inference_codeformer.py -w ' + str(weight) + ' --input_path "../'+ found + '"'
    print(command)
    os.system(command)
def startGeneration(inputVideos = "inputVideos", inputFrames = "extractedFrames", output = "output" ):
    try:
        os.mkdir(output)
    except:
        pass
    while(1):
        inputFrameFolders = onlyfolders(inputFrames)

        if(len(onlyfolders(inputVideos))==0):
            empty = 1
            for folder in inputFrameFolders:
                subfolders = onlyfolders(folder)
                if(len(subfolders)>0):
                    empty = 0
            if(empty==1):
                removeAllFiles(inputFrames)
                break
        for inputFrameFolder in inputFrameFolders:

            try:
                os.mkdir(output + os.sep + inputFrameFolder.replace(inputFrames,""))
            except:
                pass
            videoFrameFolders = onlyfolders(inputFrameFolder)

            for videoFramesFolder in videoFrameFolders:
                found = findVideo(videoFramesFolder.split(os.sep)[-1], output + os.sep +inputFrameFolder.split(os.sep)[-1])
                if(found!= ""):
                    cwd= os.getcwd()
                    print(videoFramesFolder,found)
                    runCodeFormer(videoFramesFolder, weight = 0.8)
                    #removeAllFiles(videoFramesFolder)

if __name__ == '__main__':
    startGeneration()
