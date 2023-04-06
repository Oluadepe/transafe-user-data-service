#!/usr/bin/env python3
import jwt
import models
from dotenv import load_dotenv
from os import getenv
from api.v1 import api_endpoint
from flask import Flask, jsonify
from flask_jwt_extended import (
        JWTManager, jwt_required, verify_jwt_in_request, get_jwt_identity,
        )


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
def before_request():
    try:
        verify_jwt_in_request()
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.errorhandler(422)
def invalid_token():
    return jsonify({'error': 'Invalid Token'})


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'user does not exists'}), 404


if __name__ == '__main__':
    app.run()
