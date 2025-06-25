import datetime
from pydantic import BaseModel

class UsersSchema(BaseModel):
    user_id: str
    user_name: str
    bith_day: datetime
    email: str
    phone: str
