from sqlalchemy.orm import Session

from . import models, schemas

def getAll(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stat).offset(skip).limit(limit).all()

def create(db: Session, stat: schemas.StatCreate):
    dbStat = models.Stat(
        date = stat.date,
        views = stat.views,
        clicks = stat.clicks,
        cost = stat.cost
    )
    db.delete(dbStat)
    db.commit()
    db.refresh(dbStat)
    return dbStat