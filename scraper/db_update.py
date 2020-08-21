from pymongo import MongoClient
from creds import *
from pprint import pprint

client = MongoClient(
    f'mongodb://{username}:{password}@{ip}:27017/{db_name}?authSource={db_name}&readPreference=primary&appname=MongoDB%20Compass&ssl=false')

python_dict = {
    "_id": "tt01",
    "episode": [],
    "name": "Test_data",
    "description": "This is a test data. Pls ignore. Thanks!",
    "genre": "Horror",
    "imdb_ratings": "6.9",
    "rt_rating": None,
    "age_rating": "TV-69",
    "cover_image": "https:test.jpg",
    "air_date": "2019-10-10",
    "trailer_link_1": "/video/imdb/vi273202969",
    "cast": [],
    "seasons": [],
    "title_type": "tvSeries",
    "provider_data": [],
    "trailer_link_0": "testetst"
}

filter = {
    '_id': 'tt01'
}

client[db_name][col_name].insert_one(python_dict)
result = client[db_name][col_name].find(filter=filter)


print(list(result))
