#!/usr/bin/python3
print(dict())
print(dict(['ab']))
s = dict([('name', 'bob'), ('age', 16)])
print(type(s))
a = {}.fromkeys(['bob','lili','yiliya'],19)
print(len(a))
print(len(s))
print ("bob" in s,end='')
print('bob' in a)
for key in a:
    print('%s:%s' % (key ,a[key]))
print("%(bob)s,%(lili)s" % a)
#字典赋值，有KEY更新，无KEY新增
#del 删除字典中的元素或整个字典
del s['name']
print(s)
#del s
#a.clear()
a.pop('bob')#字典无序，弹出方法需指定key
print(a)
#z字典的KEY必须是不可变对象
print(hash(10))
print(hash('abc'))
#print(hash([1,2]))
print(a.get("lili"))
print(a.get("bob",'12345'))
print(a.keys())
print(a.values())
print(a.items())
a.update(s)#更新，合并其他字典
print(a)
