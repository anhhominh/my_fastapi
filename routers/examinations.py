from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from configs.databases import get_db
from schemas.examinations_schema import CreateExamination
from services.examinations_service import ExaminationsService

router = APIRouter(prefix='/v1/examinations')

@router.post("/examination_for_user", tags=["examinations"],response_model=CreateExamination)
async def create_examination_for_user(examination:CreateExamination, db:Session = Depends(get_db)):
    return ExaminationsService.create_examination_for_user(examination=examination,db=db)