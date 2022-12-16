import os
import time
from multiprocessing import Process,  Value
from pathlib import Path
from shutil import rmtree
import shutil

from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *
try:
    removeAllFiles("output")
except:
    pass

try:
    os.mkdir("output")
except:
    pass
try:
    removeAllFiles("extractedFrames")
except:
    pass
try:
    removeAllFiles("inputVideos")
except:
    pass
#shutil.copytree("downloads", 'inputVideos')

try:
    os.mkdir("inputVideos")
except:
    pass
'''
 try:
    removeAllFiles("CodeFormer/results/")
except:
    pass
'''
