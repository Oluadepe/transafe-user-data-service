#!/usr/bin/env python3
""" Base class for transafe user service """
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4
import models


Base = declarative_base()


class Basic:
    """
    Defines all common attributes and methods
    for all other models
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

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
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        string representation of object
        """
        return "[{:s}] with identity number: ({:s})\n{}\n{}\n{}".format(
               self.__class__.__name__, self.id, '*' * 75, self.__dict__,
               '*' * 75)

    def save(self):
        """
        save/update current instance
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary representation of object
        """
        dic = dict(self.__dict__)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dic.keys():
            del dic['_sa_instance_state']
        return dic

    def delete(self):
        """ deletes instance object """
        models.storage.delete(self)
