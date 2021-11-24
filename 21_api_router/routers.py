from fastapi import APIRouter
from pydantic import BaseModel

api_router = APIRouter()


class User(BaseModel):
    name: str
    age: int


@api_router.get('/', summary="Hello World")
async def read_root():
    return {'Hello': 'World'}


@api_router.post('/users', summary="保存User")
async def save_user(user: User):
    return user
