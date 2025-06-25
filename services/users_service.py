from models.users_model import UsersModel
from repositories.users_repository import UsersRepository


class UsersService:
    @staticmethod
    async def get_user_info_from_user_id(user_id:str) -> UsersModel:
        return await UsersRepository.get_user_info_from_user_id(user_id=user_id)