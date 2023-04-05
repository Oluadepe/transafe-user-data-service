#!/usr/bin/env python3
import models
import requests
from models.user import User
from api.v1 import api_endpoint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, request, session


@api_endpoint.route('/users', methods=['GET'])
@jwt_required()
def view_all_users():
    """
    returns all user object
    """
    # validate super_user/Admin token from authentication service
    users = models.storage.all().values()
    all_users = []
    dic = {}
    for item in users:
        dic = item.to_dict()
        dict_ = {
            'dob': {
                'day': dic.pop('dob_day'),
                'month': dic.pop('dob_month'),
                'year': dic.pop('dob_year')
            }
        }
        dic.update(dict_)
        all_users.append(dic)
    return jsonify(all_users), 200


@api_endpoint.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    if request.headers.get('Content-Type') != 'application/json':
        return jsonify({'error': 'Invalid Content-Type'}), 400

    # Check if all the required fields are present in the request
    required_fields = ['first_name', 'last_name', 'gender', 'address',
                       'email', 'phone', 'dob_day', 'dob_month', 'dob_year']
    if not all(field in request.json for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # retrieve user data from request
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    gender = request.json.get('gender')
    address = request.json.get('address')
    phone = request.json.get('phone')
    dob_day = request.json.get('dob_day')
    dob_month = request.json.get('dob_month')
    dob_year = request.json.get('dob_year')

    # checks if user inputed right datatype for dob
    dob_ = [dob_day, dob_year, dob_month]
    if not all(isinstance(dob, int) for dob in dob_):
        abort(400)

    # check if user already exists
    user_exist = models.storage.get(email=email)
    if user_exist is not None:
        return jsonify({'error': 'user already exists'}), 400

    # creates the user
    try:
        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, gender=gender, address=address,
                        phone=phone, dob_day=dob_day, dob_month=dob_month,
                        dob_year=dob_year)
        new_user.save()
    except Exception:
        abort(400)
    return jsonify({'success': 'user created'}), 200


@api_endpoint.route('/users/<string:char>', methods=['GET'])
@jwt_required()
def view_one_user(char):
    """
    view current based on session or ID
    """
    if char == 'me':
        # validate user from current session
        # return user object
        pass
    elif '-' in char:
        # valid user from authentication service
        user = models.storage.get(id=char)
        user = user.to_dict()
        dict_ = {
            'dob': {
                'day': user.pop('dob_day'),
                'month': user.pop('dob_month'),
                'year': user.pop('dob_year')
            }
        }
        user.update(dict_)
        if user:
            return jsonify(user), 200
        abort(404)
    abort(400)


@api_endpoint.route('/users/<string:ID>', methods=['DELETE'])
@jwt_required()
def delete_user(ID):
    """
    deletes a user based on given user ID
    """
    if '-' not in ID:
        abort(400)
    if not isinstance(ID, str):
        abort(400)
    # Validate user from authentication service
    user = models.storage.get(id=ID)
    if user:
        user.delete()
        models.storage.save()
        # removed user cookie
        return jsonify({'success': 'user deleted successfully'}), 200
    abort(404)


@api_endpoint.route('/users/<string:ID>', methods=['PUT'])
@jwt_required()
def update_user(ID):
    """
    update user details
    """
    # validate user from authentication service
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    dob_month = request.json.get('dob_month', None)
    dob_year = request.json.get('dob_year', None)
    dob_day = request.json.get('dob_day', None)
    phone = request.json.get('phone', None)
    address = request.json.get('address', None)
    email = request.json.get('email', None)

    user = models.storage.get(id=ID)
    if user is None:
        abort(404)

    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name
    if dob_month is not None:
        user.dob_month = dob_month
    if dob_year is not None:
        user.dob_year = dob_year
    if dob_day is not None:
        user.dob_day = dob_day
    if phone is not None:
        user.phone = phone
    if address is not None:
        user.address = address
    if email is not None:
        # use SMTP to validate and change user email
        pass
    user.save()
    return jsonify({'status': 'OK',
                    'message': 'user updated seccessfully'}), 200
