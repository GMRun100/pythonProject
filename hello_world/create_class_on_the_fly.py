#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中元类的使用-----------------------
#我们通常意义上的类的定义方法
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s.' % name)
h=Hello()
h.hello()

#下面是通过type()函数来定义类
#先自定义类中可能要关联的函数，注意别忘了形参self
def fn(self,name='world'):    
    print('Hello2,%s.' % name)

#功能:通过type函数创建一个类
#参数一：类的名称
#参数二：tuple类型，父类的集合
#参数三：类的方法名称与函数绑定
Hello2=type('Hello2',(object,),dict(hello2=fn))    #这种实现方式相当于在运行期间动态的创建类
h2=Hello2()
h2.hello2()

#廖老师说元类的使用基本用不到，那就先不浪费时间研究了~~