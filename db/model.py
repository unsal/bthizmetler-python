from sqlalchemy import (Column, String, Integer, TIMESTAMP)
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Projeler(Base):
    __tablename__ = 'projeler'
    id = Column(Integer(), primary_key=True)
    yil = Column(String(5))
    grup = Column(String(10))
    baslik = Column(String(255))
    aciklama = Column(String(1000))
    sonuc = Column(String(1000))
    birim = Column(String(20))
    durum = Column(String(1))
    zamandamgasi = Column(TIMESTAMP, default = datetime.now())



