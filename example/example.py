from utils import slowedreverb

# Make sure ffmpeg and sox is install 

# Linux : sudo apt install ffmpeg sox
# Windows : 
#       ffmpeg : https://ffmpeg.org/download.html
#       sox : https://sourceforge.net/projects/sox/

slowedreverb('saware.wav', 'lofi saware.wav')
