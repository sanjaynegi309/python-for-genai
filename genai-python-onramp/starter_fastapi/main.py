from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PingResponse(BaseModel):
    message: str

@app.get("/ping", response_model=PingResponse)
def ping():
    return {"message": "pong"}
