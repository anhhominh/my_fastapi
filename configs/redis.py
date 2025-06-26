from redis import RedisCluster
from configs.envs import settings

def connect_redis():
    startup_nodes = [
        {"host": settings.REDIS_NODE, "port": settings.REDIS_POST},
    ]
    redis_cluster_client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    return redis_cluster_client

