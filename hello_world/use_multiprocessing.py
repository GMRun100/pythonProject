#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中多进程的方法-----------------------
#在windows中一个任务就表示一个进程，每个进程至少会有一个线程，本文学习多进程的使用方法
""" from multiprocessing import Process   #multiprocessing模块提供了一个Process类来代表一个进程对象
import os
#子进程需要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))   #os.getpid()获取当前的进程号


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    name=input('please enter your name:')    #此处目的是暂停一下，我们可以在相应的任务管理器中找到此PID对应的进程，程序名称为python.exe
    print('hello,',name)
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
 """
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
""" from multiprocessing import Pool
import os,time,random
def long_time_task(name):
        print('Run task %s (%s)...' % (name,os.getpid()))
        start=time.time() #返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
        time.sleep(random.random()*3)
        end=time.time()
        print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p2=Pool(4)     #pool的默认大小为4，表示最多同时执行四个进程，Pool的默认大小是CPU的核数
    for i in range(5):
        p2.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p2.close()
    p2.join()    #此处等待所有子进程执行完毕
    print('All subprocesses done.') """

#进程间通讯
#Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
#下面的例子以Queue为例
from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行代码
def write(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to the queue.' % value)
        q.put(value)
        time.sleep(random.random())
#读数据进程执行代码
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))   #target=write表示要执行的函数
    pr=Process(target=read,args=(q,))
    #启动子进程
    pw.start()
    pr.start()
    pw.join()    #等待写进程执行完毕
    pr.terminate()








