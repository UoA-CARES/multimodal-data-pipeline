import os
import time
from multiprocessing import Process,  Value
import shutil

from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

def extractVideoFrames(file, outputPath,fileOutPath):
    outDir = outputPath + os.sep + file.split(os.sep)[-1].split(".")[0]
    try:
        os.mkdir(outDir)
    except:
        pass
    print(fileOutPath)
    try:
        os.mkdir(fileOutPath)
    except:
        pass
    extractFrames(file, outDir,fileOutPath, resolution=(1080, 1920), letterBox=0)


def startExtraction(inputPath = "inputVideos",outputPath = "extractedFrames", output = "output",threads = 2, batch =2):
    inputFolders = onlyfolders(inputPath)
    print("Found folders: ", inputFolders)
    try:
        os.mkdir(outputPath)
    except:
        pass
    for inputFolder in inputFolders:
        try:
            os.makedirs(outputPath + os.sep + inputFolder.replace(inputPath,""))
        except:
            pass
        while(1):
            extractedVideoFrames = onlyfolders(outputPath + os.sep + inputFolder.replace(inputPath,"")  )
            if(len(extractedVideoFrames)<batch):
                videoFiles = onlyfiles(inputFolder)
                if(len(videoFiles)==0):
                    break
                print(inputFolder,": Found files ", len(videoFiles))
                t = []
                for i in range(threads):
                    if(len(videoFiles)>0):
                        video = videoFiles.pop()
                        fileOutPath = output + os.sep + inputFolder.split(os.sep)[-1]
                        process = Process(target= extractVideoFrames, args = ( video, outputPath + os.sep + inputFolder.replace(inputPath,""),fileOutPath ))
                        process.start()
                        t.append(process)
                for i in t:
                    i.join()

            time.sleep(1)
        removeAllFiles(inputFolder)

    print("Finished extracting frames!!!")

if __name__ == '__main__':
    startExtraction()
