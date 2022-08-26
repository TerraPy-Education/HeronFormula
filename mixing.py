import time
from gtts import gTTS
import os
from moviepy.editor import *

def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile("output/"+outname,fps=fps)

tts = gTTS('In this video we will learn about the Heron\'s Formula', lang='en')

tts.save("sound.mp3")

with open ("sound.mp3", "ab") as f:

    tts = gTTS("Heron's formula is a method of finding\n the area of a triangle when \nthe three sides are given.", lang='en')
    tts.write_to_fp(f)

combine_audio(os.path.join("media", "videos", "graphical", "1080p60", "Heron.mp4"), "sound.mp3", "main.mp4")
