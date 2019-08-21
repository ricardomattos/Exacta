from sqlalchemy import (Column, Integer, Text, DateTime)
from .meta import Base


class Session(Base):
    __tablename__ = 'sessions'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text)
    page = Column(Text)
    date = Column(DateTime)
