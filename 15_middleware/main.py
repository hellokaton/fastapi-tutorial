import time
from random import randint

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    # 等待请求执行结果
    response = await call_next(request)

    # 计算请求耗时
    process_time = round(time.time() - start_time, 1)
    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.get('/')
async def read_root():
    time.sleep(randint(0, 2))
    return {'Hello': 'World'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
