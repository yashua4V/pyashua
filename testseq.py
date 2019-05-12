#!/usr/bin/env python3
from create_file import get_content
seq = 'asdf'
seq2 = ''
print(seq2 in seq)
lista = list(seq)
print(lista)
string = str(lista)
print(string)
tupa = tuple(lista)
print(tupa)
print(len(tupa))
print(enumerate('sdkfjal'))
for i,j in  enumerate('abc'):
    print('index:' + str(i) ,j)
print(reversed([1,2,3]))
for i in reversed([1,2,3]):
    print(i,end='' )
print()
print(sorted([1,44,223,132]))
print('%d/%d/%d %d:%d' % (2019,12,3,4,58))
'my name is{}'.format('bob')
print('{:><26}'.format('{:<>15}'.format('****')))
print(min('sdsadf2345kfjl'))
def pcontent(content):
    print('+'+'*'*50+'+')
    for ch in content:

        print('+{:^50}+'.format(ch))
    print('+' + '*' * 50 + '+')
if __name__ == '__main__':
    content = get_content()
    pcontent(content)