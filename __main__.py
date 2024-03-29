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




try:
    os.chdir('D:\git\stt')
    print(os.getcwd())
except:
    pass


sqliteConnection = sq.connect('config.db')


sqlite_select_query = """SELECT * from init"""
df=pd.read_sql(sqlite_select_query,sqliteConnection)
vf=df['video_url'][0]
af=df['audio_url'][0]
chf=df['voice_url'][0]
vfilelist=[]
for path, subdirs, files in os.walk(vf):
    for name in files:
        print(os.path.join(path, name))
        vfilelist.append(os.path.join(path, name))

for vnf in vfilelist:
    mw.convert_video_to_audio_moviepy(vnf, af)

afls=[]
for path, subdirs, files in os.walk(af):
    for name in files:
        print(os.path.join(path, name))
        afls.append(os.path.join(path, name))

for anf in afls:
    #mw.audio_word_spliter(anf,chf)
    #split_in_parts(anf, chf)
    lent(anf,15,chf)

stts=[]
for path, subdirs, files in os.walk(chf):
    for name in files:
        print(os.path.join(path, name))
        stts.append(os.path.join(path, name))

for stt in stts:
    #mw.audio_word_spliter(anf,chf)
    #split_in_parts(anf, chf)
    mw.sttv(stt, "fa")

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