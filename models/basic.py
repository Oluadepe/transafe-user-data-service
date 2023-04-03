#!/usr/bin/env python3
""" Base class for transafe user service """
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4


Base = declarative_base()

class Basic:
    """
    Defines all common attributes and methods
    for all other models
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """ Initializes the basic class """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        string representation of object
        """
        return "[{:s}] with identity number: ({:s})\n{}\n{}\n{}".format(
               self.__class__.__name__, self.id, '*' * 75, self.__dict__,
               '*' * 75)

    def save(self):
        """ update 'update time' and saves instance to database """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ """
        pass

    def delete(self):
        """ deletes instance """
        pass
