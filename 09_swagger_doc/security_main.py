import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI(
    version="v1.0.5", title="Hello World OpenAPI", description="这是对 hello world openapi 的描述信息.",
    # 自定义开启的API文档的接口的时候，需要设置默认的关闭
    docs_url=None
)

security = HTTPBasic()


@app.get("/docs", include_in_schema=False)
async def get_documentation(credentials: HTTPBasicCredentials = Depends(security)):
    print("get_documentation")
    if credentials.username != "biezhi" or credentials.password != "123456":
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="用户或密码错误",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return get_swagger_ui_html(openapi_url="/openapi.json", title="doc")


@app.get(path='/api/v1/get/user', summary='获取用户', description='这个接口是用来添加用户的', tags=['用户模块'])
def getuser():
    return {"code": 0, "msg": "获取成功", "data": None}


@app.post(path='/api/v1/add/user', summary='添加用户', description='这个接口是用来获取用户信息的', tags=['用户模块'])
def adduser():
    return {"code": 0, "msg": "添加成功", "data": None}


@app.put(path='/api/v1/updata/user', summary='更新用户', description='这个接口是用来更新用户信息的', tags=['用户模块'])
def updatauser():
    return {"code": 0, "msg": "修改成功", "data": None}


@app.put(path='/api/v1/delete/user', summary='删除用户', description='这个接口是用来删除用户信息的', tags=['用户模块'])
def deleteuser():
    return {"code": 0, "msg": "删除成功", "data": None}


@app.put(path='/api/v1/add/data', summary='新增数据', description='这个接口是用来新增数据', tags=['数据模块'])
def adddatas():
    return {"code": 0, "msg": "删除成功", "data": None}


if __name__ == '__main__':
    uvicorn.run('security_main:app', host='127.0.0.1', reload=True, port=9000)
