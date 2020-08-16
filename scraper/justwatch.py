from helper import *
from pprint import pprint

RANGE_OF_SOUP = 100

def justwatch_movies(n):
    data = {}
    for i in range(1, n, RANGE_OF_SOUP):
        links = []
        for j in range(i, i+RANGE_OF_SOUP):
            link = f"https://apis.justwatch.com/content/titles/movie/{str(j)}/locale/en_US"
            links.append(link)
        pages = getSoup_list(links)
        for page in pages:
            try:
                movie = helper_titles(json.loads(str(page)))
                data.update(movie)
            except Exception as e:
                print(e)
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(data, "data/justwatch_movies.json")
    write_json(data, "data/justwatch_movies.json")

def justwatch_shows(n):
    data = {}
    for i in range(1, n, RANGE_OF_SOUP):
        links = []
        for j in range(i, i+RANGE_OF_SOUP):
            link = f"https://apis.justwatch.com/content/titles/show/{str(j)}/locale/en_US"
            links.append(link)
        pages = getSoup_list(links)
        for page in pages:
            try:
                movie = helper_shows(json.loads(str(page)))
                data.update(movie)
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(data, "data/justwatch_shows.json")
    write_json(data, "data/justwatch_shows.json")


def helper_titles(page):
    platform = []
    imdb_id = ""
    for j in range(len(page["external_ids"])):
        if(page["external_ids"][j]["provider"] == "imdb"):
            imdb_id = (page["external_ids"][j]["external_id"])
    if not imdb_id:
        return
    try:
        for k in range(len(page["offers"])):
            streamType = page["offers"][k]["monetization_type"]
            platform_links = page["offers"][k]["urls"]["standard_web"]
            streamQuality = (page["offers"][k]["presentation_type"])
            platform_id = (page["offers"][k]["provider_id"])
            try:
                currency = page["offers"][k]["currency"]
            except:
                currency = ""
            try:
                price = str(page["offers"][k]["retail_price"])
            except:
                price = "NaN"
            platform.append([platform_id, streamQuality, streamType, currency, price, platform_links])
    except:
        platform = []
    try:
        youtube_link = page["clips"][0]["external_id"]
    except:
        youtube_link = ""
    return {imdb_id:{"platform": platform, "yt_trailer": youtube_link}}

if __name__ == "__main__":
    justwatch_movies(100)