#!/usr/bin/env python3
from flask import Blueprint
"""
Defined Blueprint
"""

api_endpoint = Blueprint('user_views', __name__, url_prefix='/api/v1')

from api.v1.user import *
