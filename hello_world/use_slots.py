#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python slots属性-----------------------
#我们可以利用slots限制类的属性
class Student(object):
    __slots__=('name','age')     #我们通过slots限制类只能有name和age两个属性

s=Student()
s.name='benliu'
s.age=28
#s.score=99    #会报错，因为Student没有score的属性

class GraduateStudent(Student):
    pass

g=GraduateStudent()
g.score=99
print('g.score:',g.score)         #slot属性只对当前类实例起作用，对子类不起作用