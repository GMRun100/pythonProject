#-------python if条件语句的用法------------
age_str=input('please input your age:');

age=int(age_str)  #此处必须要用int()函数，因为input()返回的类型是str
if age>=6:
    print('teenger')
elif age>=18:
    print('adult')
else :
    print('kids')








#学习心得
#1.if语句后面不需要加括号，需要加：(冒号)
#2.else if 简写为elif