import os
import time
from multiprocessing import Process,  Value

from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

def startGeneration(inputVideos = "inputVideos", inputFrames = "extractedFrames", output = "output" ):
    try:
        os.mkdir(output)
    except:
        pass

    inputFrameFolders = onlyfolders(inputFrames)
    print(inputFrameFolders)

if __name__ == '__main__':
    startGeneration()
