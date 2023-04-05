#!/usr/bin/env python3
""" Database Management """
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.basic import Basic, Base
from models.user import User


load_dotenv()


class Database:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """
        initializes class with database information from work environment
        """
        db = getenv('TRNSF_DB')
        db_user = getenv('TRNSF_USER')
        db_pwd = getenv('TRNSF_PWD')
        host = getenv('TRNSF_HOST')

        # create connection engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(db_user, db_pwd, host, db),
                                      pool_pre_ping=True)

    def all(self):
        """
        returns dictionary of all user
        """
        dic = {}
        query = self.__session.query(User).all()
        try:
            for elem in query:
                dic[elem.id] = elem
            return dic
        except Exception:
            return None

    def new(self, obj):
        """
        adds a new element to database session
        """
        self.__session.add(obj)

    def save(self):
        """
        save changes to database table
        """
        self.__session.commit()

    def get(self, **kwargs):
        """
        Get user object based on ID or Email
        """
        try:
            if 'id' not in kwargs and 'email' not in kwargs:
                return 'this one'
            if 'id' in kwargs:
                user = self.__session.query(
                                            User).filter_by(
                                            id=kwargs['id']).first()
                return user
            if 'email' in kwargs:
                user = self.__session.query(
                                            User).filter_by(
                                            email=kwargs['email']).first()
                return user
        except Exception:
            return None

    def delete(self, obj=None):
        """
        deletes an element in the table
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create database tables and define a session for performing ORM
        operations on the database
        """
        # creates database table defined in Base
        Base.metadata.create_all(self.__engine)
        # generate session object, bind it with self.__engine.
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # create scoped session out of session to manage multiple
        # session in thread safe manner
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """
        Closes current database session
        """
        self.__session.close()
