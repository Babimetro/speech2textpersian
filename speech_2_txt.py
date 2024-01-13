# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:16:18 2023

@author: babimetro
"""


import os
import sys
import speech_recognition as sr
#sr.__version__
#'3.8.1'
r = sr.Recognizer()
#r.recognize_google('english')

def voice_recogenize(wavefile,lang):
    harvard = sr.AudioFile(wavefile)
    with harvard as source:
        audio = r.record(source)
        if lang=='':
            print(r.recognize_google(audio))
        else:
            print(r.recognize_google(audio,language = lang))
   

if __name__ == "__main__":
    vf = sys.argv[1]
    lang= sys.argv[2]
    voice_recogenize(vf,lang)
 



