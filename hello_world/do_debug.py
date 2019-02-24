#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中调试的方法-----------------------
#第一种方法是代码中添加print(),把代码中所有可能出错的地方print()出来，这种方法的坏处是代码调试完毕print()需要被注释掉，实际使用过程中确实比较麻烦
#而且使用print运行过程中还会包含很多垃圾


#第二种方法：使用断言
def foo(s):
    n=int(s)
    #assert的作用是n!=0应该为true,否则后面的程序会出错，如果断言失败，程序会抛出异常AssertionError
    assert n!=0,'n is zero'   
    return 10/n

def main():
    foo(2)

main()

#第三种方法：使用logging
import logging
#logging允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging.basicConfig(level=logging.WARNING) #通过不同的level，我们可以选择输出不同的信息
def foo_log(s):
    n_log=int(s)
    logging.info('n_log=%d' % n_log)
    logging.warning('now is warning n_log=%d' % n_log)
    return 10/n_log

foo_log('2')


#写程序最痛苦的过程莫过于调试，廖老师说了，logging才是终极武器，哈哈~~

#本章节很重要

