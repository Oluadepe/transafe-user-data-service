""" Module of Users views
 """
 from api.v1.views import api_endpoint
 from flask import jsonify, request
 from models.user import User


 @api_endpoint.route('/users', methods=['GET'], strict_slashes=False)
 def get_all_user() -> str:
    """ GET /api/v1/users
    Return:
       - list of all transafe User object
    """

    return ""
