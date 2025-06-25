from fastapi import APIRouter
from schemas.users_schema import UsersSchema
from services.users_service import UsersService

router = APIRouter(prefix='/v1/users')

@router.get("/info/{user_id}", tags=["users"],response_model=UsersSchema)
async def get_info_user_from_user_id(user_id: str):
    return await UsersService.get_user_info_from_user_id(user_id=user_id)