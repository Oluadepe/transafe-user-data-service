#!/usr/bin/env python3
from api.v1 import user_views
from flask import abort, jsonify, request


@user_views.route('/users', methods=['GET'])
def all_users():
    """
    """
    return jsonify()

@user_views.route('/users/<int:ID>', methods=['GET'])
def one_user(ID):
    """
    """
    return jsonify()

@user_views.route('/users/
