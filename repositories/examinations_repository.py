from schemas.examinations_schema import CreateExamination


class ExaminationsRepository:

    @staticmethod
    async def create_examination_for_user(examination:CreateExamination, db) -> CreateExamination:
        new_examination = CreateExamination(**examination.model_dump())
        db.add(new_examination)
        db.commit()
        db.refresh(new_examination)
        return new_examination