import json

from fastapi import APIRouter

from config import ROOT

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

# TODO :增加单个电影
# @MOVIE.post("/add/")
# def add_movie():
# pass

if __name__ == '__main__':
    pass
