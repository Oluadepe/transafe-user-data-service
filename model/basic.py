#!/usr/bin/env python3
""" Base class for transafe user service """
from sqlalchemy import Column, String, DateTime
from datetime.datetime import utcnow(), strptime
from uuid import uuid4


class Basic:
    """
    Defines all common attributes and methods
    for all other models
    """
    id = Column(String(60), unique=True, nullable=False, primary=True)
    created_at = Column(DateTime, nullable=False, default=utcnow())
    updated_at = Column(DateTime, nullable=False, default=utcnow())

    def __init__(self, *args, **kwargs):
        """ Initializes the basic class """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())
            if "created_at" not in kwargs:
                self.created_at = utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = utcnow()
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = utcnow()

    def __str__(self):
        """ """
        pass

    def save(self):
        """ """
        pass

    def to_dict(self):
        """ """
        pass

    def delete(self):
        """ """
        pass
