# from aiohttp import Payload
from jose import JWTError, jwt
from fastapi import *
from fastapi.security import *
from datetime import datetime, timedelta
from passlib.context  import *
from . import schemas as sm
from .config import settings







oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')





SECRET_KEY = f"{settings.secret_key}"
ALGORITHM = f"{settings.algorithm}"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")


        if id is None:

            raise credentials_exception

        


    except JWTError:
        raise credentials_exception

    return id



def get_current_user(token: str=Depends(oauth2_scheme)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials', headers={"WWW-Authenticate":"Bearer"})


    return verify_access_token(token, credentials_exception)




