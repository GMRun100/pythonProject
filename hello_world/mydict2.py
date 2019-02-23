# mydict2.py
#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中文档测试的方法-----------------------
#另外一个编写的文档测试用例参见myfact.py代码
class Dict(dict):
    '''   #表示多行代码
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()   
    >>> d1['x'] = 100
    >>> d1.x
    100               #doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...   #只有测试异常的时候，可以用...表示中间一大段烦人的输出
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

#一下代码在模块正常导入时，不会执行，只有在命令行运行时，才会执行
if __name__=='__main__':
    import doctest
    doctest.testmod()