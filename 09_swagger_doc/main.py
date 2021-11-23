import uvicorn
from fastapi import FastAPI

app = FastAPI(version="v1.0.5", title="Hello World OpenAPI", description="这是对 hello world openapi 的描述信息.")


# 隐藏这个接口在Api文档中不在显现
@app.get("/swag01", include_in_schema=False)
def swag01():
    return "success"


# 这个接口在Api文档中 标记为已经无法使用，相当于过期，不建议再使用
@app.get("/swag02", deprecated=True)
async def swag02():
    return "success"


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
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
