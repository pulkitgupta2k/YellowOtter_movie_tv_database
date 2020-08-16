from helper import *
from pprint import pprint
RANGE_OF_SOUP = 2


# def show_id(n):
#     api_url = "https://apis.justwatch.com/content/titles/show/" + \
#         str(n)+"/locale/en_US"
#     r = requests.get(api_url)
#     r.raise_for_status()
#     return r.json()


def justwatch_movies(n):
    data = {}
    for i in range(1, n, RANGE_OF_SOUP):
        links = []
        for j in range(i, i+RANGE_OF_SOUP):
            link = f"https://apis.justwatch.com/content/titles/movie/{str(j)}/locale/en_US"
            links.append(link)
            print(link)
        pages = getSoup_list(links)
        for page in pages:
            try:
                movie = helper_movies(json.loads(str(page)))
                data.update(movie)
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(data, "data/justwatch.json")
    write_json(data, "data/justwatch.json")

def helper_movies(page):
    platform = []
    imdb_id = ""
    for j in range(len(page["external_ids"])):
        if(page["external_ids"][j]["provider"] == "imdb"):
            imdb_id = (page["external_ids"][j]["external_id"])
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
    youtube_link = page["clips"][0]["external_id"]
    return {imdb_id:{"platform": platform, "yt_trailer": youtube_link}}

# def justwatch_shows(n):

#     data = []
#     for i in range(1, n+1):
#         streamQuality = []
#         streamType = []
#         platform_links = []
#         platform = []
#         price = []
#         seasons = []
#         imdb_id = []
#         youtube_link = []
#         page = show_id(i)
#         for j in range(len(page["external_ids"])):
#             if(page["external_ids"][j]["provider"] == "imdb"):
#                 imdb_id.append(page["external_ids"][j]["external_id"])
#         for k in range(len(page["offers"])):
#             streamType.append(page["offers"][k]["monetization_type"])
#             platform_links.append(page["offers"][k]["urls"]["standard_web"])
#             streamQuality.append((page["offers"][k]["presentation_type"]))
#             platform.append(page["offers"][k]["provider_id"])
#             try:
#                 price.append(page["offers"][k]["currency"] +
#                              " " + str(page["offers"][k]["retail_price"]))
#             except:
#                 price.append("NaN")
#             seasons.append(page["offers"][k]["element_count"])
#         youtube_link.append(page["clips"][0]["external_id"])
#         a = {"imdb": imdb_id, "quality": streamQuality, "type": streamType, "provider": platform,
#              "price": price, "seasons": seasons, "youtube_trailer": youtube_link}
#         data.append(a)
#     with open('outputfile.json', 'w') as outf:
#         json.dump(data, outf)
#     return (data)


if __name__ == "__main__":
    justwatch_movies(10)