from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def ping():
    return {"Hello": "world"}

@app.get("/read/", response_model=list[schemas.Stat])
def read(skip: int = 0, limit: int = 10, db: Session = Depends(getDb)):
    users = crud.getAll(db, skip=skip, limit=limit)
    return users

@app.post("/create/", response_model=schemas.Stat)
def create(stat: schemas.StatCreate, db: Session = Depends(getDb)):
    return crud.create(db=db, stat=stat)