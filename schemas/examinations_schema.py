from pydantic import BaseModel


class ExaminationBase(BaseModel):
    user_id: str
    examination_name: str
    examination_id: str
    score: int
    class Config:
        orm_mode = True


class CreateExamination(ExaminationBase):
    class Config:
        orm_mode = True