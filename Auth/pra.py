from cryptography.fernet import Fernet
import uuid

key= "ahmed"
uuid = "67sfbse82e8383483483483"
# Generate a key from a UUID
def generate_key(mykey):
    return Fernet.generate_key()

# Encrypt a message using a UUID as the key
def KeyEncrypt(mykey, myuuid):
    key = generate_key(mykey)
    f = Fernet(key)
    encrypted_message = f.encrypt(myuuid.encode())
    return encrypted_message

# Decrypt an encrypted message using a UUID as the key
def decrypt(mykey, token):
    key = generate_key(mykey)
    f = Fernet(key)
    decrypted_message = f.decrypt(token)
    return decrypted_message.decode()

token = KeyEncrypt(key,uuid)
print(token)
decrpy = decrypt(key,token)
print(decrpy)
