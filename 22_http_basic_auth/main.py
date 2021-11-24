import secrets

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "biezhi")
    correct_password = secrets.compare_digest(credentials.password, "hello#world")

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的账户或密码",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {
        'username': credentials.username
    }


@app.get("/users/me", summary="测试 Http Basic 认证")
# def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
def read_current_user(credentials=Depends(get_current_username)):
    return {"username": credentials['username']}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
