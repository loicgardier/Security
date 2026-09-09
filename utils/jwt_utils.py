import os
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import exceptions
from dotenv import load_dotenv
from datetime import datetime,timedelta
load_dotenv()

key = os.getenv('JWT_SECRET')

def create_token(id:str,role:str)->str:
    today=datetime.now()
    return jwt.encode({
        'iss':'Loïc',
        'iat':today.timestamp(),
        'exp': (timedelta(minutes=15) + today).timestamp(),
        'role':role,
        'sub':str(id)
    },key=key,algorithm='HS256')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login/')


def verify_token(token:Annotated[str,Depends(oauth2_scheme)]):
    try:
        print(token)
        return jwt.decode(token,key=key,algorithms=['HS256'])
    except exceptions.DecodeError as e:
        raise ValueError(e)

class RoleGuard:
    def __init__(self,roles:list[str]):
        self.authorize_role = roles

    def __call__(self, claims:Annotated[dict,Depends(verify_token)]):
        if not claims or claims['role'] not in self.authorize_role:
            raise HTTPException(403)
        return claims