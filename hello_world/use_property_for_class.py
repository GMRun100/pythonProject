#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 对class使用@property-----------------------
#可以对学生设置分数的同时，判断其是否合理
class Student(object):
    @property
    def score(self):            #此处相当于get_score()函数
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score=value
        
s=Student()
s.score=60    #此处相当于调用set_score
print('s.score:',s.score)
#s.score=9999

#廖老师安排的一个课后练习
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        if not isinstance(width,int):
            raise ValueError('width must be an interger')
        self._width=width
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,height):
        if not isinstance(height,int):
            raise ValueError('height must be an interger')
        self._height=height
    @property
    def resolution(self):
        self._resolution=self._width*self._height
        return self._resolution     #对于get属性，需要return函数
        #print(self._resolution)
        
        
        
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
    
    
#property属性非常好用，以后要学会利用