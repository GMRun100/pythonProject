#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python中如何获取对象信息-----------------------
#我们通过type()函数可以获取对象信息,返回值为对应的class的类型
print(type(123))     #返回值为<class int> ，表明为int类
print(type('123'))   #class str

import types
def fn(p):
    pass

#对于一些特定的类型，可以跟types中的常量进行比较
#判断某个类型是否是函数
print('types.FunctionType=',type(fn)==types.FunctionType)  #FunctionType属于types模块中的常量

#判断是否是python中的内建函数
print('types.BuiltinFunctionType=',type(abs)==types.BuiltinFunctionType)

#判断是否是隐藏函数
print('types.LambdaType=',type(lambda x: x)==types.LambdaType)

#判断是否是生成器类型
print('types.GeneratorType=',type((x for x in range(10)))==types.GeneratorType)

import do_animal_for_JichengAndDuotai  #这里我导入了一个我之前写的py文件

a=do_animal_for_JichengAndDuotai.Animal()
d=do_animal_for_JichengAndDuotai.Dog()
print('Dog type:',type(d)) 

print(type(d)==type(a))     #返回的结果为false,应为dog属于Dog()类型，尽管继承自Animal


#另外一种更好的判断类型的方法
#isinstance()函数可以判断某个类型是否属于该类型本身或者是该类型的父继承链上
print('dog is a dog?:',isinstance(d,do_animal_for_JichengAndDuotai.Dog))
print('dog is a animal?:',isinstance(d,do_animal_for_JichengAndDuotai.Animal))   #返回True,因为dog继承自Animal
print('animal is a dog?:',isinstance(a,do_animal_for_JichengAndDuotai.Dog))   #返回false

#isinstance还可以判断某个变量是否是某种类型中的一种
print('is [1,2,3] a list or tuple?',isinstance([1,2,3],(list,tuple)))
print('is (1,2,3) a list or tuple?',isinstance((1,2,3),(list,tuple)))
print('is 1 a list or tuple?',isinstance(1,(list,tuple)))   #1属于int


#使用dir()获取一个对象的所有属性和方法
property=dir(d)
print('dog\'s property:',property)   #这里面是获取一个对象的所有属性和方法

#新建一个类
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()

#hasattr()函数判断对象是否有某种属性
print('obj has x?',hasattr(obj,'x'))

setattr(obj,'x',20)       #设置某个属性值

print('obj x:',getattr(obj,'x'))   #获取某个属性值

#如果某个属性不存在，也可以传入一个默认值

print('obj y:',getattr(obj,'y',404))   #当某个参数不存在时，返回传入的默认值

#这里我们也可以获取某个成员函数属性，并将其赋给某个变量，这时这个变量指向这个成员函数
fn=getattr(obj,'power')
print('exe power:',fn())   #这时执行fn()和执行obj.power()的效果是一样的
print('exe power:',obj.power())   








#类型的判断可以用在函数功能执行之前，因为python当中变量的类型是动态的，所以可以先做类型判断，防止程序出错
