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

df.describe()

studio_name_count = pd.crosstab(index=df["studio_name"], columns="n", colnames=[""])

df_runtime_in_minuts = df.sort_values("runtime_in_minuts", ascending= False)

df_quant = df.quantile([.25,.5,.75])

for col in df_quant.columns:  
  iqr = df_quant[col][.75] - df_quant[col][.25]
  lim_sup = df_quant[col][.75] + iqr * 1.5
  lim_inf = df_quant[col][.25] - iqr * 1.5
  
  aux = np.array([])
  
  for val in df[col]:
    if val > lim_sup:
      aux = np.append(aux, "superior")
    elif val < lim_inf:
      aux = np.append(aux, "inferior")
    else:
      aux = np.append(aux, "normal")
      
  df[col + "_bp"] = aux


df_runtime_in_minuts = df.sort_values("runtime_in_minuts", ascending= True)


























