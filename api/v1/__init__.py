#!/usr/bin/env python3
from flask import Blueprint
"""
Defined Blueprint
"""

user_views = Blueprint('user_views', __name__, url_prefix='/api/vi')

from api.v1.users import *
