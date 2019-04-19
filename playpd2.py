# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:42:46 2019

@author: Administrator
0418  playdata group by
"""
import numpy as np
import pandas as pd
import matplotlib
from pandas import Series,DataFrame

df= pd.read_csv('2317BSD.csv')
#print (df.shape)
#print(df.head(3))

#g=df.groupby(df['Change'])
#print(g.get_group('change'))

#C=df['name'][0].strip().split(' ')
#print(C)

#def foo(line):
  # line = df.strip().split(' ')
  # return Series([line[1],line[2]])   #拆資料 同欄拆多欄 但資料須明顯結構差異 : 空白

C_se=df['se_sell']
B_se=df['se_buy']
#print(C.head(10),B.head(10))
#ne=C_se.combine_first(B_se)           #當A資料缺失可透過B資料 combine_first 補上
#print(ne.head(5))

#print(df.drop_duplicates(['ma_buy'])) #清理重複資料 當此欄位資料重複時刪除
s1=Series(df['se_sell'])
s1=s1.astype(np.int32)

#print(s1.cumsum)
s1.plot(kind='line')
s1.show()