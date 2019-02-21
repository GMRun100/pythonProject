#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 对class使用多重继承-----------------------
#在C++中我们也经常用到多重继承
class Animal(object):
    pass
#哺乳动物类
class Mammal(Animal):
    def born_child(self):
        print('Mammal can give birth')

#鸟类
class Bird(Animal):
    def born_egg(self):
        print('bird can born an egg')

#为了更好的看出类的继承关系，对于额外的功能，我们在命名时后缀最好加上MixIn
class RunnableMixIn(object):
    def run(self):
        print('running.....')
        
class FlyableMixIn(object):
    def fly(self):
        print('flying.....')


#狗：既是哺乳动物又具有跑的功能
class Dog(Mammal,RunnableMixIn):
    pass

dog=Dog()
if hasattr(dog,'born_child'):
    dog.born_child()
if hasattr(dog,'run'):
    dog.run();