#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import reduce
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    name=name.lower()
    name=name.title()
    return name


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(L):
    def crax(x,y):
        n = x * y
        return n
    return reduce(crax,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

'''
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456：
'''
from functools import reduce

def str2float(s):
    num_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def char2num(s):
        return num_dict[s]
    L=s.split('.')
    def upnumb(x,y):
        return x*10+y
    def lownumb(x,y):
        return x/10+y
    return reduce(upnumb,map(char2num,L[0]))+reduce(lownumb,map(char2num,reversed(L[1])))/10

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
print(str2float('234534.56235234')==234534.56235234)
