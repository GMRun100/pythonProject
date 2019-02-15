#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------学习python中filter函数的用法--------------------
#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#例：删除一个数列中的偶数
def is_odd(n):
    return n%2==1
num=list(range(5))
l=list(filter(is_odd,num))   #由于filtet返回的结果是Iterator,所以用list函数得到所有的结果
print(l)

#当然我们也可以不用list函数
x=filter(is_odd,num)
for x1 in x:
    print(x1)      #在for循环中，不用再需要next，感觉for循环隐含的在调用next(x)函数


#当然我们也可以自己调用next()函数  
num2=filter(is_odd,num)
num_tmp=num2
while True:
    try:
        print(num_tmp)
        num_tmp=next(num2)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
    
   