import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Request http://127.0.0.1:9000/static/picnic.min.css
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
