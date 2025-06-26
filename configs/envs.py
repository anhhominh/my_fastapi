import os
from pydantic import BaseModel

class Env(BaseModel):
    DATABASE_URL : str = os.getenv("DATABASE_URL",default="mongodb://localhost:27017")
    DATABASE_TYPE : str = os.getenv("DATABASE_TYPE",default="mongodb")
    REDIS_NODE : str = os.getenv("REDIS_NODE",default="redis_node_1")
    REDIS_POST : str = os.getenv("REDIS_POST",default=6379)
    CELERY_URL : str = os.getenv("CELERY_URL", default='amqp://guest@localhost//')
    SQLALCHEMY_DATABASE_URL : str = os.getenv("SQLALCHEMY_DATABASE_URL",default='postgresql://postgres:Bright#1270@localhost/fastapi')

# Create an instance of the Env class
settings = Env()

