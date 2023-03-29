#!/usr/bin/env python3
from .basic import Basic, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class User(Basic, Base):
    """
    'users' table column definitions
    """
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
