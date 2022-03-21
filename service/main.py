from fastapi import FastAPI
import models
from database import engine

# create app for start api
app = FastAPI()

# create database on database platform
models.Base.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello():
    return {"msg": "Hello"}
