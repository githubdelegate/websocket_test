import datetime
from . import base
from sqlalchemy.orm import  relationship
from sqlalchemy import  Integer, Column, String, ForeignKey, Float, DateTime, SmallInteger

# 用户信息
class User(base):
    uid = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), nullable=False)
    remarkname = Column(String(30))
    phone = Column(String(15), nullable=False, unique=True)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    pay_date = Column(DateTime())


# // 位置信息
class Location(base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.uid'))
    lat = Column(String(50))
    lot = Column(String(50))
    time = Column(DateTime())
    speed = Column(Float)

class Userrelation(base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_user = relationship('User')
    fromuid = Column(Integer, ForeignKey('from_user.uid'))
    to_user = relationship('User')
    touid = Column(Integer, ForeignKey('to_user.uid'))
