#!/usr/bin/env python3
""" Database Management """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.basic import Basic, Base
from models.user import User


class Database:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """
        initializes class with database information from work environment
        """
        db = getenv('MYSQL_DB')
        db_user = getenv('MYSQL_USER')
        db_pwd = getenv('MYSQL_PWD')
        host = getenv('MYSQL_HOST')

        # create connection engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(db_user, db_pwd, host, db),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """ """
        pass

    def new(self, obj):
        """ """
        pass

    def save(self, obj):
        """ """
        pass

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
