from fastapi import FastAPI
from typing import Optional


app = FastAPI()
@app.post("/addrouter")

def addrouter():
    return {"hello"}