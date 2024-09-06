from sqlalchemy import Column, Integer, String, JSON, DateTime
from .database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    rubrics = Column(JSON)
    text = Column(String)
    created_date = Column(DateTime)
