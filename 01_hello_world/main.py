from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    item.id = item_id
    return item


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=9000, reload=True)
