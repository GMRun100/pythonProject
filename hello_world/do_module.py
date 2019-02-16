#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------学习python 模块的用法---------------
'a test module'    #对模块添加说明    在命令行交互模式下，我们可以运行do_module.__doc__命令就可以看到这个注释

__author__='GM'     #本模块的作者

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello world')
    elif len(args)==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')
#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':         
    test()                 #这里需要运行do_module.test()命令才能运行test()函数
    
    
#在python当中，如果某些模块或者变量只希望在模块内部被使用，可以用_作为前缀
def _private_1(name):    #在python中私有变量不应该被直接引用
    print('Hello %s' % name)
        
def _private_2(name):
    print('Hi %s' % name)   

def greeting(name):        #在这里我们将具体的处理方法用私有变量封装起来，而不用关心内部的私有函数细节，这也是函数抽象的一种体现
    if(len(name)>3):
        _private_1(name)
    else:
        _private_2(name)


#我们应该将外部不需要引用的变量全部定义成private，只将外部需要引用的函数定义成public