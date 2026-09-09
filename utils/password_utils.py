import os
from dotenv import load_dotenv
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib import PasswordHash
 

load_dotenv()

def get_pepper():
    pepper= os.getenv('APPLICATION_PEPPER',None)
    if not pepper:
        pass
    return pepper


password_hasher = Argon2Hasher(
    memory_cost=65536,
    parallelism=4,
    time_cost=6
)

password_context = PasswordHash([password_hasher])

def hash(plain_password):
    pepper=get_pepper()
    return password_context.hash(plain_password+pepper)

def verify(plain_password,hash):
    pepper=get_pepper()
    return password_context.verify(plain_password+pepper,hash)
