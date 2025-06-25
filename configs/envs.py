import os
from pydantic import BaseModel

class Env(BaseModel):
    DATABASE_URL = os.environ.get("DATABASE_URL",default="mongodb_dev://localhost:27017")
    DATABASE_TYPE = os.environ.get("DATABASE_TYPE",default="mongodb")
    REDIS_NODE = os.environ.get("REDIS_NODE",default="redis_node_1")
    REDIS_POST = os.environ.get("REDIS_POST",default=6379)

