from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base

class Stat(Base):
    __tablename__ = "stat"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, index=True)
    views = Column(Integer)
    clicks = Column(Integer)
    cost = Column(Float)
