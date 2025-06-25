from repositories.examinations_repository import ExaminationsRepository
from schemas.examinations_schema import CreateExamination


class ExaminationsService:

    @staticmethod
    async def create_examination_for_user(examination:CreateExamination, db) -> CreateExamination:
        return await ExaminationsRepository.create_examination_for_user(examination=examination,db=db)