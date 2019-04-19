# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:37:55 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
import seaborn as sns

s=Series(np.random.randn(100))
#s.plot()
#plt.show()
#sns.distplot(s,color='r',bins=10)
#sns.kdeplot(s,shade=True)
df = sns.load_dataset('flights')
#print (df.head(10))

#df.plot(kind='bar')

df = df.pivot(index='month',columns='year',values='passengers')
#print(df)
#df.sum().plot(kind='bar')
#sns.barplot(df.sum().index,df.sum().values)
sns.heatmap(df,annot=True,fmt='d')

plt.show()