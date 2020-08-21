from func import *

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


def update_driver():
    # today_ids()
    title_driver("data/today_id.json", "data/masters.json", "data/cast.json")

if __name__ == "__main__":
    update_driver()