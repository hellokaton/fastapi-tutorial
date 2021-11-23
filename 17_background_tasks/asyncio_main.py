import asyncio
import logging
import threading
import time

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%d-%m %H:%M:%S')


async def write_log():
    logging.info(threading.current_thread().getName() + " 开始执行")
    # 模拟再协程使用同步的阻塞的方式，会发现有的时候回阻塞整个线程的执行！！！！
    time.sleep(3)
    logging.info(threading.current_thread().getName() + " 结束执行")


async def write_log_2():
    logging.info(threading.current_thread().getName() + " 开始执行")
    # 这里需要使用的异步的模拟阻塞的方式，所以time.sleep(3)的区别很明显
    await asyncio.sleep(3)
    logging.info(threading.current_thread().getName() + " 结束执行")


@app.get("/syncio/task", summary="协程下的同步阻塞")
async def do_task():
    asyncio.create_task(write_log())
    return "你好，协程下的同步阻塞！"


@app.get("/asyncio/task", summary="协程下的异步阻塞")
async def do_task():
    asyncio.create_task(write_log_2())
    return "你好，协程下的异步阻塞！"


# 定义路由，并且在方法中带上request: Request
@app.get("/request/msg")
def read_request(item_id: str, request: Request):
    scope = request.scope
    logging.info(scope)
    client = request.client
    logging.info(client)
    return {
        'item_id': item_id,
        'client': str(client.host) + ':' + str(client.port)
    }


if __name__ == '__main__':
    uvicorn.run('asyncio_main:app', host='127.0.0.1', reload=True, port=9000)
