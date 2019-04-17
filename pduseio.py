# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:15:06 2019

@author: Administrator
pd Dataframe I/O
"""
#import numpy as np
import pandas as pd
from pandas import Series,DataFrame
#import webbrowser


link='https://www.tiobe.com/tiobe-index/'
#webbrowser.open(link)
df= pd.read_csv('df_io.csv')


#print(df.head(3))
#df.to_csv('df_io.csv',index=False)
#df_json=df.to_json()
#print (pd.read_json(df_json))
#print(df[['Programming Language','Ratings']])
#print (df.iloc[1:3:,0:6])

#a=(df.loc[[1,3,5],['Programming Language','Ratings']])
#print(a)


