from fastapi import APIRouter
from schemas.users import UsersSchema

router = APIRouter(prefix='/users')


@router.get("/info/{user_id}", tags=["users"],response_model=UsersSchema)
async def get_info_user_from_user_id(user_id: str):
    return 

