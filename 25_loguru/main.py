import time
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query

from logger import logger, init_logging

app = FastAPI()

init_logging()


@app.get('/')
async def read_root(q: Optional[int] = Query(None)):
    logger.info('来了来了, q = {q}', q=q)
    logger.info('这是 / 接口：当前时间戳为：{times}', times=time.time())
    return {'Hello': 'World'}

# see https://gist.github.com/nkhitrov/a3e31cfcc1b19cba8e1b626276148c49
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=9000, reload=True, access_log=True)
