#!/usr/bin/python3
#-*- coding: utf-8 -*-
#@Time    :2019/6/18 14:07
#@Author  :yashua_4V
#@FileName: test.wsgi.py.py

#@Software: PyCharm
from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return[b'<h1>hello,web!</h1>']

httpd = make_server('',8000,application)
print('Serving http on port 8000')

httpd.serve_forever()