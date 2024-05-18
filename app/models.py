from .database import *
from sqlalchemy import *


class User(Base):

    __tablename__ = "user_db"

    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)

    ######################################################

    # trans_dbm = relationship("trans_")




class trans_(Base):

    __tablename__ = "trans_db"

    id = Column(Integer, primary_key=True, nullable=False)
    entered = Column(String, nullable=False)
    translated = Column(String, nullable=False)



class Vote(Base):
    __tablename__ = "votes_db"
    user_id = Column(Integer, ForeignKey("user_db.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("trans_db.id", ondelete="CASCADE"), primary_key=True)

