#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中一些特殊函数的使用-----------------------
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return  'Student object (name:%s)' % self.name
    __repr__=__str__
    
    def __getattr__(self,attr):
        if attr=='score':
            return 99
            
        if attr=='age':
            return lambda:25
        #对于没有属性，我们也可以让程序抛出异常
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        #return 'no such attr'
        
print(Student('benliu'))    #此时调用的为__str__

s=Student('guooujie')
print(s)                    #看教程的意思是会调用__repr__函数

print('s.socre:',s.score)   #对于类当中没有的属性，会调用__getattr__函数
print('s.age:',s.age())     #此处我们传入的为一个函数

#通过callable()函数可以判断某个对象能否被直接调用
print('s is callable?',callable(s))   #此处我们发现s不能被直接调用

class Student2(object):
    def __init__(self,name):
        self.name=name
    
    def __call__(self):
        print('My name is %s.' % self.name)

s2=Student2('benliu')
print('s2 is callable?',callable(s2))   #这里s2对象就可以被直接调用
s2()   #此处我们直接调用s2



