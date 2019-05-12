#!/usr/bin/python3
#字符串的内建函数
mystr = 'hello'
print(mystr.capitalize())
print(mystr.title())
print(mystr.center(50,'*'))
print(mystr.count('l'))
mystr = 'this is a test string'
print(mystr.count('is'))
print(mystr.count('t',0,1))
print(mystr.endswith('g'))
print(mystr.endswith('s',0,4))
print(mystr.upper())
print(mystr.isupper())
print(mystr.lower())
print(mystr.islower())
print(mystr.isdigit())
print(mystr.isalpha())
mystr='12345'
print(mystr.isdigit())
mystr='linke'
print(mystr.isalpha())
mystr = 'this is a test string'
#split(str) 以str 为准分割字符串，返回列表
print(mystr.split(' '))
print(mystr.split(' ',2))
mystr = '  ni hao  '
print(mystr.strip())