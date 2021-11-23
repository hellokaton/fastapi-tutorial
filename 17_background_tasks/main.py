import uvicorn

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def tasks(msg):
    print('耗时任务开始执行', msg)
    import time
    time.sleep(5)
    print('耗时任务开始结束', msg)


@app.post("/bg_task_with_thread")
async def bg_task_with_thread(msg: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(tasks, msg)
    return "任务已经再处理中！"


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
