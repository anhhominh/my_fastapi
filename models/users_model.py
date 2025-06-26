import datetime
from pydantic import BaseModel

class UsersModel(BaseModel):
    user_id: str
    user_name: str
    bith_day: datetime.datetime
    email: str
    phone: str
