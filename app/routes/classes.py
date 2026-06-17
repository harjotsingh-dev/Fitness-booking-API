from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.models import FitnessClass 
from app.schemas.fitness_class import *
from app.dependencies import get_db,get_current_user
from app.core.security import *

router = APIRouter()

@router.post("/classes", response_model= ClassResponse)
def classes(data:ClassCreate, db:Session= Depends(get_db),user= Depends(get_current_user)):
    new  =FitnessClass(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/classes")
def get_classes(db:Session= Depends(get_db)):
   
    return db.query(FitnessClass).all()