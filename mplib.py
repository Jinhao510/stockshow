# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:07:29 2019

@author: Administrator  

0418 matplotlib  seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('2317BSD.csv')
C_se=df['se_sell']
B_se=df['se_buy']

#累加折線圖
print(C_se,B_se)
def plotData(plt, data):
    
  x = [p[0] for p in data]
  y = [p[1] for p in data]

  plt.plot(x,'-', y, 'o')
  
 

plotData(plt, C_se)
plotData(plt, B_se)   
    
    
#plt.plot(C_se,B_se)
plt.show()