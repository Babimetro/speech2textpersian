# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:36:59 2023

@author: babimetro
"""
'''
from pydub import AudioSegment

t1 = t1 * 1000 #Works in milliseconds
t2 = t2 * 1000
newAudio = AudioSegment.from_wav("oldSong.wav")
newAudio = newAudio[t1:t2]
newAudio.export('newSong.wav', format="wav") 
'''


import os
import sys
import soundfile as sf
from pydub import AudioSegment

def lent(audiofile):
    
    f = sf.SoundFile(audiofile)
    print('samples = {}'.format(len(f)))
    print('sample rate = {}'.format(f.samplerate))
    print('seconds = {}'.format(len(f) / f.samplerate))
    ll=(len(f) / f.samplerate)*1000
    t1=0
    f=1
    while(t1<ll):
        t2=t1+30000

        newAudio = AudioSegment.from_wav(audiofile)
        newAudio = newAudio[t1:t2]
        newAudio.export(audiofile+'_'+str(f)+'.wav', format="wav")
        print(t1,t2,ll)
        t1=t1+30000
        f+=1
      
    
    
if __name__ == "__main__":
    vf = sys.argv[1]
    lent(vf)
    
    