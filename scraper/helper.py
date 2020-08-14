import csv
import json
import grequests
import requests
from bs4 import BeautifulSoup
import time

# CSV & JSON


def ret_tsv(file):
    with open(file, encoding="utf-8") as f:
        data = list(csv.reader(f, delimiter="\t"))
    return data


def write_json(data, file):
    with open(file, "w") as f:
        json.dump(data, f)


def ret_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def append_json(file, data):
    with open(file) as f:
        json_data = json.load(f)
    json_data.update(data)
    with open(file, "w") as f:
        json.dump(json_data, f)
# HTML


def getSoup_list(urls):
    MAX_CONNECTIONS = 100
    requests = []
    for x in range(0, len(urls), MAX_CONNECTIONS):
        rs = (grequests.get(u, stream=False)
              for u in urls[x:x+MAX_CONNECTIONS])
        print(".")
        time.sleep(0.2)
        response = grequests.map(rs)
        requests.extend(response)
        print(response)
    soups = []
    for request in requests:
        try:
            html = request.content
            soup = BeautifulSoup(html, "html.parser")
            soups.append(soup)
        except:
            pass
    return soups


def getSoup(link):
    urls = [link]
    MAX_CONNECTIONS = 100
    requests = []
    for x in range(0, len(urls), MAX_CONNECTIONS):
        rs = (grequests.get(u, stream=False)
              for u in urls[x:x+MAX_CONNECTIONS])
        time.sleep(0.2)
        requests.extend(grequests.map(rs))
    req = requests[0]
    html = req.content
    soup = BeautifulSoup(html, "html.parser")
    return soup


def movie_id(n):
    api_url = "https://apis.justwatch.com/content/titles/movie/" + \
        str(n)+"/locale/en_US"
    r = requests.get(api_url)
    r.raise_for_status()
    return r.json()


def show_id(n):
    api_url = "https://apis.justwatch.com/content/titles/show/" + \
        str(n)+"/locale/en_US"
    r = requests.get(api_url)
    r.raise_for_status()
    return r.json()


def justwatch_movies(n):
    data = []
    for i in range(1, n+1):
        page = movie_id(i)
        streamQuality = []
        streamType = []
        platform_links = []
        platform = []
        price = []
        imdb_id = ""
        youtube_link = ""
        for j in range(len(page["external_ids"])):
            if(page["external_ids"][j]["provider"] == "imdb"):
                imdb_id = (page["external_ids"][j]["external_id"])
        for k in range(len(page["offers"])):
            streamType.append(page["offers"][k]["monetization_type"])
            platform_links.append(page["offers"][k]["urls"]["standard_web"])
            streamQuality.append((page["offers"][k]["presentation_type"]))
            platform.append(page["offers"][k]["provider_id"])
            try:
                price.append(page["offers"][k]["currency"] +
                             " " + str(page["offers"][k]["retail_price"]))
            except:
                price.append("NaN")
        youtube_link = page["clips"][0]["external_id"]
        a = {"imdb": imdb_id, "quality": streamQuality, "type": streamType, "provider": platform,
             "price": price, "youtube_trailer": youtube_link}
        data.append(a)
    with open('outputfile.json', 'w') as outf:
        json.dump(data, outf)
    return (data)


def justwatch_shows(n):

    data = []
    for i in range(1, n+1):
        streamQuality = []
        streamType = []
        platform_links = []
        platform = []
        price = []
        seasons = []
        imdb_id = []
        youtube_link = []
        page = show_id(i)
        for j in range(len(page["external_ids"])):
            if(page["external_ids"][j]["provider"] == "imdb"):
                imdb_id.append(page["external_ids"][j]["external_id"])
        for k in range(len(page["offers"])):
            streamType.append(page["offers"][k]["monetization_type"])
            platform_links.append(page["offers"][k]["urls"]["standard_web"])
            streamQuality.append((page["offers"][k]["presentation_type"]))
            platform.append(page["offers"][k]["provider_id"])
            try:
                price.append(page["offers"][k]["currency"] +
                             " " + str(page["offers"][k]["retail_price"]))
            except:
                price.append("NaN")
            seasons.append(page["offers"][k]["element_count"])
        youtube_link.append(page["clips"][0]["external_id"])
        a = {"imdb": imdb_id, "quality": streamQuality, "type": streamType, "provider": platform,
             "price": price, "seasons": seasons, "youtube_trailer": youtube_link}
        data.append(a)
    with open('outputfile.json', 'w') as outf:
        json.dump(data, outf)
    return (data)
