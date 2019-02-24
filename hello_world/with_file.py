#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中文件的读写方法-----------------------
#读文件
""" try:
    f=open('test.txt','r')
    print(f.read())
finally:            #此条语句很重要，保证无论文件打开是否异常，都会正确的关闭文件
    if f:
        f.close() """

#另外一种打开关闭文件的方式
""" with open('test.txt','r') as f2:
    print(f2.read()) """

#下面我们尝试读取1000的配置文件
""" with open('gp.csv','r') as f:
    for line in f.readlines():    #当文件比较大时采用按行读取的方法
        print(line.strip())       #按行读取时返回的为list"""
fpath=r'D:\CNCS\NicSys1000\NicSys1000_dev\trunk\02.Software\02.DB\branches\english_version\bin\Debug\config_test\gp.csv'       
with open(fpath,'r') as f:
    for line in f.readlines():    #当文件比较大时采用按行读取的方法
        print(line.strip())       #按行读取时返回的为list

#写文件
with open('test.txt','a') as f2:     #参数a表示以追加的方式写入
    f2.write('Hello weiyongxin!\n')

with open('test.txt','r') as f2:
    print(f2.read())

#一些常用的参数如下所示，从官网摘取https://docs.python.org/3/library/functions.html#open
""" Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing) """