from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    email = Column(String)
    password = Column(String)
    permission = Column(String)

class billet(Base):
    __tablename__ = 'billet'
    no = Column(Integer, primary_key=True, index=True)
    number = Column(String)
    timestamp = Column(DateTime)
    file_name = Column(String)