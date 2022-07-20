from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class StatBase(BaseModel):
    date: datetime
    views: int | None = None
    clicks: int | None = None
    cost: float | None = None

class StatCreate(StatBase):
    pass

class Stat(StatBase):
    id: int

    class Config:
        orm_mode = True