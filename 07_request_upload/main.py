import os
import uuid
from typing import List

import aiofiles
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload1/", summary="小文件上传")
async def upload1(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/upload2/", summary="更常用的文件上传")
async def upload2(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type}


@app.post("/upload3/", summary="上传多个文件")
async def upload3(files: List[UploadFile] = File(...)):
    return {"size": len(files), "filenames": [file.filename for file in files]}


@app.post("/upload4/", summary="异步储存文件到磁盘")
async def upload4(in_file: UploadFile = File(...)):
    _, file_extension = os.path.splitext(in_file.filename)
    out_file_path = f'{uuid.uuid4().hex}{file_extension}'
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        while content := await in_file.read(1024):  # async read chunk
            await out_file.write(content)           # async write chunk
    return {"Result": "OK"}

# pip install aiofiles
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
