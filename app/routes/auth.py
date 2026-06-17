from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.models import User
from app.schemas.user import *
from app.dependencies import get_db
from app.core.security import *

router = APIRouter()

@router.post("/signup")
def signup(user:UserCreate,db:Session = Depends(get_db)):
    exist = db.query(User).filter(User.email == user.email).first()
    if exist:
        raise HTTPException(
            400,
            "Email already exists"
        )
    new_user = User(
        name = user.name,
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()

    return {
        "message":"User Created"
    }

@router.post("/login")
def login(user:UserLogin ,db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            400,
            "Invalid login"
        )
    if not verify_password(
        user.password,db_user.password
    ):
        raise HTTPException(
            400,
            "Invalid password"
        )
    token = create_token(
        {"user_id":db_user.id}
    )

    return {
        "access_token":token
    }


