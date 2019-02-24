#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中多线程的方法-----------------------
#在python中提供了threading这个高级模块
import time,threading,multiprocessing

""" def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)    #推迟调用线程的运行，参数指秒数
    print('thread %s is ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)   #主线程的名称默认为MainThread
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()  #等待直至线程终止
print('thread %s ended.' % threading.current_thread().name) """

#当多个线程操作同一个变量时，需要用线程锁
#例
balance=0
lock=threading.Lock()   #lock为Lock类型的一个实例

def change_it(n):
    global balance    #在python当中变量默认为局部变量，加上global表示此变量为全局变量
    balance=balance+n
    balance=balance-n

def run_thread(n):
    
    for i in range(1000):
        #获取锁
        lock.acquire()   #当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
        #print('thread %s is running i=%s' % (threading.current_thread().name,i))     #通过打印信息可以看出线程在交替执行
        try:
            change_it(n)
        finally:
            #释放锁
            #print('thread %s ended' % threading.current_thread().name)
            lock.release()    #获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放
            pass

t1=threading.Thread(target=run_thread,args=(5,),name='t1')
t2=threading.Thread(target=run_thread,args=(8,),name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print('balance=',balance)

####查看cpu的核数
print('cpu number is : %s' % multiprocessing.cpu_count())    #可以看出我的电脑是4核的