from fastapi import FastAPI, Query, Depends
from typing import Optional, Union
from datetime import date
from pydantic import BaseModel # For data validation, its like Request and Responce data validation in Laravel

from bookings.router import router as router_bookings
from users.router import router as router_users


app = FastAPI()


app.include_router(router_users)
app.include_router(router_bookings)


class HotelsSerachArgs:
   def __init__(
         self,
         location: str,  
         date_from: int, 
         date_to: int,
         has_spa: Optional[bool]=False,
         stars: Optional[int]=Query(None, ge=1, le=5)
      ):
      self.lacation = location
      self.date_to = date_to
      self.date_from = date_from
      self.has_spa = has_spa
      self.stars = stars


class SHotel(BaseModel): # Response validation
   address: str
   name: str
   stars: int


@app.get("/hotels") # Path params , response_model=list[SHotel]
def get_hotels(
    search_ars: HotelsSerachArgs = Depends()
   ): # return type -> list[SHotel]

   return search_ars




