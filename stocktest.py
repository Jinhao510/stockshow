# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:05:31 2019

@author: Administrator
"""
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import pandas_datareader as pdr
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

#df= pdr.get_data_yahoo('BABA') #可透過PANDAS串接YAHOO、GOOGLE等網站資料
#print(df.info())
#print (df.tail(10))
start = datetime (2017,1,1)
baba= pdr.get_data_yahoo('BABA',start=start)
amaz= pdr.get_data_yahoo('AMZN',start=start)

#print(baba.head(10))
#print(amaz.head(10))

#baba['Close'].plot()
#amaz['Close'].plot()
#baba['updo']=baba['High'] -baba['Low']
#amaz['updo']=amaz['High'] -amaz['Low']
amaz['change']=amaz['Close'].pct_change()
baba['change']=baba['Close'].pct_change()




baba['change'].plot(figsize=(10,4),linestyle='--',marker='o',color='r')
amaz['change'].plot(figsize=(10,4),linestyle='--',marker='o',color='b')

plt.show()