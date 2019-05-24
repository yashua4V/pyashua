#!/usr/bin/python3
# -*- coding: utf-8 -*-
def createCounter():
    def f():
        b=1
        while True:
            yield b
            b = b+1
    it = f()
    def counter():
        return next(it)
    return counter

# 测试:
counterA = createCounter()
print(counterA)
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')