import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/hello/{req_id}", response_class=HTMLResponse)
async def read_item(request: Request, req_id: str):
    return templates.TemplateResponse("hello.html", {"request": request, "req_id": req_id})


# pip install jinja2
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
