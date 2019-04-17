# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:40:17 2019

@author: Administrator
play with data through pandas
"""
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#X=DataFrame(np.random.rand(15).reshape(3,5))
#print(X.sort_values(ascending = True))
#print(X.sort_values(axis=1,by = 1))
#print(X.max(axis=1))

score_list =np.random.randint(30,100,20)
#print(score_list)
#bins= (30,59,79,100)
#C=(pd.cut(score_list,bins))
#print(C.value_counts())

df=DataFrame()
df['score']=score_list
df['student']=[pd.util.testing.rands(5) for i in range(20)]

bins= (30,59,79,100)
df['bins']=pd.cut(score_list,bins=bins,labels=['bad','soso','ok'])
print (C)
#for i in range(20):
   # df['student']= pd.util.testing.rands(5)
#for i in range(20):print(pd.util.testing.rands(5))
#df['student']=[pd.util.testing.rands(5) for i in range(20)]
print (df)

    
