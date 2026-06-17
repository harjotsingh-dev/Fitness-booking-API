from fastapi import FastAPI
from app.db.database import Base,engine
from app.db import models
from app.routes import auth,classes,booking


Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Fitness Booking API")

app.include_router(auth.router)
app.include_router(classes.router)
app.include_router(booking.router)

@app.get("/")
def home():
    return {"message": "Api running"}