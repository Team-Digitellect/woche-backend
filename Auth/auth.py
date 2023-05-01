import jwt

from datetime import datetime, timedelta
from flask import jsonify, request,abort
from functools import wraps

SECRET_KEY = 'your-secret-key-here'


def check_token_header():
    auth_header = request.headers.get('Authorization',None)
    if not auth_header:
        return jsonify({'error': 'Authorization header is missing.'}), 401
    
    auth_header_parts = auth_header.split(' ')
    if len(auth_header_parts) != 2 or auth_header_parts[0] != 'Bearer':
        return jsonify({'error': 'Invalid Authorization header.'}), 401
    auth_token = auth_header.split(' ')[1]
    return auth_token
    

# Function to encode a JWT token
def encode_auth_token(user_id,role):
    if not user_id:
        raise ValueError('User Id is required.')
    if not role:
        raise ValueError('Role is required.')  
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
           'sub': {'user_id': user_id,'role':role}
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
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        abort(401)
    except jwt.InvalidTokenError:
        abort(401)
    except jwt.JWTClaimsError:
            abort(401)
    except Exception:
        abort(400)

def check_role(role, payload):
    if 'role' not in payload:
        abort(400)
    if role not in payload['role']:
        abort(403)
    return True
   
   
def get_identity():
    try:
        auth_token = check_token_header()
        payload = decode_auth_token(auth_token)
        user_id = payload['user_id']
        if user_id:
            return user_id
        else:
            return jsonify({'error': 'Invaid User'}), 400
    except:
        abort(403)
    
  
def protected(role = ''):
    def require_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_token = check_token_header()
            try:
                payload = decode_auth_token(auth_token)
            except:
                abort(403)
            check_role(role, payload)
            return f(*args, **kwargs)
        return decorated
    return require_auth
        
            
            

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

