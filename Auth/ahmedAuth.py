import jwt


def encode():
    pass

def decode():
    pass

import jwt
from datetime import datetime, timedelta
from flask import jsonify, request

app = Flask(__name__)
SECRET_KEY = 'your-secret-key-here'


# Function to encode a JWT token
def encode_auth_token(user_id,key,role):
    if not user_id:
        raise ValueError('User Id is required.')
    if not key:
        raise ValueError('Woche Key is required.')
    if not role:
        raise ValueError('Role is required.')  
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
           'sub': {'user_id': user_id, 'key': key,'role':role}
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e

# Function to decode a JWT token
def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    
@app.route('/login', methods=['POST'])
def login():
    # Validate user credentials and get the user id
    user_id = '123'  # Example user id
    
    # Generate JWT token and return it to the client
    auth_token = encode_auth_token(user_id)
    return jsonify({'auth_token': auth_token.decode()})
    
@app.route('/protected', methods=['GET'])
def protected():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Authorization header is missing.'}), 401

    auth_header_parts = auth_header.split(' ')
    if len(auth_header_parts) != 2 or auth_header_parts[0] != 'Bearer':
        return jsonify({'error': 'Invalid Authorization header.'}), 401
    auth_token = auth_header.split(' ')[1]
    
    if auth_token:
        decode_data = decode_auth_token(auth_token)
        user_id = decode_data.user_id
        token_key = decode_data.key
        role = decode_data.role
        user_token=Keydecrypt(key,token_key)
        
        if isinstance(user_id, str):
            return jsonify({'error': user_id}), 401
        else:
            # User is authenticated and authorized to access the protected resource
            return jsonify({
                user_id:user_id,
                user_token:user_token,
                role:role
            })
    else:
        return jsonify({'error': 'Authorization token is missing.'}), 401



from functools import wraps
from flask import jsonify, request

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Authorization header is missing.'}), 401

        auth_token = auth_header.split(' ')[1]
        user_id = decode_auth_token(auth_token)

        if isinstance(user_id, str):
            return jsonify({'error': user_id}), 401

        return f(user_id, *args, **kwargs)

    return decorated


from cryptography.fernet import Fernet
import uuid

# Generate a key from a UUID
def generate_key(uuid_str):
    return Fernet.generate_key()

# Encrypt a message using a UUID as the key
def KeyEncrypt(uuid_str, message):
    key = generate_key(uuid_str)
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt an encrypted message using a UUID as the key
def Keydecrypt(uuid_str, encrypted_message):
    key = generate_key(uuid_str)
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

