from fastapi import *
from fastapi.security.oauth2 import *
from sqlalchemy import *
from sqlalchemy.orm import *
from .. import models
from .. import utils
from .. import oauth2
from ..database import *
from ..import schemas as sm
from ..schemas import *


router = APIRouter(tags=['Authentication']) # prefix
m = FastAPI()

###############################################################################################################

# authentication





# @m.post("/login")
@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    

    global token


    user = db.query(models.User).filter(models.User.username==user_credentials.username).first()


    


    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')


    token = oauth2.create_access_token(data={"user_id" : user.id})
    # access_token = oauth2.create_access_token(data={"user_id" : user.id})


    return {
        "token" : token,
        "type" : "bearer"
    }
