#学习python中函数的使用分享
#最近在学习廖雪峰老师的python教程，先将自己学习过程中写的py文件与大家分享
#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------学习python 函数的用法----------------
#在编程的过程中，我们借助函数来实现代码的抽象表达，
#通过借助抽象，我们可以不关心底层代码的具体实现方式，而直接在更高的层次上思考问题
#在python中用def来定义函数，最后要添加：(冒号)
import math   #导入math包
def my_abs(x):
     if not isinstance(x,(int,float)):   #数据类型检查可以用内置函数isinstance()
        raise TypeError('bad operand type')
     if x>0:
        return x
     else:
        return -x
x_r=my_abs(-66)
print(x_r)
	 
#定义一个空函数
def nop():
    pass	   #pass可以用来做占位符
	 
print('nop')
#---------------python 函数返回多个值的情况------------------
def move(x,y,step,angel=0):
    nx=x+step*math.cos(angel)
    ny=y+step*math.sin(angel)
    return nx,ny

x,y=move(100,100,60,math.pi/6)
print(x,y)

r=move(100,100,60,math.pi/6)
print(r[1])   #函数多个返回值是一个tuple类型

#-----默认参数---------------------------------
def power(x,n=2):
    s1=1
    while n>0:
        n=n-1
        s1=s1*x
    return s1
x=power(5)
print(x)
x=power(5,3)
print(x)

#--------当有多个默认参数时
def enroll(name,gender,age=6,city='Beijing'):
    print('name',name)
    print('gender',gender)
    print('age',age)
    print('city',city)
enroll('benliu','M',city='tianjin')    #当只想使用某些默认参数时，直接指定参数名即可

#--------可变参数，可变参数可以当参数是list或者是tuple时使用
#函数功能：计算传入参数的平方和：a^2 + b^2 + c^2 + ……
def calc(*number):
    print(number)           #我们可以发现在函数内部将可变参数转化成了tuple类型
    sum=0
    for n in number:
       sum=sum+n*n
    return sum
print(calc(1,3,5,7))	
nums=[1,2,3]
print(calc(*nums))          #这里面我们给函数传递的是list类型

#----------关键字参数--------
#关键字参数可以用于当参数需要传入dict类型时
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('guooujie',30)     #传入参数时，我们可以不传入关键字参数，但是定义函数时关键字参数不需要给出默认参数
extra={'city':'Beijing','job':'Engineer'}
person('weiyongxin',24,**extra)   #注意，这里函数内部KW获得的是extra的一份拷贝，对KW的改动不会影响到函数外的extra
	
#------命名关键字参数------------
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name,age,*,city,job):    #命名关键字也可以有默认值
    print(name,age,city,job)
person2('Jack',24,city='Beijing',job='Engineer')    #给命名关键字赋值时，必须要加上city指明给哪个命名关键字赋值

#-----------参数组合使用----------------
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
#下面是见证神奇的时刻
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。----就问你服不服，服不服！但是实际中应该很少会这样用，可理解性较差

#---------------递归函数:函数内部调用函数本身-----------------
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(5))

#---------------学习心得--------------------
#当在python中没想好函数具体怎么是现实时，可以先用pass语句，这样可以保证程序编译通过
#在python中函数返回多个值实际上是返回tuple类型，可以用多个变量同时接受这个tuple值，python会按照位置顺序进行赋值
#在python中，函数中如果没有添加return语句，会自动返回return None.这一点与C++语言不同，C++语言中函数必须定义返回值，否则编译会报错
#函数中设置默认参数的好处是可以降低函数调用的复杂度
#定义默认参数要注意：定义默认参数必须指向不变对象，像数字，字符串等等
#可以把可变参数理解为传入地址指针
#在python中有五种参数类型：必选参数，默认参数，可变参数，关键字参数，命名关键字参数。
#当在程序中需要组合使用这些参数时，参数定义的顺序必须是必选参数，默认参数，可变参数，命名关键字参数，关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。感觉python的用法真的是太灵活了。。。有点烧脑。。。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
