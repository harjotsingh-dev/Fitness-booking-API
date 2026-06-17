from fastapi import Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.models import User
from app.core.security import SECRET_KEY, ALGORITHUM




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str,
    db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHUM])
        user_id = data.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid Token")

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired Token")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user