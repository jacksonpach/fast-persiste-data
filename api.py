from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import redis

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

    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('name', person.country)
    name = r.get('name')
    return name

#Persit data in redis

@app.post("/sub/")
async def sub():
    r = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = r.pubsub()
    pubsub.subscribe('channel-1')
    r.publish('channel-1', 'jackson')