from helper import *
from pprint import pprint

def clean_tsv():
    data = ret_tsv("data/data.tsv")
    ids = []
    for row in data:
        if row[1] != 'tvEpisode':
            ids.append([row[0], row[1]])
    write_json(ids, "smol_data.json")

def get_imdb_info_1():
    data = ret_json("data/smol_data.json")
    links = []
    for row in data:
        links.append(f"https://www.imdb.com/title/{row[0]}/")
    for i in range(0, len(links), 300):
        pages = getSoup_list(links[i : i+300])
        for page in pages:
            script_data = get_page_data_1(page)

def get_page_data_1(soup):
    data = json.loads(soup.find("script", {"type": "application/ld+json"}).text)

    t_id = data['url'][7:-1]
    name = data['name']
    try:
        desc = soup.find("div", {"class": "plot_summary"}).text
    except:
        desc = ""
    try:
        genre = data['genre']   #list
    except:
        genre = ""
    try:
        IMDB_rating = data['aggregateRating']['ratingValue']
    except:
        IMDB_rating = ""
    Rotten_rating = None
    try: 
        age_rating = data['contentRating']
    except:
        age_rating = ""
    try:
        cover_image = data['image']
    except:
        cover_image = ""
    try:
        air_date = data['datePublished']
    except:
        air_date = ""
    trailer_link = "#"

    cast = []
    tv_season = []
    epidode = []

    ret_data = [t_id, name, desc, genre, IMDB_rating, Rotten_rating, age_rating, cover_image, air_date, trailer_link, cast, tv_season, epidode]
    pprint(ret_data)
    return ret_data

def driver():
    # clean_tsv()
    get_imdb_info_1()
    # get_page_data_1(getSoup("https://www.imdb.com/title/tt0000002/"))