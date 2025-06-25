from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from configs.databases import Base

class Examination(Base):
    __tablename__ = "examinations"

    id = Column(Integer,primary_key=True,nullable=False)
    user_id = Column(String,nullable=False)
    examination_name = Column(String,nullable=False)
    examination_id = Column(String,nullable=False)
    score = Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))