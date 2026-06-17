from pydantic import BaseModel

class BookingCreate(BaseModel):
   class_id : int
   client_name : str
   client_email : str
