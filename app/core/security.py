from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHUM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password,hashed):
    return pwd_context.verify(password,hashed)

def create_token(data):
    data["exp"] = datetime.utcnow()+timedelta(hours=2)
    return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHUM)