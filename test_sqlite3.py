#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,sqlite3
db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()
def get_score_in(low,high):
#    '返回指定区间的名字，按分数低到高排序'
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select name from user where score>=? and score<=? order by score  ',(low,high))
        values = cursor.fetchall()
        return [value[0] for value in values]
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


#测试
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('pass')