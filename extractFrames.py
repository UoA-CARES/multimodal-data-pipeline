import os
import time
from multiprocessing import Process,  Value

from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

def extractVideoFrames(file, outputPath):
    outDir = outputPath + os.sep + file.split(os.sep)[-1].split(".")[0]
    try:
        os.mkdir(outDir)
    except:
        pass
    extractFrames(file, outDir, resolution=(1080, 1920), letterBox=0)


def startExtraction(inputPath = "inputVideos",outputPath = "extractedFrames", threads = 2, batch =2):
    inputFolders = onlyfolders(inputPath)
    print("Found folders: ", inputFolders)

    for inputFolder in inputFolders:
        while(1):
            extractedVideoFrames = onlyfolders(outputPath)
            if(len(extractedVideoFrames)<batch):
                videoFiles = onlyfiles(inputFolder)
                if(len(videoFiles)==0):
                    break
                print(inputFolder,": Found files ", len(videoFiles))
                t = []
                for i in range(threads):
                    if(len(videoFiles)>0):
                        video = videoFiles.pop()
                        process = Process(target= extractVideoFrames, args = ( video, outputPath))
                        process.start()
                        t.append(process)
                for i in t:
                    i.join()
            time.sleep(1)

    print("Finished extracting frames!!!")

if __name__ == '__main__':
    startExtraction()
