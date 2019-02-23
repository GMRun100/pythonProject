#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#练习廖老师的文档测试方法
def fact(n):
    #执行文档测试
    '''
    Calculate 1*2*3*....*n
    >>> fact(1)   #注意添加空格
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    #文档测试结束
    #函数功能：
    if n<1:
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)

if __name__=='__main__':
    import doctest
    doctest.testmod()
