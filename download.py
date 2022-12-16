import os
import shutil
downloadFolder = "./downloads"
try:
    os.makedirs(downloadFolder, exist_ok=True)
except:
    pass
path = input("youtube url or txt file name? (dont include .txt): ")
if(len(path)>5 and "." in path ):
    print("detected url")
    urls = [path]
else:
    urls = []
    #read txt file
    with open(path+".txt") as f:
        contents = f.readlines()
    for line in contents:
        urls.append(line)
    #remove duplicates
    res = []
    [res.append(x) for x in urls if x not in res]
    urls = res
print(urls)
print("Found %i urls" %len(urls))

currentDir = os.getcwd()
os.chdir(downloadFolder)
for url in urls:

	command = 'yt-dlp -o "%(id)s.%(ext)s"'  +' ' + url
	print(command)
	print("\nDownloading ", url)
	os.system(command)
	print("=============")
os.chdir(currentDir)
shutil.move(downloadFolder, "inputFolder")
os.system("python main.py")
