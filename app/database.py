from sqlalchemy import create_engine
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
# from psycopg2.extras import RealDictCursor
# import psycopg2
# import time
# from .config import settings



##########################################################################################################################################################


# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.db"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}"
SQLALCHEMY_DATABASE_URL = "postgresql://avnadmin:AVNS_QHbuDuXH6nTNUi9IvFo@postgres-smartboy.h.aivencloud.com:26207/api?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()






def get_db():

    db = SessionLocal()

    try:

        yield db


    finally:

        db.close()

##########################################################################################################################################################
##########################################################################################################################################################

# while True:
#
#     try:
#         conn = psycopg2.connect(host='localhost', port='5432', database='postgres', user='postgres',
#                                 password='postgres', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
#
#######################################################################################################################################################
