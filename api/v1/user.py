#!/usr/bin/env python3
import models
import requests
from os import getenv
from models.user import User
from api.v1 import api_endpoint
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import abort, jsonify, request, session


@api_endpoint.route('/users', methods=['GET'])
@jwt_required()
def view_all_users():
    """
    returns all user object
    only admin can access this route
    """
    # validate if client is an admin
    claim = get_jwt()
    if 'role' not in claim:
        abort(422)
    if getenv('ADMIN_ROLE') != claim.get('role'):
        abort(401)

    # fetch all users from database
    users = models.storage.all().values()
    if users is None or not users:
        return jsonify({"error": "no users found"}), 404

    # edit output
    all_users = []
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
    return jsonify({
        "status": "success",
        "message": "successfully retrieved all users",
        "data": all_users
        }), 200


@api_endpoint.route('/users', methods=['POST'])
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
    if gender.lower() not in ['male', 'female']:
        return jsonify({'error': 'Invalid gender type'})
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
        return jsonify({'status': 'error',
                        'message': 'user already exists'}), 409

    # creates the user
    try:
        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, gender=gender, address=address,
                        phone=phone, dob_day=dob_day, dob_month=dob_month,
                        dob_year=dob_year)
        new_user.save()
    except Exception:
        abort(400)
    return jsonify({'status': 'success',
                    'message': 'user created'}), 200


@api_endpoint.route('/users/<string:char>', methods=['GET'])
@jwt_required()
def view_one_user(char):
    """
    view current based on session or ID
    """
    if char == 'me' or '-' in char:
        identity = get_jwt_identity()
        role = get_jwt().get('role')

        # checks if user has view right
        if '-' in char and len(char) != 36:
            abort(400)
        if char != get_jwt().get('sub') and role != getenv('ADMIN_ROLE') and char != 'me':
            abort(401)
        if role not in [getenv('ADMIN_ROLE'), getenv('USER_ROLE')]:
            abort(401)

        # retrieve and return user
        user = models.storage.get(id=identity)
        if user is None:
            abort(404)
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
    else:
        abort(400)


@api_endpoint.route('/users/<string:me_or_id>', methods=['DELETE'])
@jwt_required()
def delete_user(me_or_id):
    """
    deletes a user based on given user ID
    """
    if '-' not in me_or_id and me_or_id != 'me':
        abort(400)
    if '-' in me_or_id and len(me_or_id) != 36:
        abort(400)

    # get user identity
    identity = get_jwt_identity()
    if '-' in me_or_id and identity != me_or_id:
        if get_jwt().get('role') != getenv('ADMIN_ROLE'):
            abort(401)
        else:
            identity = me_or_id

    if get_jwt().get('role') not in [getenv('ADMIN_ROLE'), getenv('USER_ROLE')]:
        abort(401)

    # retrieve user from database
    user = models.storage.get(id=identity)
    if user is not None:
        user.delete()
        models.storage.save()
        # removed user cookie
        return jsonify({'status': 'success',
                        'message': 'user deleted successfully'}), 200
    abort(404)


@api_endpoint.route('/users/<string:me_or_id>', methods=['PUT'])
@jwt_required()
def update_user(me_or_id):
    """
    update user details
    """
    if me_or_id == 'me':
        identity = get_jwt_identity()
    elif '-' in me_or_id:
        if getenv('USER_ROLE') != get_jwt().get('role'):
            if getenv('ADMIN_ROLE') != get_jwt().get('role'):
                abort(401)
            else:
                identity = me_or_id
        else:
            identity = get_jwt_identity()
    else:
        abort(400)

    # validate user from authentication service
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    dob_month = request.json.get('dob_month', None)
    dob_year = request.json.get('dob_year', None)
    dob_day = request.json.get('dob_day', None)
    phone = request.json.get('phone', None)
    address = request.json.get('address', None)
    email = request.json.get('email', None)

    user = models.storage.get(id=identity)
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
        if user.email == email:
            abort(409)
    # line below will be removed once email modification is enabled
    if email is not None:
        return jsonify({'error': 'cannot modify email address'}), 400

    # use SMTP to confirm email change from user
    user.save()
    return jsonify({'status': 'success',
                    'message': 'user updated seccessfully'}), 200
