from sqlalchemy import Column, Integer, String,Numeric
from db2 import *
from sqlalchemy import Column, Integer, String
import sqlalchemy
from decimal import Decimal
Base = sqlalchemy.orm.declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True)
    food_item = Column(String(255), unique=True)  # Specify length for String columns
    price = Column(Numeric(10, 2))
    category = Column(String(255))  # Specify length for String columns
    quantity = Column(Integer, default=0)


class User(Base):
    __tablename__= "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    role = Column(String(20))
class Config:
        orm_mode = True



