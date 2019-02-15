#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------学习python中sorted函数的用法--------------------
#sorted函数是对一个list进行排序
#例：我们对一个字符串进行排序
l=[-4,3,50,4,67,3,10]
print(l)
print(sorted(l))   #sorted函数默认是按着从小到大排序的


#sorted函数也可以传入函数参数，list中的每个变量由该函数处理后，该依据处理后的新list进行排序
#例如对上述list,每个数值取绝对值之后进行排序
print(sorted(l,key=abs))   #通过用法可以看出，key应该是一个命名关键字参数

#对一个字符串进行排序
classmates=['benliu2','yuan2','bo2','GM2']
print(sorted(classmates))   #默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted(classmates,key=str.lower))   #对字符串忽略大小写进行排序
print(sorted(classmates,key=str.lower,reverse=True))   #也可以对字符串进行反向排序

#对dict中的字符串进行排序
classmates2={'benliu':150,'yuan':90,'bo':80,'GM':100}
def by_name(t):
    return(t.lower())

print('方法一：',sorted(classmates2,key=str.lower))
l=sorted(classmates2,key=by_name)
print('方法二：',l)

#对dict中的数字进行排序
def by_num(kw):
        return classmates2[kw]

l=sorted(classmates2,key=by_num,reverse=True)
print('对dict中的数字排序,成绩从高到低，哈哈：',l)


#sorted是一个高阶函数，用sorted函数排序的关键是写一个排序方法的映射函数
