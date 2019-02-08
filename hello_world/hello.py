#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#print('hello world!')
#name=input('please enter your name:')
#print('hello,',name)
#print('''line1
#line2
#line3''')
#print(r'''line1
#line2
#line3''')

#print('中文测试')

#第一种格式化字符串的方法
#前面加0当位数不够时可以补0，
#print('%2d-%05d' % (3000,1))
#print('%.5f' % 3.1) 

#第二种格式化字符串的方法，采用format,用这种方法比用%方法要麻烦
print('Hello,{0},成绩提升了{1:.1f}%,{2}'.format('小明',17.125,'haha'))