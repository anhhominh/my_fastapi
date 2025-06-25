from redis import RedisCluster
from configs.envs import Env

def connect_redis():
    startup_nodes = [
        {"host": Env.REDIS_NODE, "port": Env.REDIS_POST},
    ]
    redis_cluster_client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    return redis_cluster_client

