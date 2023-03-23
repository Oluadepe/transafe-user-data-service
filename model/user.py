#!/usr/bin/python3
from flask import Column, String
from sqlalchemy.orm import relationship


class User(Base):
        __tablename__ = 'users'
        id = Column(db.Integer, primary_key=True)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)




        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
