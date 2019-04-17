# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:19:53 2019

updata   0417 to Udemy learn pandas
"""
 
#import webbrowser


link='https://www.tiobe.com/tiobe-index/'
#webbrowser.open(link)
#
#df= pd.read_clipboard()
data ={
       'Country':['China','India','Brazil'],
       'Capital':['Beijing','New Delhi','Brasilia'],
       'Population':['1432732201','1303171635','207847528']
       }
#df=DataFrame(data)

s1 = Series(data['Country'])
s2 = Series(data['Capital'])
s3 = Series(data['Population'])

df_n = DataFrame([s1,s2,s3],index=['Country','Capital','Population'])
df_n=df_n.T
#print (df_n)

df_n.index=['A','B','C']
#print (df_n)

#for row in df.iterrows():
 #   print(row)

#print (df)
#print(type(df.Ratings))
#print(df['Programming Language'])

#print(df.index)
#df_n = DataFrame(df,columns=['Apr 2019','Programming Language','Change.1'])
#df_n=df[0:5]
#print (df_n)

a= [1,2,3,4]
D= Series(a)
#print (D)
#print (D.index)

s2=Series(np.arange(5))
s3=Series({'A':1,'B':2,'C':3,'D':4})
#print(s3,s2) 
s3.to_dict()
#print (s3[s3>2])
#print(s3.max())
s4 =Series (s3,index=['B','C','D'])
#print (s4)
rs=df= np.random.rand(15).reshape(3,5)
df= DataFrame(rs,index =['在','左','邊'],columns =['我','在','上','面','喔'])
#print (df.reindex(index =['在','左'],columns =['我','在']))


#print (type (np.nan))

