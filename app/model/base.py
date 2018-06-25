
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Integer, Column, String, ForeignKey, Float, DateTime, SmallInteger

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())