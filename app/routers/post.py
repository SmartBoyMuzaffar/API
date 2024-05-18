from fastapi import *
from requests import post
from sqlalchemy import *
from ..database import *
from .. import schemas as sm
from ..schemas import *
from ..utils import *
from sqlalchemy.orm import *
from .. import models
from .. import utils
from .. import oauth2
from typing import *





router = APIRouter(
    prefix="/post",
    tags=["Post"]
)
m = FastAPI()






###################################################################################################################
###################################################################################################################

@router.get("")
def root(db: Session=Depends(get_db), limit:int=0, skip:int=0, search: Optional[str]="", user_id: str=Depends(oauth2.get_current_user)):
    # c.execute("""
    # select * from user_db;
    # """)
    # posts = c.fetchall()
    

    # post = db.query(models.User).filter(models.User.username==search).all()
    print(user_id)

    user_info = db.query(models.User).filter(models.User.id == user_id).first()  # / all()
    # posts = db.query(models.User, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.User.id, isouter=True).group_by(models.User.id).filter(models.User.username.contains(search)).limit(limit).offset(skip).all()


    return {"user info": user_info}
    # return my_posts





@router.get("/token-m")
def _():
    return oauth2.oauth2_scheme









###################################################################################################################
###################################################################################################################

# @m.post("/body-post")
@router.post("/body-post")
def name(name: dict = Body(...)):
    return {"Salom " + name['username']}



###################################################################################################################



###################################################################################################################






# # @m.get("/")
# @router.get("/")
# def get_posts(db: Session = Depends(get_db)):
#     # c.execute("""

#     # select * from user_db

#     # """)

#     # posts = c.fetchall()

#     posts = db.query(models.User)

#     # db.add(posts)

#     return posts


##############################################################################################################


##############################################################################################################


# @m.post("/", status_code=status.HTTP_201_CREATED, response_model=sm.UserOut)
@router.post("", status_code=status.HTTP_201_CREATED)
def create_posts(post: sm.User, db: Session=Depends(get_db)):
    # c.execute("""
    # insert into user_db (firstname, lastname, email, username, password, id)
    # values (%s, %s, %s, %s,%s, %s) returning *
    # """, (post.firstname, post.lastname, post.email, post.username, post.password, post.id))

    # con.commit()

    # new_post = c.fetchone()

    # userinfo = models.User(firstname=post.firstname, lastname=post.lastname, email=post.email, username=post.username, password=post.password, id=post.id)
    
    #######################################
    #hash password
    hashed_pwd = utils.hash(post.password)
    post.password = hashed_pwd
    userinfo = models.User(**post.dict(), )

    db.add(userinfo)
    db.commit()
    db.refresh(userinfo)

    return userinfo

    # return {
    #     "username":f"{post.username}",
    #     "password":f"{post.password}",

    #     "time":f"{datetime.now()}"
    #     }

    # con.commit()




########################################################################################################

# @m.get("/{id}")
@router.get("/{id}")
def get_post(id: str, response: Response, db: Session = Depends(get_db)):
    # c.execute("""

    # select * from user_db where id=%s

    # """, (str(id),))

    post = db.query(models.User).filter(models.User.id == id).first()  # / all()

    

    # post = c.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id: {id} not found!")

    return post


################################################################################################################





# @m.delete("/{id}", response_model=List[sm.Post])
@router.delete("/{id}", response_model=List[sm.Post])
def delete_post(id: int, db: Session = Depends(get_db)):
    # c.execute("""

    # delete from user_db where id = %s returning *

    # """, (str(id),))

    # delete_post = c.fetchone()

    # con.commit()

    post = db.query(models.User).filter(models.User.id == id)

    if post.first() == None:  # is None

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id: {id} does not exist!")

        # my_posts.pop()

    post.delete(synchronize_session=False)

    db.commit()

    return "Succesfully deleted!"


#################################################################################################################


# @m.put("/{id}", response_model=List[sm.Post])
@router.put("/{id}", response_model=List[sm.Post])
def update_post(id: int, post: PostBase, db: Session = Depends(get_db)):

    update_post.update(**post.dict(), synchronize_session=False)

    db.commit()

    return update_post.first()


################################################################################################################


# @m.get('/user-db')
@router.get('/user-db')
def user_db(db: Session = Depends(get_db)):
    post = db.query(models.User).all()

    return post


################################################################################################################
################################################################################################################

