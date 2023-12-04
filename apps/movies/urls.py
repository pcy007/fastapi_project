import json

from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel

from config import ROOT


class Movie(BaseModel):
    m_id: int
    m_title: str  # 电影名字
    m_director: str | None = None  # 导演
    m_scriptwriter: str | None = None  # 编剧
    m_actors: list[str] | None  # 主演
    m_genre: str | None = "剧情片"  # 题材
    m_introduction: str | None = None  # 简介
    m_language: str = "中文"  # 语言
    m_area: str = "中国"  # 制片国家 / 地区
    m_releaseDate: str | None = None  # 上映日期
    m_footage: str | None = "120分钟"  # 影片时长


MOVIE = APIRouter()


# 查询所有电影
@MOVIE.get("/movies")
def show_movies():
    with open(ROOT + '\\database\\movies.json', mode="r") as f:
        resp_movies = json.load(f)
    f.close()

    return resp_movies


# 查询单个电影
@MOVIE.get("/movie/{m_title}")
def search_movies(m_title: str):
    with open(ROOT + '\\database\\movies.json', mode="r") as f:
        movies = json.load(f)
    f.close()

    for i in movies:
        if m_title in i["m_title"]:
            return i

    return {"result": f"{m_title}不存在"}


# 增加单个电影
@MOVIE.post("/add/")
def add_movie(m: Movie):
    m_json = m.model_dump()

    with open(ROOT + '\\database\\movies.json', mode="r") as f:
        movies = json.load(f)
    f.close()

    for i in movies:
        if m_json["m_id"] == i["m_id"]:
            return {"result": f"id为{m_json['m_id']}已经存在"}

    movies.append(m_json)
    with open(ROOT + '\\database\\movies.json', mode="w") as f:
        json.dump(movies, f, ensure_ascii=False)
    f.close()

    return {"result": "电影添加成功"}


# 删除单个电影
@MOVIE.get("/delete/{m_id}")
def delete_movie(m_id: int):
    with open(ROOT + '\\database\\movies.json', mode="r") as f:
        movies = json.load(f)
    f.close()

    for i in movies:
        if m_id == i["m_id"]:
            movies.remove(i)
            with open(ROOT + '\\database\\movies.json', mode="w") as f:
                json.dump(movies, f, ensure_ascii=False)
            f.close()
            return {"result": "电影删除成功"}

    return {"result": f"id为{m_id}的电影不存在"}


# 更新单个电影信息
@MOVIE.put("/update/{m_id}")
def update_movie(m_id: int, m_scriptwriter: str):
    with open(ROOT + '\\database\\movies.json', mode="r") as f:
        movies = json.load(f)
    f.close()

    for i in movies:
        if m_id == i["m_id"]:
            i["m_scriptwriter"] = m_scriptwriter
            with open(ROOT + '\\database\\movies.json', mode="w") as f:
                json.dump(movies, f, ensure_ascii=False)
            f.close()
            return {"result": "电影更新成功"}

    return {"result": f"id为{m_id}的电影不存在"}


# 为查询参数添加校验Query,为路径参数添加校验Path,为请求体参数添加校验Body
@MOVIE.put("/movies/query/{m_id}")
def query_movie(m_id: int = Path(title="m_id必须大于等于1", ge=1),
                q: str | None = Query(default="title", title="校验", description="--为查询参数添加校验--", min_length=1,
                                      max_length=20), mov: Movie | None = Body(title="这是请求题")):
    result = {
        "m_id": m_id,
        "q": q,
        "mov": mov
    }
    return result


if __name__ == '__main__':
    pass
