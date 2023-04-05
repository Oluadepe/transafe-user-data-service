#!/usr/bin/env python3
"""
Storage instance for application
reload database on import
"""
from models.db import Database


storage = Database()
storage.reload()
