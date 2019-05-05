#!/usr/bin/env python3
import os
def get_fname():
    '判断文件是否存在'
    while True:
        fname = input('filename')
        if not os.path.exists(fname):
            break
        print('%s already exists!')
    return fname

def get_content():
    '获取用户输入内容存放列表'
    content = []
    print('输入数据，输入end退出')
    while True:
        data = input('>')
        if data == 'end':
            break
        content.append(data)
    return content

def wfile(fname,content):
    '将内容写入到文件'
    content= ['%s\n' %line for line in content]
    with open(fname,'w') as f:
        f.writelines(content)
        f.close()

if __name__ == '__main__':
    fname   = get_fname()
    content = get_content()
    wfile(fname,content)
