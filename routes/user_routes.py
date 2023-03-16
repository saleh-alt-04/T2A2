from flask import Blueprint, request, jsonify
from app import db
from models.user import User

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])


@user_bp.route('/', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    new_user = User(username, email, password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.__dict__), 201


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.__dict__)


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    username = request.json.get('username', user.username)
    email = request.json.get('email', user.email)
    password = request.json.get('password', user.password)

    user.username = username
    user.email = email
    user.password = password

    db.session.commit()

    return jsonify(user.__dict__)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return '', 204
