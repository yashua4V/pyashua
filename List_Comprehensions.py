#!/usr/bin/python3
import os
'''
列表生成式
'''
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'abcd' for n in 'xyz'])
print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print (d.items())
##for j in d.items():
##    print(j)
print([k+'='+v for k,v in d.items()])
L = ['Hello', 'World', 18, 'Apple', None]
print( [s for s in L if  isinstance(s,str) ])
L2 = [s.lower() for s in L if  isinstance(s,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')