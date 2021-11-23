import asyncio
import threading

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

from fastapi.openapi.docs import get_swagger_ui_html
import time


# 后台任务
async def write_log():
    print(threading.current_thread().getName())
    # 模拟再协程使用同步的阻塞的方式，会发现有的时候回阻塞整个线程的执行！！！！
    time.sleep(5)


# 后台任务
async def write_log_2():
    print(threading.current_thread().getName())
    # 这里需要使用的异步的模拟阻塞的方式，所以    time.sleep(5)的区别很明显
    await asyncio.sleep(5)


# 用户请求
@app.get("/syncio/task")
async def do_task():
    asyncio.create_task(write_log())
    return "你好，协程下的同步阻塞！"


# 用户请求
@app.get("/asyncio/task")
async def do_task():
    asyncio.create_task(write_log_2())
    return "你好，协程下的异步阻塞！"


# 定义路由，并且在方法中带上request: Request
@app.get("/request/msg")
def read_request(item_id: str, request: Request):
    scope = request.scope
    print(scope)
    client = request.client
    print(client)
    return get_swagger_ui_html()


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
