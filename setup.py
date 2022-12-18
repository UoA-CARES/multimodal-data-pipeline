import os
cwd = os.getcwd()

# Install dependencies
os.system("pip install moviepy")
os.system("pip install yt-dlp")
os.system("sudo apt install ffmpeg")
os.system("pip install ffmpeg-python")

os.chdir("CodeFormer")
os.system("python basicsr/setup.py develop")

