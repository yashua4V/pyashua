#!/usr/bin/python3
# -*- coding: utf-8 -*-
from  sqlalchemy  import Column,String, create_engine
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    #表的名字：
    __tablename__ = 'user'

    #表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

#初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root:YYfIaUxJIVT2xjLQ14ZoNRJUL@localhost:3306/test')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#向数据库中添加一行记录，可以视为添加一个user对象
#创建Session:
session = DBSession()
#创建新User对象:
new_user = User(id='6',name='bob')
#添加到session:
session.add(new_user)
#提交即保存到数据库：
session.commit()
#关闭session:
session.close()


#创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行：
session = DBSession()
user = session.query(User).filter(User.id=='5').one()
#打印类型和对象的name属性：
print('type:',type(user))
print('name:',user.name)
session.close()