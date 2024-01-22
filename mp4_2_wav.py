# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:10:01 2023

@author: babimetro`
"""

import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.silence import split_on_silence

def convert_video_to_audio_moviepy(video_file,audio_url, output_ext="wav"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    names=os.path.basename(filename).split('/')[-1]
    clip.audio.write_audiofile(audio_url+"/"+f"{names}.{output_ext}")
  
def audio_word_spliter(audio_file,path):

    sound_file = AudioSegment.from_wav(audio_file)
    audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=500,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
    )
    
    for i, chunk in enumerate(audio_chunks,path):
    
        out_file = path+"//"+"chunk{0}.wav".format(i)
        print ("exporting", out_file)
        chunk.export(out_file, format="wav")