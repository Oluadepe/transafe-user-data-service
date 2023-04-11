#!/usr/bin/env python3
from .basic import Basic, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class User(Basic, Base):
    """Define the representation/Properties of Users

    Args:
        Basic (_type_): _This class define the common properties_
        Base (_type_): _Class that hold the OOP equivalent of SQL syntax_
    """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False, unique=True)
    address = Column(String(256), nullable=False)
    phone = Column(String(128), nullable=False)
    gender = Column(String(128), nullable=False)
    dob_day = Column(Integer, nullable=False)
    dob_month = Column(Integer, nullable=False)
    dob_year = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user.
           Based on inherited values from the parent class
        """
        super().__init__(*args, **kwargs)
