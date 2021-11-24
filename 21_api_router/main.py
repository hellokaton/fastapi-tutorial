import uvicorn
from fastapi import FastAPI

from routers import api_router

app = FastAPI()

# 注册路由
app.include_router(api_router, prefix="/ch01", tags=["第一章节"])

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
