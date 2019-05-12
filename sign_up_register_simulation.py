#!/usr/sbin/pyton3
import getpass
userinfo={}
def register():
    user_name= input('请输入用户名\n')
    while True:
        if user_name  in userinfo:
            user_name = input('用户名已存在，请重新输入\n')
        else:
            break
    password = input('请输入密码\n')
    userinfo.update({user_name:password})

    pass
def sign_up():
    login_name = input('请输入用户名\n')
    login_pass = getpass.getpass('请输入用户名\n')
    while True:
        if login_name not in userinfo:
            login_name = input('用户名不存在，请重新输入\n')
        else:
            break
    while True:
        if userinfo.get(login_name) != login_pass:
            login_pass = input('密码不匹配，请重新输入\n')
        else:
            print('登录成功')
            break
    pass
def show_menu():
    cmds = {'1':register,'2':sign_up}
    while True:
        formatword='欢迎访问linke.com.请选择下列指令中的一项执行\n1.注册\n2.登录\n3.退出\n（1\\2\\3):\n'
        choice = input(formatword)
        if choice == "3":
            exit(0)
        if choice not in '12':
            print('入有误，请重新输入')
        else:
            cmds[choice]()

if __name__ == '__main__':
    show_menu()