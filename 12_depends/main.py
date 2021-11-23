from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, Query, HTTPException, Header, Request


# 全局依赖项
async def request_log(request: Request):
    print('请求路径:', request.url)
    print('请求方法:', request.method)


app = FastAPI(dependencies=[Depends(request_log)])


async def common_parameters(q: str = Query(None, description="查询关键词"),
                            page: int = Query(1, description="请求页码", gt=0),
                            limit: int = Query(10, description="每页条数")):
    return {"q": q, "page": page, "limit": limit}


@app.get("/read_items")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/read_users")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/depends_by_class", summary="类级别的子依赖")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    """
    :param commons: 可以简写为  commons: CommonQueryParams = Depends()
    :return:
    """
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/users_depends", summary="路径依赖项", dependencies=[Depends(verify_token), Depends(verify_key)])
async def users():
    return [{"username": "张三"}, {"username": "罗翔"}]


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
