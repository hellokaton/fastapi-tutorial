from typing import Optional

import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [{'item_name': '刘华强'}, {'item_name': '罗翔'}, {'item_name': '张三'}, {'item_name': '周星驰'}]


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get('/items', summary='查询参数传参', description='该示例中查询参数为 skip和limit，并提供了默认值.')
async def read_item_by_query(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}', summary='路径参数传参', description='该示例中查询参数为item_id，并指定传入类型为int.')
async def read_item_by_path(item_id: int):
    return {'item_id': item_id}


@app.post('/items', summary='请求Body传参')
async def create_item(item: Item):
    return item


@app.post('/get_request_body', summary='获取请求Body')
async def get_request_body(request: Request):
    return request.body()


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
