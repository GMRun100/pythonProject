#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------学习python 当中的继承和多态---------------
class Animal(object):   #当我们定义一个类的时候，实际上就是在定义一种数据类型
    def run(self):
        print('Animal is running...')


#继承一个非常大的好处是可以直接调用父类的方法
class Dog(Animal):
    def run(self):     #这里面我们用子类的run()函数覆盖了父类的run()函数，在代码实际运行的时候，总是会调用子类的run()函数，这就叫多态
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog=Dog()
dog.run()

print('dog type:',type(dog))   #通过type函数可以判断对象的类型

cat=Cat()
cat.run()

#--------------多态具体有什么好处呢，请看下面-------------------
#当我们编写一个函数需要调用到一个基类下面不同的子类时，我们可以将函数的参数设置为基类类型，调用基类的方法。
#由于python是动态语言，所以变量的类型是不固定的，下面这个函数，只要传入的类具有run()成员函数，都可以被当成是animal
#但是在C++语言等静态语言当中，下面的参数类型必须为Animal基类或者其子类
def run_twice(animal):     
    animal.run()            #这里我们我们根本不关心子类的run()函数是如何实现的，而当我们新加一个子类时，也只需要将run()函数写好即可
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

#以下是廖老师的原话：
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对扩展开放：允许新增Animal子类；

# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

