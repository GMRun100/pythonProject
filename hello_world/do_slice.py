#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------学习python切片的用法---------------
#新建一个list数组
L=list(range(100))
print(L)
print("获取数组前10个元素:",L[0:10])  #不包括10
print("获取数组后10个元素:",L[-10:])  #倒数时包括-10
print("获取前50个元素，从0开始，步长为5:",L[:50:5])
#对字符串进行切片
str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(len(str))
print(str)
print('获取前5个字母:',str[:5])
print('获取后5个字母:',str[-5:])
