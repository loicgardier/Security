from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path, Query,HTTPException
from models.users_register import UsersRegister
from models.users_login import UsersLogin
from services.users_repository import UserRepository
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

from utils import jwt_utils


router = APIRouter(prefix="/auth",tags=['users'])



@router.post('/register/')
async def register(user:UsersRegister=Body(),repository=Depends(UserRepository)):
    return await repository.register_user(user)

@router.post('/login/')
async def login(user:OAuth2PasswordRequestForm=Depends(),repository=Depends(UserRepository)):
    return {'access_token': await repository.login_user(user)}

@router.get('/need_authentication/')
def need_authentication(token:dict=Depends(jwt_utils.verify_token)):
    print(token)

@router.get('/need_role_admin/')
def need_role_admin(token:dict=Depends(jwt_utils.RoleGuard(['admin']))):
    print(token)
