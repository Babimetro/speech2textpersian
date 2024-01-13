# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:13:08 2024

@author: babimetro
"""

import sqlite3 as sq
import pandas as pd

sqliteConnection = sq.connect('config.db')


sqlite_select_query = """SELECT * from init"""
df=pd.read_sql(sqlite_select_query,sqliteConnection)


