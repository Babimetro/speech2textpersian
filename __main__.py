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
#import sqlite3 as sq
#import pandas as pd 
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
theme="BlueMono"
sg.theme(theme)

frame_layout = [[sg.Multiline("", size=(80, 20), autoscroll=True,

    reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]]

 

layout=[[sg.Text('Online STT')],

        [sg.Button('Video Folder Location'),sg.Button('Audio Folder Location'),sg.Button('Voice Folder Location')],

        [sg.Frame("Output console", frame_layout)],
        [sg.Button('Video to Audio'),sg.Button('Audio Slicing'),sg.Button('STT'),sg.Button('Close')],

        [sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20),  key='-PBAR-')  ],
        [sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True)]
                

        ]

window=sg.Window("Video STT-Babi",layout,size=(500,550))
#window['-OUT-'].update("0%")
 

while True:

    event,values=window.read()

    #=================Folder Configuration===================
    #=======================Video============================
    if event=='Video Folder Location':

        vf=gui.folderbrowser(theme)

        print('Video Folder Location set to ='+vf)
    #=======================Audio============================
    elif event=='Audio Folder Location':

        af=gui.folderbrowser(theme)

        print('Audio Folder Location set to ='+af)
    #=======================Voice============================    
    elif event=='Voice Folder Location':

        chf=gui.folderbrowser(theme)

        print('Voice Chunk Folder Location set to ='+chf)
        
    #=================Buttons=====================================
    #====================Video t Audio Convertor==================
    elif event=='Video to Audio':
        vfilelist=[]
        for path, subdirs, files in os.walk(vf):
            for name in files:
                print(os.path.join(path, name))
                vfilelist.append(os.path.join(path, name))
        vff=vfilelist
        i=0
        window['-OUT-'].update(str(i)+"%")
        for vnf in vfilelist:

            mw.convert_video_to_audio_moviepy(vnf, af)
            i=i+round(100/len(vfilelist),0)
            window['-PBAR-'].update(current_count=i )
            window['-OUT-'].update(str(i)+"%")

    #=================Buttons=====================================
    #=========================='Audio Slicing'====================       
    elif event=='Audio Slicing':

        afls=[]
        for path, subdirs, files in os.walk(af):
            for name in files:
                print(os.path.join(path, name))
                afls.append(os.path.join(path, name))
        i=0
        window['-OUT-'].update(str(i)+"%")
        for anf in afls:
            i=i+round(100/len(afls),0)
            window['-PBAR-'].update(current_count=i )
            window['-OUT-'].update(str(i)+"%")
            lent(anf,15,chf)
    #=================Buttons=====================================
    #========================'Audio Slicing'====================    

    elif event=='STT':
 
        stts=[]
        for path, subdirs, files in os.walk(chf):
            for name in files:
                print(os.path.join(path, name))
                stts.append(os.path.join(path, name))
        i=0
        window['-OUT-'].update(str(i)+"%")       
        for stt in stts:
            i=i+round(100/len(stts),0)
            window['-PBAR-'].update(current_count=i )
            window['-OUT-'].update(str(i)+"%")
            mw.sttv(stt, "fa")
    
    #=====================================================================
    #=====================================================================  
    #================================ Exit ===============================
    elif event in (None,'Cancel') or event=='Close' or event == sg.WIN_CLOSED :

        break
      
    

window.close()
