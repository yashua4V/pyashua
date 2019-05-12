#!/usr/bin/python3
#用列表模拟栈结构、
alist=[]
def ruzhan():
    item=input('请输入要入栈的数据:\n').strip()
    if item:
        alist.append(item)

def chuzhan():
    if alist:
        print('From stack,popped %s' % alist.pop())
    else:
        print('\033[31;1mEmpty\33[0m' )

def chachan():
    print(alist)

def showmenu():
    cmds = {'1':ruzhan,'2':chuzhan,'3':chachan }
    while True:
        user_num =input('请输入要进行的操作:\n1.入栈\n2.出栈\n3.查栈\n4.退出程序\n')
        if (user_num not in '123'):
            if (user_num == '4'):
                exit(0)
            else:
                print("你输入的数字有误")

        cmds[user_num]()
if __name__ == '__main__':
    showmenu()