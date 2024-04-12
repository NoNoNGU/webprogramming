from typing import Union

from fastapi import FastAPI

app = FastAPI()

name = 'dong hyun'

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/{item_id}")
def create(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}