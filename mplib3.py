# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:54:14 2019

@author: Administrator
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

#s=Series(np.random.randn(1000))
#plt.hist(s, rwidth=0.9)
#a1 =Series(np.arange(10))
#plt.hist(s,rwidth=0.9,bins=20,color='m')  #直方圖
#s.plot(kind='line')   #直方頂點曲線圖


df=DataFrame(np.random.randint(1,10,40).reshape(10,4),columns =['A','B','C','D'])
print(df['A'])

#for i in df.index:
    #df.iloc[i].plot(label=(i))
    
plt.legend()
#df.plot(kind='area')
df['A'].plot(kind='area')
plt.show()

