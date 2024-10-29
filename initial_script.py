# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 06:02:33 2024

@author: Dell
"""

# import os
import numpy as np
import pandas as pd
import pyodbc
from datetime import date
from datetime import datetime
import re


# ----------------------------DATABASE CONNECTION------------------------------

SERVER = 'DESKTOP-G1RQ1QS\SQLEXPRESS'
DATABASE = 'rotten_tomatoes_movies'

connectionString = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE}'
conn = pyodbc.connect(connectionString)

sql_inicial = """
SELECT *
FROM movie_rating;
"""

df = pd.read_sql(sql_inicial, conn)

df.shape

df.info()

numeric_data = df.describe()








