
from configs.envs import settings
# config.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Add handlers etc. for logger

#---MongoDB----
from pymongo import MongoClient
#--- Khởi tạo db_client
db_client: MongoClient = None
def connect_mongodb():
    client = MongoClient(settings.DATABASE_URL)
    return client

#---Postgres---
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()