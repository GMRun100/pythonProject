#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------学习dict用法-----------------------
classmates={'benliu':100,'yuan':90,'bo':80,'GM':100}
print(classmates['benliu'])

#放入新数据
classmates['benliu']=95
print(classmates['benliu'])
classmates['guooujie']=95    #当dict中没有此元素时，会默认在后面添加此元素
print(classmates['guooujie'])
print(classmates)
#print(classmates['weiyongxin'])  #当dict中没有此元素时,会报错

#--------------判断dict中是否存在某个元素------------
#方法一：通过in来判断,如果存在返回True，如果不存在返回False
res='weiyongxin' in classmates
print(res)

#方法二: 通过get方法
res=classmates.get('weiyongxin')
print(res)   #get方法默认的返回值是None
res=classmates.get('weiyongxin',-1)   #也可以指定默认的返回值
print(res)

#----------用pop()函数删除某个key-------------
classmates.pop('guooujie')
print(classmates)


#---------------------python set用法---------
#set和dict类似是一组key的集合，但是set不存储value,而且set不存储重复元素
#创建一个set,需要提供一个list
s=set([1,2,3])
print(s)
s.add(3)    #add(函数可以添加元素)set会自动过滤掉重复元素
print(s)
s.add(5)
print(s)
#--------set可以看成数学意义上无序和无重复元素的集合-----
s2=set([2,3,4])
print(s&s2)    #两个不同的set之间可以做交集（&）运算，并集（|）运算等

#我们尝试将tuple类型赋值给set
t=(6,7,8)
s_t=set(t)    #因为t是tuple类型，而tuple类型是固定的，所以被赋值给set
print(s_t)   #因为set存储的是一个无序的集合，所以打印出来的效果可以是{8,6,7}

t2=(6,7,[8,9])
#s_t2=set(t2)   #这句话会报错，因为t2中存在可变的list元素
#print(s_t2)  #这句话会报错，因为t2中存在可变的list元素


#------------------学习心得----------------------------
#1.python里面的dict就相当于map
#2.在定义dict时需要用{}，list的定义用[]，tuple的定义用()，set的定义用set()
#3.dic的key必须是不可变对象，在实际应用中最常用的key是字符串
#4.这个通过key计算位置的算法称为哈希算法(Hash)
#5.set的key同样必须是不可变对象
#6.要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
