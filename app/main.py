# from fastapi import *
# from psycopg2 import *
# from psycopg2.sql import *
# from database import Base, SessionLocal, get_db, engine
# from sqlalchemy.orm import Session
# from sqlalchemy.orm import *
# import models
# from django.template import Origin
# from routers.post import *
# from routers.user import *
# from muzaffar.auth import *
from .routers import post, user, vote
from .muzaffar import auth, translate_
from .muzaffar.translate_ import *
from .database import *
from typing import *
from fastapi.middleware.cors import CORSMiddleware



##############################################################################################################







models.Base.metadata.create_all(bind=engine)



router = APIRouter()
m = FastAPI()




origins = ["*"]

m.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




#######################################################################################################################################################

m.include_router(post.router) 
m.include_router(user.router)
m.include_router(auth.router)
m.include_router(translate_.router)
m.include_router(vote.router)

#######################################################################################################################################################



@m.get('/', response_model=List[sm.User])
def root(db: Session=Depends(get_db)):
    # c.execute("""
    # select * from user_db;
    # """)
    # posts = c.fetchall()

    data = db.query(models.User).all() # select * from user_db;


    return data
    # return my_posts






################################################################################################################
################################################################################################################

########################################################################################################
########################################################################################################








# driver function
if __name__ == '__main__':

    m.run(debug = True)
