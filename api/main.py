import sys
from fastapi import FastAPI

# from pydantic import BaseModel
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste")
def read_teste():
    return {"not": "World"}