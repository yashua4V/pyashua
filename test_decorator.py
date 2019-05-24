#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import functools
import time
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call')
        fs = func(*args,**kw)
        print('end call')
        print('%s executed in %s ms' % (func.__name__, 1))
        return fs
    return wrapper

@log
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

@log
def println():
    print('asd')

@log
def fast(x, y):
    time.sleep(0.0012)
    print('ing')
    return x + y;

@log
def slow(x, y, z):
    time.sleep(0.1234)
    print('2ing')
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

