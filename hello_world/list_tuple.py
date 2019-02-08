#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------list相关用法---------------------------
#python语言最后不用加;作为结尾，感觉好不习惯
classmates=['benliu','yuan','bo','GM']
#print(classmates[0])
#print(classmates[1])
#print(classmates[2])
#print(classmates[3])

#可以设置索引为-1，直接显示最后一个元素，-2为倒数第二个元素，以此类推
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
#通过len()函数可以计算数组的长度
print(classmates)
print(len(classmates))
#往数组中追加元素
classmates.append('weiyongxin')
print(classmates)
#向指定位置插入元素
classmates.insert(1,'guooujie')
print(classmates)
#删除list末尾的元素，用pop函数
classmates.pop()
print(classmates)
#删除指定位置的函数，用pop(i)函数
classmates.pop(1)
print(classmates)

#list里面的元素类型可以不同，这一点和C语言和C++是完全不一样的
L=['apple',123,True]
print(L)

#list里面还可以嵌套其他的数组
s=['xuming',classmates,'chengjinchao']
print(s)
print(len(s))   
#注意通过len函数发现s的长度是3，这里可以把s看成是一个二维数组
print(s[1][1])


#---------------------tuple的用法-----------
#在python中另外一种有序列表叫元组（名字有些搞笑有木有），tube和list很类似，但是tube一旦初始化，值就不能改变了
#tuple和list定义的区别是，list是通过[]定义，而tuple通过()定义
t=(2,1)
print(t)
#t(1)=3   这句话会报错，因为tuple类型的值不能发生改变
#如何定义一个一维数组呢
t2=(1,)   #此处必须要加一个，
print(t2)

#tuple不可变有啥用，安全啊，所以在定义数组的时候能用tuple就不用list
