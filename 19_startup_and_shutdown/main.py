import uvicorn
from fastapi import FastAPI

app = FastAPI()

items = {}


@app.on_event("startup")
async def startup_event():
    print('startup')
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    if items.__contains__(item_id):
        return items[item_id]
    return {}


@app.on_event("shutdown")
async def shutdown_event():
    print('shutdown...')


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
