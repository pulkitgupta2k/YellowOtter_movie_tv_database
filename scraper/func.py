from helper import *
from pprint import pprint

def clean_tsv():
    data = ret_tsv("data.tsv")
    ids = []
    for row in data:
        if row[1] != 'tvEpisode':
            ids.append([row[0], row[1]])
    write_json(ids, "smol_data.json")

def get_imdb_info_1():
    data = ret_json("smol_data.json")
    links = []
    for row in data:
        links.append(f"https://www.imdb.com/title/{row[0]}/")
    for i in range(0, len(links), 1000):
        pages = getSoup_list(links[i : i+1000])
        for page in pages:
            script_data = get_page_data_1(page)

def get_page_data_1(soup):
    data = soup.find("script", {"type": "application/ld+json"})
    print(data.text)

def driver():
    # clean_tsv()
    # get_imdb_info_1()
    get_page_data_1(getSoup("https://www.imdb.com/title/tt4574334/"))