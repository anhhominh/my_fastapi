import pymongo
from configs.envs import Env

def connect_mongodb():
    client = pymongo.MongoClient(Env.DATABASE_URL)
    return client

