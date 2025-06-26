from commons.exp_cache import EXP_CACHE
from configs.redis import connect_redis
from configs.databases import logger,db_client
from models.users_model import UsersModel

class UsersRepository:
    @staticmethod
    async def get_user_info_cache(user_id: str):
        try:
            rc = connect_redis()
            info = rc.get(f"info_{user_id}")
            rc.close()
            return info
        except Exception as e:
            logger.error(f"Có lỗi: {e}")

    @staticmethod
    async def set_user_info_cache(user_id:str,info:dict):
        try:
            rc = connect_redis()
            rc.set(user_id, info, ex=EXP_CACHE)
            rc.close()
        except Exception as e:
            logger.error(f"Có lỗi {e}")

    @staticmethod
    async def get_user_info_from_user_id(user_id:str) -> UsersModel:
        try:
            info_cache = UsersRepository.get_user_info_cache(user_id=user_id)
            if info_cache:
                return UsersModel(**info_cache)
            db = db_client["mydatabase"]
            my_collection = db["mycollection"]
            user_info = my_collection.find_one({"user_id":user_id})
            UsersRepository.set_user_info_cache(user_id=user_id,info=user_info)
            return UsersModel(**user_info)
        except Exception as e:
            logger.error(f"Có lỗi: {e}")