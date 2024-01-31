from fastapi import FastAPI, Request, Depends
#from app.api_models import LibraryAccess,LibraryResponse
from pydantic import BaseModel, Field
from typing import Optional
#from utils.utils import get_user
import uuid
import random

class LibraryLoan(BaseModel):
    id: int
    books: int

class LibraryResponse(BaseModel):
    message: Optional[str] = Field(None, description="Optional message to be displayed")
    reconfirm: bool
    uuid: str


app = FastAPI()

loans=[]

#Get all 
@app.get("/library/")
async def get_loans(LibraryLoan: LibraryLoan):
    return {"loans":loans}


