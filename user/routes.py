from flask import jsonify, request,abort
import jwt
import datetime


from . import user
from .models import User
from Auth.auth import encode_auth_token


@user.route('/signup', methods=['POST'])
def signup():

    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({
            'success': False,
            'message': 'Email already exists'
            }), 400
    existusername = User.query.filter_by(username=username).first()
    if existusername:
        return jsonify({
            'success': False,
            'message': 'Username has been taken'
            }), 400
    user = User(username=username, email=email,password=password)
    user.insert()
    
    return jsonify({
        'success': True,
        'message': 'User created successfully!',
        'user':user.format()
        }), 201


@user.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({
            'success': False,
            'message': 'Invalid email or password'
            }), 401
    id=str(user.id)
    role = 'woche user'
    token = encode_auth_token(id,role)
    return jsonify({
        'success': True,
        'token': token.decode('UTF-8'),
        'user':user.format(),
        'message':'Log in Successfully'
        })

@user.route('/')
def index():
    return 'This is The user Blueprint'