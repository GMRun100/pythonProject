#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中os模块的操作方法-----------------------
#Python内置的os模块也可以直接调用操作系统提供的接口函数
import os
print(os.name)   #输出nt就表示windows系统
#print(os.environ.get('path'))   #输出系统的path环境变量

#查看当前目录的绝对路径
m_dir=os.path.abspath('.')    #获取当前的绝对路径
print(m_dir)   
#在某个路径下创建一个新目录
m_dir=os.path.join(m_dir,'testdir')
print(m_dir)
#创建这个新目录
if not os.path.isdir(m_dir):    
    os.mkdir(m_dir)    #如果在本地没有此目录会自动进行创建
#删除目录
os.rmdir(m_dir)

#拆分路径
fpath=r'D:\CNCS\NicSys1000\NicSys1000_dev\trunk\02.Software\02.DB\branches\english_version\bin\Debug\config_test\gp.csv'  
m_path,m_csv=os.path.split(fpath)
print(m_path)
print(m_csv)

#列出当前目录下的所有目录
l=[x for x in os.listdir('.') if os.path.isdir(x)]   #此处采用了列表生成式的写法
print('当前目录下所含有的文件夹：',l)


#列出当前目录下所有的py文件
f_py=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print('当前目录下所有的py文件：',f_py)

#