# 生成模拟数据


from faker import Faker

fake = Faker(locale="zh_CN")
movies = []
for i in range(5):
    movie = {
        "id": i + 1,
        "title": fake.text(),
        "daoyan": fake.name(),
        "zhuyan": [fake.name(), fake.name(), fake.name()],
        "leibie": fake.text(),
        "pingjia": fake.text(),
        "nianfen": fake.text(),
        "juzhao": fake.text()
    }
    movies.append(movie)


print(movies)

