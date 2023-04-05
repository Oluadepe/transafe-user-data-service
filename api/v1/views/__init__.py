#!/usr/bin/env python3
 """ Auto initialization for view package
 """
 from flask import Blueprint

 api_endpoint = Blueprint("api_endpoint", __name__, url_prefix="/api/v1")
