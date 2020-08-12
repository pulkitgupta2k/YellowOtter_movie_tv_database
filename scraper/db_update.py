from func import *
from creds import username, password, ip, db_name, col_name
from pymongo import MongoClient


# global variables for connecting to mongo
client = MongoClient(f'mongodb://{username}:{password}@{ip}:27017/{db_name}?authSource=cool_db&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
collection = client[db_name][col_name]


def check_cast():
    data = ret_json("data/smol_data.json")
    for row in data:
        filter = {'id': row[0]}
        result = list(collection.find(filter=filter))

        if result:
            pprint(result)


def db_driver():
    clean_tsv()
    check_cast()

if __name__ == "__main__":
    db_driver()