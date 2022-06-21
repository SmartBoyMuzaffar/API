from sqlalchemy import create_engine
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from psycopg2.extras import RealDictCursor
import psycopg2
import time
from .config import settings


##########################################################################################################################################################


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}"


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


while True:


    try:
        con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='smartboymuzaffar', cursor_factory=RealDictCursor)

        c = con.cursor()

        print("\nDatabase connected successully!\n")

        break

    except Exception as error:


        print("\nConnection database was failed!\n")
        # print("Error:", error)
        time.sleep(5)

#######################################################################################################################################################
