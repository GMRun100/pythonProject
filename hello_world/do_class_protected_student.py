#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------学习python 类添加访问限制的用法
#类名最好以大写字母为开头
class Student(object):   #在python中如果不确定类继承自哪个类可以直接写object

    def __init__(self,name,score):      #初始化参数，必须要有self参数
        self.__name=name                #变量名前面加上两个下划线，就表示为私有变量
        self.__score=score
    
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
        
    def get_name(self):      #由于名字已经被私有化，所以要通过公有的函数来调用私有变量
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self,score):  #这里我们可以对输入的参数做判断，防止输入无效的参数
        if 0<=score<=100:      #C++是不能这么写的，还是python NB!
            self.__score=score
        else:
            raise ValueError('bad score')


bart=Student('Bart Simpson',59)
#print('name:',bart.__name)   #由于name已经被定义成私有变量，所以是无法通过实例直接调用的
print('name:',bart.get_name())
print('score:',bart.get_score())
bart.set_score(99)
print('new score:',bart.get_score())
