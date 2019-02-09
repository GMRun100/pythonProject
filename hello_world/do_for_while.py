#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------学习python for...in...用法-----------------
classmates=['benliu','yuan','bo','GM']
for name in classmates:
    print(name)
	
#0到100的整数求和
sum=0;
for x in range(101):   #range()函数可以生成小于括号内数字的整数序列
	sum=sum+x
print(sum)
	
#------------while循环------------------------------
sum=0	
n=99
while n>0:
   sum=sum+n
   n=n-2
print(sum)

#-----------break语句结束循环----------------
#当n大于10是，停止打印
n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print('End')

#------------continue语句-----------
#只输出打印10以内的奇数
n=0
while n<=10:
      n=n+1
      if n%2==0:
         continue
      print(n)
print('End')
	
#-----学习心得----------------
#1.for语句最后一定要加：(冒号)
#2.for语句最后不需要像C语言那样有什么i++之类的，自动会遍历序列
#3.在python中是不需要声明变量类型的
#4.在python中相同的缩进表示一个语句块
#5.while语句后面同样不要忘了：(冒号)
#6.在python语句中需要注意tab键的使用
