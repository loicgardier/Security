from dtos.users import Users as UsersDto
from models.users_register import UsersRegister
from models.users_login import UsersLogin
from utils import password_utils
from utils import jwt_utils

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

from fastapi.exceptions import HTTPException 

class UserRepository:
    def __init__(self):
        config = dotenv_values(".env") 
        engine=create_engine(config.get("DATABASE_CONNECTION_STRING"))
        self.session_local = sessionmaker(autoflush=False,bind=engine)

    async def register_user(self,user:UsersRegister):
        userdb= UsersDto()
        userdb.username=user.username
        userdb.password = password_utils.hash(user.password)
        userdb.email = user.email
        userdb.role = user.role
        with self.session_local() as session:
            session.add(userdb)
            session.commit()
            session.refresh(userdb)
            return userdb

    async def login_user(self,user:UsersLogin):
        with self.session_local() as session:
            userdb = session.query(UsersDto).where(UsersDto.username==user.username).first()
            print(userdb.password,password_utils.hash(user.password))
            if(password_utils.verify(user.password,userdb.password)):
                return jwt_utils.create_token(userdb.id,userdb.role)
            else:
                raise HTTPException(401,'Unauthorized')