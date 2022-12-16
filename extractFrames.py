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

    extractFrames(file, outDir,fileOutPath, resolution=(1080, 1920), letterBox=0)


def startExtraction(inputPath = "inputVideos",outputPath = "extractedFrames", output = "output", batch =2):

    try:
        os.mkdir(outputPath)
    except:
        pass

    while(1):
        extractedVideoFrames = onlyfolders(outputPath  )
        if(len(extractedVideoFrames)<batch):
            print(extractedVideoFrames, batch)
            videoFiles = onlyfiles(inputPath)
            if(len(videoFiles)==0):
                break
            t = []
            for i in range(batch):
                if(len(videoFiles)>0):
                    video = videoFiles.pop()
                    fileOutPath = output + os.sep + video.split(os.sep)[-1]
                    process = Process(target= extractVideoFrames, args = ( video, outputPath ,fileOutPath ))
                    process.start()
                    t.append(process)
            for i in t:
                i.join()

        time.sleep(1)
    #removeAllFiles(inputFolder)

    print("Finished extracting frames!!!")

if __name__ == '__main__':
    startExtraction()
