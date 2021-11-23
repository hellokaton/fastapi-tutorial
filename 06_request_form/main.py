import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/", summary="登录")
async def login(username: str = Form(..., description="登录用户名"), password: str = Form(..., description="登录密码")):
    print('password:', password)
    return {"username": username}

# pip install python-multipart
# 表单数据的「媒体类型」编码一般为 application/x-www-form-urlencoded
# 但包含文件的表单编码为 multipart/form-data
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
