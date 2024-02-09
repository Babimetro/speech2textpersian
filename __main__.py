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

        [sg.Button('Video Folder Location'),sg.Button('Audio Folder Location'),sg.Button('Voice Folder Location'),sg.Spin(['5','10','15','20','25','30'], s=(15,2))],

        [sg.Frame("Output console", frame_layout)],
        [sg.Button('Video to Audio'),sg.Button('Audio Slicing'),sg.Button('STT'),sg.Button('Close')],

        [sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20),  key='-PBAR-')  ],
        [sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True)]
                

        ]

window=sg.Window("Video STT-Babi",layout,size=(500,550))
#window['-OUT-'].update("0%")
 
#window['-PBAR-'].update(max=100)
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
        i=0
        window['-OUT-'].update(str(i)+"%")
        window['-PBAR-'].update(current_count=i )
        
        vfilelist=[]
        for path, subdirs, files in os.walk(vf):
            for name in files:
                print(os.path.join(path, name))
                vfilelist.append(os.path.join(path, name))
        vff=vfilelist
        for vnf in vfilelist:
            
            mw.convert_video_to_audio_moviepy(vnf, af)
            i=i+round(100/len(vfilelist),0)
            if i>100:
                i=100
            window['-OUT-'].update(str(i)+"%")
            window['-PBAR-'].update(current_count=i )
            print('------------------------------')
            print('-----------Finished-----------')
            
            

    #=================Buttons=====================================
    #=========================='Audio Slicing'====================       
    elif event=='Audio Slicing':
        i=0
        window['-OUT-'].update(str(i)+"%")
        window['-PBAR-'].update(current_count=i )
        afls=[]
        for path, subdirs, files in os.walk(af):
            for name in files:
                print(os.path.join(path, name))
                afls.append(os.path.join(path, name))

        for anf in afls:
            i=i+round(100/len(afls),0)
            if i>100:
                i=100
            window['-OUT-'].update(str(i)+"%")
            window['-PBAR-'].update(current_count=i )
            lent(anf,15,chf)
            print('------------------------------')
            print('-----------Finished-----------')
    #=================Buttons=====================================
    #========================'Audio Slicing'====================    

    elif event=='STT':
        i=0
        window['-OUT-'].update(str(i)+"%")
        window['-PBAR-'].update(current_count=i )
        stts=[]
        for path, subdirs, files in os.walk(chf):
            for name in files:
                print(os.path.join(path, name))
                stts.append(os.path.join(path, name))
   
        for stt in stts:
            i=i+round(100/len(stts),0)
            if i>100:
                i=100
            window['-OUT-'].update(str(i)+"%")
            window['-PBAR-'].update(current_count=i )

            mw.sttv(stt, "fa")
            print('------------------------------')
            print('-----------Finished-----------')
    
    #=====================================================================
    #=====================================================================  
    #================================ Exit ===============================
    elif event in (None,'Cancel') or event=='Close' or event == sg.WIN_CLOSED :

        break
      
    

window.close()
