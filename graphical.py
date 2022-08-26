from textwrap import fill
from manim import *
from gtts import gTTS
import playsound
from moviepy.editor import *

def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile("./output/"+outname,fps=fps)

class Heron(Scene):
    def construct(self):
        title = Text("Heron's Formula", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))
        self.wait(3)
        t2 = Triangle(stroke_width=2, color=WHITE)
        t1 = Text("Heron's formula is a method of finding the area of a triangle when the three sides are given", font_size=20).set_color(WHITE).to_edge(UP, buff=1.2)
        self.play(Create(t1, run_time=3.0))
        self.play(Create(t2, run_time=3.0))
        
        # self.play(Write(Text("Heron's Formula", font_size=30)))
        # tri = Triangle(stroke_width=2, color=WHITE)
        # self.play(Create(tri))
        self.wait(2)


