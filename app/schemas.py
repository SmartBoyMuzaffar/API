from typing import Optional, List
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime

from .database import Base
from .models import trans_

time_ = datetime.now()



    
class PostBase(BaseModel):

    ##############
    firstname: str
    lastname: str
    email: EmailStr
    username: str
    password: str
    id: int

    class Config:
        orm_mode = True





class Post(PostBase):

    ##############
    id: int

    created_at: datetime

    class Config:
        orm_mode = True



class User(BaseModel):

    firstname: str
    lastname: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    # firstname: str
    # lastname: str
    email: EmailStr
    # username: str
    password: str

class trans_(BaseModel):
    entred: str
    translated: str

class UserOut(BaseModel):
    Data: User
    time: str=time_

    class Config:
        orm_mode = True



class UserLogin(BaseModel):

    username: str
    password: str





class Token(BaseModel):

    access_token: str
    token_type: str


class TokenData:

    id: Optional[str]=None





class CreatePost(BaseModel):
    email: EmailStr
    password: str
    id: int





class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)






# class model(BaseModel):
#     email: EmailStr
#     id: int

#     class Config:
#         orm_mode = True


