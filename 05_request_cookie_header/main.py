from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Header, Cookie

app = FastAPI()


@app.get("/read_header", summary="获取 header 参数")
async def read_header(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}


@app.get("/header_list", summary="重复的 header")
async def header_list(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}


@app.get("/read_cookie", summary="获取 cookie 参数")
async def read_cookie(cc_id: Optional[str] = Cookie(None)):
    return {"cc_id": cc_id}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
