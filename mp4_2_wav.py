# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:10:01 2023

@author: babimetro
"""

import os
from moviepy.editor import VideoFileClip

def convert_video_to_audio_moviepy(video_file,audio_url, output_ext="wav"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    names=os.path.basename(filename).split('/')[-1]
    clip.audio.write_audiofile(audio_url+"/"+f"{names}.{output_ext}")
  

 