from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI


class Person(BaseModel):
    name: str
    phone: str
    email: str
    postal_zip: Union[str, None] = None
    region: str
    country: str
    text: str
    number_range: float
    currency: str
    alphanumeric: str = None


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/persons/")
async def create_item(person: Person):

    return person

#Persit data in redis
