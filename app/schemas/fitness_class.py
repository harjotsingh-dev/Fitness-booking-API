from pydantic import BaseModel,ConfigDict
from datetime import datetime

class ClassCreate(BaseModel):
    name : str
    datetime : datetime
    instructor : str
    availableSlots : int

class ClassResponse(BaseModel):
    id : int
    name : str
    datetime : datetime
    instructor : str
    availableSlots : int

    model_config = ConfigDict(from_attributes=True)




