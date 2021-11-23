import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


class TipException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(TipException)
async def unicorn_exception_handler(request: Request, exc: TipException):
    return JSONResponse(
        status_code=418,
        content={
            "code": -1,
            "message": f"emmm. {exc.name} 出现了亿点点问题..."
        },
    )


# 覆盖默认异常处理器
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "code": -1,
            "message": exc.errors()
        },
    )


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! 一个HTTP错误!: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! 客户端发送了非法数据!: {exc}")
    return await request_validation_exception_handler(request, exc)


@app.get("/items/{item_id}", summary="根据ID读取数据 404 异常")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="找不到该项", headers={"X-Error": "this is custom response header"})
    return {"item": items[item_id]}


@app.get("/unicorns/{name}", summary="自定义异常处理器")
async def read_unicorn(name: str):
    if name == "biezhi":
        raise TipException(name=name)
    return {"unicorn_name": name}


@app.get("/items2/{item_id}", summary="测试输入非数字导致进入自定义异常处理器")
async def read_item2(item_id: int):
    return {"item_id": item_id}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
