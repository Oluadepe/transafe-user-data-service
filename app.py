#!/usr/bin/env python3
import jwt
import models
from dotenv import load_dotenv
from os import getenv
from api.v1 import api_endpoint
from werkzeug.datastructures import Headers
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, verify_jwt_in_request, get_jwt)


load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')
app.register_blueprint(api_endpoint)
app.url_map.strict_slashes = False
jwt = JWTManager(app)


@app.teardown_appcontext
def clean_up(error):
    models.storage.close()


@app.before_request
def add_token_to_header():
    token = request.cookies.get(getenv('COOKIE_NAME'))
    if token is None:
        return
    headers = Headers(request.headers)
    headers['Authorization'] = 'Bearer {}'.format(token)
    request.headers = headers


@app.before_request
def before_request():
    if request.method == 'POST' and request.path == '/api/v1/users':
        return
    try:
        verify_jwt_in_request()
        if get_jwt().get('iss') != getenv('JWT_ALLOWED_ISSUER'):
            return jsonify({'error': 'Invalid token issuer'}), 401
    except Exception as e:
        return jsonify({'status': 'error',
                        'message': str(e)}), 422


@app.errorhandler(422)
def invalid_token(error):
    return jsonify({'error': 'Invalid Token'}), 422


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(409)
def conflict(error):
    return jsonify({'error': 'email provided already in use'}), 409


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
