from pydantic import Field,BaseModel,EmailStr

class UsersLogin(BaseModel):

    username:str = Field(description="User login")
    password:str = Field(description="User password")