# 生成模拟数据
import json

from faker import Faker

from config import ROOT

fake = Faker(["zh_CN", "en_US"])
movies = []
for i in range(3):
    movie = {
        "m_id": i + 1,
        "m_title": fake.word(ext_word_list=None),
        "m_director": fake.name(),  # 导演
        "m_scriptwriter": fake.name(),  # 编剧
        "m_actors": [fake.name(), fake.name(), fake.name()],  # 主演
        "m_genre": fake.word(ext_word_list=None),  # 题材
        "m_introduction": fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),  # 简介
        "m_language": fake.word(ext_word_list=None),  # 语言
        "m_area": fake.country(),  # 制片国家 / 地区
        "m_releaseDate": fake.date(),  # 上映日期
        "m_footage": fake.word(ext_word_list=None)  # 影片时长
    }
    movies.append(movie)

with open(ROOT + "/database/movies.json", mode="w") as f:
    json.dump(movies, f, ensure_ascii=False)

f.close()

# 导演: 弗兰克·德拉邦特
# 编剧: 弗兰克·德拉邦特 / 斯蒂芬·金
# 主演: 蒂姆·罗宾斯 / 摩根·弗里曼 / 鲍勃·冈顿 / 威廉姆·赛德勒 / 克兰西·布朗 / 更多...
# 类型: 剧情 / 犯罪
# 制片国家 / 地区: 美国
# 语言: 英语
# 上映日期: 1994 - 0
# 9 - 10(多伦多电影节) / 1994 - 10 - 14(美国)
# 片长: 142
# 分钟
# 又名: 月黑高飞(港) / 刺激1995(台) / 地狱诺言 / 铁窗岁月 / 消香克的救赎
