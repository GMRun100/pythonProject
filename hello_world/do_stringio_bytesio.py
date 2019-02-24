#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中在内存中操作str和bytes的方法-----------------------
#在内存中操作str
from io import StringIO
f=StringIO()
f.write('hello')        #在内存中写入str
f.write(' ')
f.write('world!')
print(f.getvalue())   #获得写入的str

#从内存中读取str
f2=StringIO('Hello！\nHi\nGoodbye')
while True:
    s=f2.readline()    #我们会发现从内存中读取str与操作文件是类似的
    if s=='':
        break
    print(s.strip())

#操作内存中的二进制数据使用BytesIO
from io import BytesIO
f=BytesIO()
#写入一个字节流
f.write('中文'.encode('utf-8'))    #encode是将str转变为bytes

print(f.getvalue().decode('utf-8'))   #decode的方法是将字节流转变成str

#读取一个字节流
f2=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f2.read().decode('utf-8'))