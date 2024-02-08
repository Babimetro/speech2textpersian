# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:13:08 2024

@author: babimetro
"""
#===============================
#
#      
#    Liberaries
#
#================================
import sqlite3 as sq
import pandas as pd 
import os
import Functions as mw
from Functions import lent
import PySimpleGUI as sg
import GUI_lib as gui
#===============================
#
#      
#    Gui
#
#================================

frame_layout = [[sg.Multiline("", size=(80, 20), autoscroll=True,

    reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]]

 

layout=[[sg.Text('My window')],

        [sg.Button('Video Folder Location'),sg.Button('Audio Folder Location'),sg.Button('Voice Folder Location'),sg.Button('Close')],

        [sg.Frame("Output console", frame_layout)],
        [sg.Button('Video to Audio'),sg.Button('Audio Slicing'),sg.Button('Converting')]

       

                

        ]

window=sg.Window("My application",layout,size=(400,400))

 

while True:

    event,values=window.read()

    if event in (None,'Cancel'):

        window.close()

    elif event=='Close':

        window.close()

    elif event=='Video Folder Location':

        vf=gui.folderbrowser()

        print('Video Folder Location='+vf)
    elif event=='Audio Folder Location':

        af=gui.folderbrowser()

        print('Audio Folder Location'+af)
        
    elif event=='Voice Folder Location':

        chf=gui.folderbrowser()

        print('Voice Folder Location'+chf)
    elif event=='Voice Folder Location':

        chf=gui.folderbrowser()

        print('Voice Folder Location'+chf)
        
    elif event=='Video to Audio':
    
        vfilelist=[]
        for path, subdirs, files in os.walk(vf):
            for name in files:
                print(os.path.join(path, name))
                vfilelist.append(os.path.join(path, name))
        
        for vnf in vfilelist:
            mw.convert_video_to_audio_moviepy(vnf, af)


        print('Voice Folder Location'+chf)
        
    elif event=='Voice Folder Location':

        afls=[]
        for path, subdirs, files in os.walk(af):
            for name in files:
                print(os.path.join(path, name))
                afls.append(os.path.join(path, name))

        for anf in afls:
            #mw.audio_word_spliter(anf,chf)
            #split_in_parts(anf, chf)
            lent(anf,15,chf)


    elif event=='Voice Folder Location':
 
        stts=[]
        for path, subdirs, files in os.walk(chf):
            for name in files:
                print(os.path.join(path, name))
                stts.append(os.path.join(path, name))
        
        for stt in stts:
            #mw.audio_word_spliter(anf,chf)
            #split_in_parts(anf, chf)
            mw.sttv(stt, "fa")
   
#===============================
#
#      
#    Collect input file list
#
#================================




'''
# Get the list of all files and directories
path = df['video_url'][0]
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

for files in dir_list:
    vfile=path+"/"+files
    print(vfile)
    mw.convert_video_to_audio_moviepy(vfile,df['audio_url'][0])
'''
 

window.close()
