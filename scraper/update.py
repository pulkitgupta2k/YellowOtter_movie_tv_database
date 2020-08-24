# import pymongo
from func import *
from creds import *
from pymongo import MongoClient
from pprint import pprint
UPLOAD_LIMIT = 1000

def get_imdb_ids(tsv_file, output_file):
    data = ret_tsv(tsv_file)
    ids = []
    for row in data:
        if row[1] != 'tvEpisode':
            ids.append([row[0], row[1]])
    write_json(ids,output_file)

def get_left(new_ids, prev_ids, output_file):
    new_data = ret_json(new_ids)
    prev_data = set(ret_json(prev_ids))

    output_data = []

    for row in new_data:
        if row[0] not in prev_data:
            output_data.append(row)

    write_json(output_data, output_file)

def today_ids():
    down_tsv("https://datasets.imdbws.com/title.basics.tsv.gz", "data/downloads/data")
    get_imdb_ids("data/downloads/data.tsv", "data/imdb_id.json")
    get_left("data/imdb_id.json", "data/title_id.json", "data/today_id.json")

def join_ids(prev_file, new_file):
    prev_data = ret_json(prev_file)
    new_data = ret_json(new_file)

    for key, value in new_data.items():
        prev_data.append(key)
    write_json(prev_data, prev_file)

def get_ep_ids(tsv_file, output_file):
    data = ret_tsv(tsv_file)
    write_json(data,output_file)  

def episode_ids():
    down_tsv("https://datasets.imdbws.com/title.episode.tsv.gz", "data/downloads/episode")
    get_ep_ids("data/downloads/episode.tsv", "data/new_ids/episode_id.json")
    get_left("data/new_ids/episode_id.json", "data/prev_ids/ep_id.json", "data/new_ids/today_ep_id.json")

def clean_episode(new_ids, prev_ids):
    new_data = ret_json(new_ids)
    prev_data = set(ret_json(prev_ids))

    ret_data = []

    for row in new_data:
        if row[1] in prev_data:
            ret_data.append(row)
    
    write_json(ret_data, new_ids)

def add_ep_to_mep(episode, master_ep):
    ep_data =ret_json(episode)
    mep_data = ret_json(master_ep)
    for key, value in ep_data.items():
        if "episode" in mep_data[value["series_id"]].keys():
            mep_data[value["series_id"]]["episode"].append(key)
        else:
            mep_data[value["series_id"]]["episode"] = [key]
    write_json(mep_data, master_ep)


# Database Functions
def conv_data(file):
    ret_list = []
    data = ret_json(file)

    for key, value in data.items():
        id = {"_id": key}
        value.update(id)
        ret_list.append(value)

    write_json(ret_list, file)

def data_upload(file, col_name):
    data = ret_json(file)
    client = MongoClient(f'mongodb://{username}:{password}@{ip}:27017/{db_name}?authSource={db_name}&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    
    for i in range(0, len(data), UPLOAD_LIMIT):
        batch_data = data[i:i+UPLOAD_LIMIT]
        try:
            client[db_name][col_name].insert_many(batch_data, ordered=False)
        except pymongo.errors.BulkWriteError as e:
            pass
        print(i)


def data_update_cast(file, col_name):
    data = ret_json(file)
    client = MongoClient(f'mongodb://{username}:{password}@{ip}:27017/{db_name}?authSource={db_name}&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    
    for key, value in data.items():
        filter = {'_id': key}
        result = list(client[db_name][col_name].find(filter=filter))
        if result:
            titles = value["titles"]
            client[db_name][col_name].update_one({'_id': key}, {'$push': {'titles': { '$each': titles}}})
        else:
            batch_data = {"_id": key, "name": value["name"], "pic": value["pic"], "titles": value["titles"]}
            client[db_name][col_name].insert_one(batch_data)

def data_update_mep(file, col_name):
    data = ret_json(file)
    client = MongoClient(f'mongodb://{username}:{password}@{ip}:27017/{db_name}?authSource={db_name}&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    
    for key, value in data.items():
        filter = {'_id': key}
        res = list(client[db_name][col_name].find(filter=filter))
        if res:
            try:
                seasons = value["season"]
                try:
                    episodes = value["episode"]
                except:
                    episodes = []
                
                for season in res[0]["seasons"]:
                    if season:
                        if season[0] in seasons:
                            seasons.remove(season[0])
                ret_seasons = []
                if seasons:
                    for i in seasons:
                        ret_seasons.append([i, ""])
                episodes = list(set(episodes) - set(res[0]["episode"]))
                
                client[db_name][col_name].update_one({'_id': key}, {'$push': {'seasons': { '$each': ret_seasons}}})
                client[db_name][col_name].update_one({'_id': key}, {'$push': {'episodes': { '$each': episodes}}})
            except Exception as e:
                print(e)
                print(key)
                a = input(0)
                # client[db_name][col_name].update_one({'_id': key},{'$set': {'seasons': []}} )
        else:
            print(key)

def update_driver():
    today_ids()
    title_driver("data/new_ids/today_id.json", "data/new_data/masters.json", "data/new_data/cast.json")
    join_ids("data/prev_ids/title_id.json", "data/new_data/masters.json")

    episode_ids()
    clean_episode("data/new_ids/today_ep_id.json", "data/prev_ids/title_id.json")
    episode_driver("data/new_ids/today_ep_id.json", "data/new_data/master_ep.json", "data/new_data/episode.json")
    join_ids("data/prev_ids/ep_id.json", "data/new_data/episode.json")
    add_ep_to_mep("data/new_data/episode.json", "data/new_data/master_ep.json")
    # print()

def database_update():
    conv_data("data/new_data/cast.json")
    conv_data("data/new_data/masters.json")
    conv_data("data/new_data/episode.json")
    data_upload("data/new_data/masters.json", "masters")
    data_upload("data/new_data/episode.json", "episodes")
    data_update_cast("data/new_data/cast.json", "casts")
    data_update_mep("data/new_data/master_ep.json", "masters")

if __name__ == "__main__":
    update_driver()
    database_update()