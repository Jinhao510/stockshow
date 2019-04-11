# -*- coding: utf-8 -*-
"""
20190411
my sql test use 2317 stock data 
link my sql
"""
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='bb556656', db='my_db', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法（查詢資料庫版本）
sql = 'select wei from com_per'

#執行語法
cursor.execute(sql)
#選取第一筆結果
data = cursor.fetchone()

print ("Database version : %s " % data)
#
#關閉連線
db.close()