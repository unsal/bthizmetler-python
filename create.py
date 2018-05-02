from flask import Flask
from db.connection import Connect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, TIMESTAMP)
from sqlalchemy import exc
from datetime import datetime

Base = declarative_base()

class Projeler(Base):
    __tablename__ = 'projeler'
    id = Column(Integer(), primary_key=True)
    yil = Column(String(4))
    grup = Column(String(10))
    baslik = Column(String(100))
    aciklama = Column(String(255))
    birim = Column(String(20))
    durum = Column(String(1))
    zamandamgasi = Column(TIMESTAMP, default = datetime.now())

class DB():
    def __init__(self):
        self.conn = Connect()
        self.session = self.conn.session()
        self.engine = self.conn.engine

    def __del__(self):
        self.session.close()

    def createBase(self):
        try:
            Base.metadata.create_all(self.engine)
        except exc.SQLAlchemyError:
            print("DB Error ", exc)


if __name__ == "__main__":
    db = DB()
    db.createBase()

    # print("Base created successfully..")