from fastapi import APIRouter, FastAPI
from fastapi import *
from ..database import *
from .. import schemas as sm
from ..schemas import *
from ..utils import *
from typing import List
from .. import models
from .. import utils
from sqlalchemy.orm import *


router = APIRouter(
    prefix="/user",
    tags=["User"]
)
m = FastAPI()


################################################################################################################



# @m.post("/", status_code=status.HTTP_201_CREATED, response_model=sm.UserOut)
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_posts(post: PostBase, db: Session = Depends(get_db)):
    # c.execute("""
    # insert into user_db (firstname, lastname, email, username, password, id)
    # values (%s, %s, %s, %s,%s, %s) returning *
    # """, (post.firstname, post.lastname, post.email, post.username, post.password, post.id))

    # con.commit()

    # new_post = c.fetchone()

    # userinfo = models.User(firstname=post.firstname, lastname=post.lastname, email=post.email, username=post.username, password=post.password, id=post.id)
    hashed_pwd = utils.hash(post.password)
    post.password = hashed_pwd
    postinfo = models.User(**post.dict(), )

    db.add(postinfo)
    db.commit()
    db.refresh(postinfo)

    return postinfo

    # return {
    #     "username":f"{post.username}",
    #     "password":f"{post.password}",

    #     "time":f"{datetime.now()}"
    #     }

    con.commit()



# @m.get('/{id}')
# @router.get('/{id}', response_model=List[sm.User])
@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    # user = db.execute(f"""
    # select * from user_db where id={id}
    # """).first()
    user = db.query(models.User).filter(models.User.id == id).first()  # / all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    # return userS
    return user


#################################################################################################################
#################################################################################################################

