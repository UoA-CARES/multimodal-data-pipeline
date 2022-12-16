import os
import time
from multiprocessing import Process,  Value
from pathlib import Path
from shutil import rmtree
import shutil
import moviepy.editor as mp
import cv2


from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

def findVideo(name,inputVideos):
    videos = onlyfiles(inputVideos)
    for video in videos:
        if( name in video):
            return video
    return ""


def renderVideo(frames, found, mergeAudio = 0):
    cwd = os.getcwd()
    my_clip = mp.VideoFileClip(found)
    framerate = my_clip.fps
    if(mergeAudio ==1):
        extractAudioFolder= "extractedAudio"
        try:
            os.mkdir(extractAudioFolder)
        except:
            pass

        audioNameList = found.split("\\")[-1].split("/")[-1].split(".")
        audioName ="".join(audioNameList[0])


        my_clip.audio.write_audiofile(extractAudioFolder+ os.sep + audioName +".wav")
        command = "ffmpeg -framerate "+ str(framerate)+" -thread_queue_size 512 -i "
        originalVideoName = found.rsplit("_",1)[0].split(".")[0]
        command +=  frames + '/%011d.png ' +cwd+os.sep + originalVideoName+"_HDface.mp4 -i extractedAudio/"+audioName+".wav"
        print(command)
        os.system(command)

        try:
            removeAllFiles("extractedAudio")
        except:
            pass



def cleanCodeformer():
    try:
        removeAllFiles("CodeFormer/results/")
    except:
        pass
def runCodeFormer(videoFrameFolder,found, weight = 0.8):
    currentDir = os.getcwd()
    imgs = onlyfiles(videoFrameFolder)
    img = imgs[0]
    img = cv2.imread(img)
    w,h,c = img.shape

    os.chdir('CodeFormer')
    command = 'python inference_codeformer.py -w ' + str(weight) + ' --input_path "../'+ videoFrameFolder + '"'
    if(w>1920 or h> 1920):
        command += " --upscale 1"
    print(command)
    os.system(command)
    os.chdir(currentDir)
    renderPath = "CodeFormer" + os.sep + "results" + os.sep + videoFrameFolder.split(os.sep)[-1] + "_" + str(weight) + os.sep + "final_results"

    renderVideo(renderPath, found, mergeAudio=1 )
    cleanCodeformer()
def startGeneration(inputVideos = "inputVideos", inputFrames = "extractedFrames", output = "output" ):
    try:
        os.mkdir(output)
    except:
        pass
    while(1):


        try:
            videoFrameFolders = onlyfolders(inputFrames)
        except:
            videoFrameFolders = []
        if(len(videoFrameFolders)==0 and len(onlyfiles(inputVideos))==0):
            break
        for videoFramesFolder in videoFrameFolders:
            found = findVideo(videoFramesFolder.split(os.sep)[-1], output)
            if(found!= ""):
                cwd= os.getcwd()
                print("a",videoFramesFolder,found)
                runCodeFormer(videoFramesFolder,found, weight = 0.8)
                print("removing ", videoFramesFolder)
                removeAllFiles("." + os.sep + videoFramesFolder)


if __name__ == '__main__':
    startGeneration()
