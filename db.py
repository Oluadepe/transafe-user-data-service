#!/usr/bin/python3
"""""""Database Setup and Configurations"""

import os
from flask_sqlalchemy import SQLAlchemy


# Set the enviroment variables
os.environ['TRNSF_USER'] = 'transafe_dev'
os.environ['TRNSF_PWD'] = 'transafe_dev_pwd'
os.environ['TRNSF_DB'] = 'transafe_dev_db'

# This line below is just for testing purposes
print(SQLAlchemy)
