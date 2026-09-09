from pydantic import Field,BaseModel,EmailStr


class UsersRegister(BaseModel):

    username:str = Field(description="User login")
    password:str = Field(description="User password")
    email:EmailStr = Field(description="User mail")
    role:str = Field(description="User role")
