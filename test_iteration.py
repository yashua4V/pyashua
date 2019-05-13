#!/usr/bin/python3
'''
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''

def findMinAndMax(L):
    if L == []:
        return(None,None)
    max = L[0]
    min = L[0]
    if len(L) >1:
        for i, value in  enumerate(L):
            if max < L[i+1]:
                max = L[i+1];
#            print( L[i+1])
            if i+1 == len(L)-1:
                break

        for i ,value in  enumerate(L):
            if min > L[i+1]:
                min = L[i+1];
#                print(value,L[i+1])
            if i+1 == len(L)-1:
                break
    return(min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print(findMinAndMax([7, 1, 3, 9, 5]),'测试失败!4')
else:
    print('测试成功!')