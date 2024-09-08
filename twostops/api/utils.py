from fastapi import APIRouter
from fastapi import Form
from typing import Annotated

router = APIRouter(tags=["Utils"])

@router.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@router.post("/health")
async def health_check(msg:Annotated[str, Form(...)]):
    return {"message": msg}