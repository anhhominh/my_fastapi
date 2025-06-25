import os
from pydantic import BaseModel

class Env(BaseModel):
    DATABASE_URL = os.getenv("DATABASE_URL",default="mongodb_dev://localhost:27017")
    DATABASE_TYPE = os.getenv("DATABASE_TYPE",default="mongodb")
    REDIS_NODE = os.getenv("REDIS_NODE",default="redis_node_1")
    REDIS_POST = os.getenv("REDIS_POST",default=6379)
    CELERY_URL = os.getenv("CELERY_URL", 'amqp://guest@localhost//')
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL",'postgresql://postgres:Bright#1270@localhost/fastapi')
