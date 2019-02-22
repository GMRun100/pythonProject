#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中枚举类的使用-----------------------
from enum import Enum,unique  #python 中提供了枚举类

Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():    #说明枚举类型是可迭代的
    print(name,'=>',member,',',member.value)
    
#我们也可以从enum类派生出自定义类
@unique   #@unique 装饰器可以帮助我们检查保证没有重复值
class WeekDay(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

#访问枚举类型
day1=WeekDay.Mon
print(day1) 
print(day1.value)
print(WeekDay(2))
print(WeekDay.Sat)

#廖老师测试用例
class Gender(Enum):
    Male=0
    Female=1

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
    
    
#在实际的代码使用过程中会经常使用到枚举类型