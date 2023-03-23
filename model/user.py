#!/usr/bin/python3
from model import basic
from flask import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(basic, Base):
        __tablename__ = 'users'
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        address = Column(String(256), nullable=False)
        phone = Column(String(128), nullable=False)
        gender = Column(String(128), nullable=False)
        dob_day = Column(Integer(128), nullable=False)
        dob_month = Column(Integer(128), nullable=False)
        dob_year = Column(Integer(128), nullable=False)
