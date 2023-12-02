# 入口文件
from fastapi import FastAPI
import uvicorn

from apps.movies.urls import MOVIE

app = FastAPI()

app.include_router(MOVIE, prefix="/M", tags=["电影查询接口"])

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)
