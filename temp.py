# -*- coding: utf-8 -*-
"""
20190417
my sql test use 2317 stock data 
numpy
"""
import numpy as np
import pymysql



db = pymysql.connect(host='localhost', port=3306, user='root', passwd='bb556656', db='my_db', charset='utf8')
#link mysql

cursor = db.cursor()
sql = 'select id,tr_buy,tr_sell,tr_net from 2317trcp'

cursor.execute(sql)
data = cursor.fetchall()
list_1=(data)
#print (list_1)
array_1 = np.array(list_1)
#print ("    id   buy  sell net \n ",array_1)
#print (array_1[9])

#c= np.array([[1,2,3],[4,5,6],[7,8,9]])
#print (c[:2,1:])

#print (np.random.randint(10, size=(3,2))) #產生隨機整數10個 

#x=np.arange(10)
#f = open ('x.pkl','rb')
#print (pickle.load(f))

#c=np.load('one_array.npy')
#y=np.arange(20)
#np.savez('two_array.npz',a=c,b=y)
c=np.load('two_array.npz')
print (c['b'])