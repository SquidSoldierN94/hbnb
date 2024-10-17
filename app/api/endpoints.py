from flask import Blueprint, jsonify, request
from business.facade import Facade

api_bp = Blueprint('api', __name__)
facade = Facade()

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = facade.get_all_users()
    return jsonify(users)

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = facade.add_user(data)
    return jsonify(user), 201
