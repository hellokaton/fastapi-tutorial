from typing import Optional

import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()

fake_items_db = [{'item_name': '刘华强'}, {'item_name': '罗翔'}, {'item_name': '张三'}, {'item_name': '周星驰'}]


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title='The description of the item', max_length=300
    )
    price: float = Field(..., gt=0, description='The price must be greater than zero')
    tax: Optional[float] = None


@app.get('/items', summary='查询参数传参校验', description='将 Query 用作查询参数的默认值，并设置最小长度为2，最大长度为10.')
async def read_items(q: Optional[str] = Query(None, min_length=2, max_length=10)):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


@app.get('/users/{user_id}', summary='路径参数传参校验')
async def read_items(user_id: int = Path(..., gt=0, title='要获取的用户ID')):
    results = {'user_id': user_id}
    return results


@app.put('/items/{item_id}', summary='Body参数传校验')
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {'item_id': item_id, 'item': item}
    return results


@app.get('/mobile_items', summary='正则校验查询参数', description='将 Query 用作查询参数的默认值，并设置最小长度为2，最大长度为10.')
async def find_by_mobile(
        mobile: str = Query(None, regex='^1[3579]\\d{9}$', description='请输入手机号类型')
):
    results = {'mobile': mobile}
    return results


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
