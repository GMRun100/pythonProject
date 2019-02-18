#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python中的类属性-----------------------
#每增加一个学生，将count的数量加1
class Student(object):
    count=2
    def __init__(self,name):
        self.name=name
        #self.add_count()
        self.count=self.count+1   #每创建一个该类实例，则此类属性数值加1
benliu=Student('benliu')
print('Student num:',benliu.count) 
guooujie=Student('guooujie')
print('Student num:',guooujie.count)   
print(num)

#没成功，不知道咋整了，后面我再想想！！！

