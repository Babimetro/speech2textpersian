# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:10:01 2023

@author: babimetro`
"""
#===============================
#
#      
#    Liberaries
#
#================================
import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.silence import split_on_silence
from scipy.io.wavfile import write as write_wav
import numpy as np
#import vflibrosa
import soundfile as sf
import speech_recognition as sr
import sqlite3 as sq
import pandas as pd

def convert_video_to_audio_moviepy(video_file,audio_url, output_ext="wav"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    names=os.path.basename(filename).split('/')[-1]
    clip.audio.write_audiofile(audio_url+"/"+f"{names}.{output_ext}")
''' 
def audio_word_spliter_v1(audio_file,path):

    sound_file = AudioSegment.from_wav(audio_file)
    audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=500,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
    )
    
    for i, chunk in enumerate(audio_chunks):
    
        out_file = path+"\\"+"chunk{0}.wav".format(i)
        print ("exporting", out_file)
        chunk.export(out_file, format="wav")

def zero_runs(a):
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges

def split_in_parts(audio_path, out_dir):
    # Some constants
    min_length_for_silence = 0.01 # seconds
    percentage_for_silence = 0.01 # eps value for silence
    required_length_of_chunk_in_seconds = 60 # Chunk will be around this value not exact
    sample_rate = 16000 # Set to None to use default

    # Load audio
    waveform, sampling_rate = vflibrosa.load(audio_path, sr=sample_rate)

    # Create mask of silence
    eps = waveform.max() * percentage_for_silence
    silence_mask = (np.abs(waveform) < eps).astype(np.uint8)

    # Find where silence start and end
    runs = zero_runs(silence_mask)
    lengths = runs[:, 1] - runs[:, 0]

    # Left only large silence ranges
    min_length_for_silence = min_length_for_silence * sampling_rate
    large_runs = runs[lengths > min_length_for_silence]
    lengths = lengths[lengths > min_length_for_silence]

    # Mark only center of silence
    silence_mask[...] = 0
    for start, end in large_runs:
        center = (start + end) // 2
        silence_mask[center] = 1

    min_required_length = required_length_of_chunk_in_seconds * sampling_rate
    chunks = []
    prev_pos = 0
    for i in range(min_required_length, len(waveform), min_required_length):
        start = i
        end = i + min_required_length
        next_pos = start + silence_mask[start:end].argmax()
        part = waveform[prev_pos:next_pos].copy()
        prev_pos = next_pos
        if len(part) > 0:
            chunks.append(part)

    # Add last part of waveform
    part = waveform[prev_pos:].copy()
    chunks.append(part)
    print('Total chunks: {}'.format(len(chunks)))

    new_files = []
    for i, chunk in enumerate(chunks):
        out_file = out_dir + "chunk_{}.wav".format(i)
        print("exporting", out_file)
        write_wav(out_file, sampling_rate, chunk)
        new_files.append(out_file)

    return new_files
'''


def lent(audiofile,lenght,chf):
    lenght=lenght*1000
    f = sf.SoundFile(audiofile)
    print('samples = {}'.format(len(f)))
    print('sample rate = {}'.format(f.samplerate))
    print('seconds = {}'.format(len(f) / f.samplerate))
    ll=(len(f) / f.samplerate)*1000
    t1=0
    f=1
    while(t1<ll):
        t2=t1+lenght

        newAudio = AudioSegment.from_wav(audiofile)
        newAudio = newAudio[t1:t2]
        newAudio.export(chf+os.path.basename(audiofile)+'_'+str(f)+'.wav', format="wav")
        print(t1,t2,ll)
        t1=t1+lenght
        f+=1


#sr.__version__
#'3.8.1'
r = sr.Recognizer()
#r.recognize_google('english')

def sttv(wavefile,lang):
    try:
        sqliteConnection = sq.connect('stt1.db')
        cursor = sqliteConnection.cursor()
        
        print("Successfully Connected to SQLite")
    except sq.Error as error:
        print("Failed to insert data into sqlite table", error)
        
 
    harvard = sr.AudioFile(wavefile)
    with harvard as source:
        print(wavefile)
        audio = r.record(source)
        if lang=='':
            text=r.recognize_google(audio)
            print(text)
        else:
            try:
                text=r.recognize_google(audio,language = lang)
                print(text)
            except:
                text="no text detected."
                print(text)
            
            
        
        
        sqlite_insert_query = """INSERT INTO stt
                      (filename, text) 
                       VALUES 
                      (?,?)"""

        count = cursor.execute(sqlite_insert_query,(wavefile,text))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    