# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:44:55 2019

xls data input my sql

"""
import pandas as pd
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='bb556656', db='my_db', charset='utf8')

df = pd.read_excel("2317BSD.xlsx")
d=(df.head(20))
print (d)
