#!/usr/bin/env python3
from .basic import Basic, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import bcrypt


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
    password = Column(String(128), nullable=False)
    address = Column(String(256), nullable=False)
    phone = Column(String(128), nullable=False)
    gender = Column(String(128), nullable=False)
    dob_day = Column(Integer(128), nullable=False)
    dob_month = Column(Integer(128), nullable=False)
    dob_year = Column(Integer(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user.
           Based on inherited values from the parent class
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password by first encoding to bytes.
           Then use bcrypt hashing, for secure staorable value.
        """
        if name == "password":
            value = value.encode()
            salt = bcrypt.gensalt()
            hash_pwd = bcrypt.hashpw(value, salt)
        self.__setattr__(name, hash_pwd)
