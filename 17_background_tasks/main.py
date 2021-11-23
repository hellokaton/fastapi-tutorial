import random
import time

import uvicorn
from fastapi import BackgroundTasks, FastAPI, Depends

app = FastAPI()


def write_notification(email: str, message=""):
    print('开始给邮箱:', email, '发送邮件,', message)
    time.sleep(random.randint(1, 3))
    print('邮箱:', email, '发送邮件结束')


@app.post("/send-notification/{email}", summary="异步发送邮件通知")
async def bg_task_with_thread(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="欢迎欢迎━(*｀∀´*)ノ亻!")
    return {"message": "邮件已发送, 请查看您的邮箱."}


@app.post("/send-notification2/{email}", summary="异步发送邮件通知 - 基于依赖")
async def send_notification(send_email: str = Depends(bg_task_with_thread)):
    return send_email


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
