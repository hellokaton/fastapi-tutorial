import aioredis
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    """ 获取链接 :return: """
    app.state.redis = await aioredis.from_url("redis://localhost")


@app.on_event('shutdown')
async def shutdown_event():
    """ 关闭 :return: """
    app.state.redis.close()
    await app.state.redis.wait_closed()


@app.get("/", summary="读取 redis 数据")
async def read_value(request: Request, key: str):
    v = await request.app.state.redis.get(key)
    return v


@app.post("/", summary="写入 redis 数据")
async def read_value(request: Request, key: str, value: str):
    request.app.state.redis.set(key, value)
    return {"msg": "success"}


# pip intsall aioredis
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
