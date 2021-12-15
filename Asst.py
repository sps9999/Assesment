# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:49:25 2021

@author: avinash
"""

import os
import time
import threading
import multiprocessing
import shutil

import pymysql





	
conn = pymysql.connect(
		host='localhost',
		user='root',
		password = "",
       db='test'
       
		
		)
myc=conn.cursor()

query = """CREATE TABLE fileop ( 
       filenam varchar(30) ) """
  
#To execute the SQL query
myc.execute(query) 


root_path = 'D:/'

list = ['processing', 'queue', 'processed']

for items in list:
	path = os.path.join(root_path, items)
	os.mkdir(path)


r='D:/processing/'
def create ():
     for i in range(1,10):
        f=r+str(i)+'.txt'
        # file=open(f,'r') 
        file=open(f,'w')
        file.close()
        time.sleep(1)
        
def pre():
    for i in range(1,5):
       if len(os.listdir('D:/queue') ) == 0:
        #print("Directory is empty")
        path = "D:/processing/"
        dir_list = os.listdir(path)
        for i in dir_list:
            sql = "INSERT INTO fileop (filenam) VALUES (%s)"
            val = (i)
            myc.execute(sql, val)
            conn.commit()
            
        
        # for f in files:
        for f in dir_list:
             shutil.move(r+f, 'D:/queue/'+f)
       
        time.sleep(6)
           
# prints all files
        # print(dir_list)
                 
def t3():
    for i in range(1,5):
     
        path = "D:/queue/"
        dir_list = os.listdir(path)
    # for f in files:
        for f in dir_list:
            shutil.move(path+f, 'D:/processed/'+f)
        time.sleep(5)         

t1 = threading.Thread(target=create)
t2 = threading.Thread(target=pre)
t3 = threading.Thread(target=t3)
  
    # starting thread 1

t1.start()
t2.start()
t3.start()


