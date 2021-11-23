import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, StreamingResponse, RedirectResponse, FileResponse, \
    JSONResponse

app = FastAPI()


@app.get("/response_xml", summary="相应XML类型数据")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")


@app.get("/plain_text_response", summary="响应文本类型数据")
async def plain_text_response():
    return PlainTextResponse('我是文本数据')


@app.get("/plain_text_response2/", summary="响应文本类型数据2", response_class=PlainTextResponse)
async def plain_text_response2():
    return "我是文本数据22！"


@app.post("/json_response", summary="响应JSON数据")
async def json_response():
    return {"code": 0, "msg": "修改成功", "data": None}


@app.post("/json_response2", summary="响应JSON数据2")
async def json_response2():
    return JSONResponse(status_code=200, content={"message": "success"})


@app.get("/response_html", summary="响应HTML数据", response_class=HTMLResponse)
async def response_html():
    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/redirect_response", summary="重定向", response_class=HTMLResponse)
async def redirect_response():
    return RedirectResponse("https://wwww.baidu.com")


async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"


@app.get("/stream_response", summary="流式响应")
async def stream_response():
    return StreamingResponse(fake_video_streamer())


some_file_path = "large-video-file.mp4"


@app.get("/stream_response2", summary="流式响应2")
def stream_response2():
    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")


@app.get("/file_response", summary="文件响应")
def file_response():
    return FileResponse(some_file_path, media_type="video/mp4")


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
