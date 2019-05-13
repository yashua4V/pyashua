#!/usr/bin/python3
L = [ 'Lisa','John','Alice','Bob']
print(L[0:3])
print(L[:4])
L=list(range(100))
print(L)
print(L[10:20])
print(L[-1])
print(L[-2])
print(L[:-10])
print(L[1::2])
a=L.copy()
print(a)

def trim(s):
    head =0
    slenght = len(s)
    if s == '':
        return ''
    while True:
        if s[head] == ' ':
            head += 1
            if head == slenght:
                return ''
        else:
            break
    tail =-1
    while True:
        if s[tail] == ' ':
            tail -= 1
        else:
            break
    tail += 1
    if tail == 0:
        return s[head:]

    return s[head:tail]

print(trim('     hello    '))
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!7')