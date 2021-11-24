from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from response_json import to_json, to_json_tip

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get('/', summary="数据为 dict")
async def read_root():
    return to_json({'hello': 'world'})


@app.get('/text', summary="数据为 text")
async def text():
    return to_json('Hello World')


@app.get('/list', summary="数据为自定义 list")
async def query_list():
    item1 = Item(id=1, name='jack', price=128)
    return to_json([item1])


@app.get('/tips', summary="数据为提示消息")
async def tips():
    return to_json_tip('账号不存在')


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=9000, reload=True)
