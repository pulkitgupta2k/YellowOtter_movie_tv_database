from helper import *
from pprint import pprint

RANGE_OF_SOUP = 100

# adding titleType to the json
def add_type(ids, output_file):
    ready_1 = ret_json(output_file)
    rem_1 = ret_json(ids)

    for tid in rem_1:
        try:
            ready_1[tid[0]]["title_type"] = tid[1]
        except:
            try:
                 ready_1[tid[0]]["title_type"] = ""
            except:
                pass
    write_json(ready_1, output_file)

# First scrape getting general data


def get_general(input_file, output_file):
    data = ret_json(input_file)
    links = []
    script_data = {}
    for row in data:
        links.append(f"https://www.imdb.com/title/{row[0]}/")
    for i in range(0, len(links), RANGE_OF_SOUP):
        pages = getSoup_list(links[i: i + RANGE_OF_SOUP])
        for page in pages:
            try:
                script_data.update(general_helper(page))
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            write_json(script_data, output_file)
    write_json(script_data,output_file)

# First scrape helper
def general_helper(soup):
    data = soup.find("script", {"type": "application/ld+json"})
    data = json.loads(data.contents[0])
    t_id = data['url'][7:-1]
    name = data['name']
    try:
        desc = soup.find("div", {"class": "plot_summary"}
                         ).text.strip().split("\n")[0]
    except:
        desc = ""
    try:
        genre = data['genre']  # list
        if type(genre) is not list:
            genre = [genre]
    except:
        genre = [""]
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
    try:
        trailer_link = data['trailer']['embedUrl']
    except:
        trailer_link = "#"

    cast = []
    tv_season = []
    epidode = []
    ret_data = {}
    ret_data[t_id] = {"_id":t_id, "name":name, "description": desc,"genre": genre, "imdb_ratings": IMDB_rating, "rt_rating": Rotten_rating,
                      "age_rating": age_rating, "cover_image":cover_image, "air_date": air_date, "trailer_link_1": trailer_link, "cast": cast, 
                      "season": tv_season, "episode": epidode}

    return ret_data


def get_cast(ids, output_file, cast_file):
    data = ret_json(ids)
    links = []
    for t_id in data:
        links.append(f"https://www.imdb.com/title/{t_id[0]}/fullcredits")
    try:
        cast_data = ret_json(cast_file)
    except:
        cast_data = {}
    
    try:
        data = ret_json(output_file)
    except:
        data = {}

    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i: i+RANGE_OF_SOUP])
        for page in pages:
            try:
                t_id_data = cast_helper(page, data, cast_data)
                data[t_id_data[0]]["cast"] = (t_id_data[1])
                cast_data = t_id_data[2]
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            write_json(data, output_file)
            write_json(cast_data, cast_file)
    write_json(data, output_file)
    write_json(cast_data, cast_file)


# Second Scrape Helper

def cast_helper(soup, cast_data):
    data = []
    fullcredits_content = soup.find("div", {"id": "fullcredits_content"})
    headings_soup = fullcredits_content.findAll("h4")
    table_soup = fullcredits_content.findAll("table")

    t_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
    for index, heading in enumerate(headings_soup):
        heading_text = heading.text.lower()
        if "directed" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")
            for tr in trs[:5]:
                try:
                    try:
                        cast_id = tr.find("td", {"class": "name"}).find("a")[
                            "href"].split("/")[2]
                    except:
                        cast_id = ""
                    cast_name = tr.find("td", {"class": "name"}).text.strip()
                    real_name = tr.find("td", {"class": "name"}).text.strip()
                    cast_type = "dir"
                    pic = ""
                    data.append({"cast_id": cast_id, "played_as": cast_name, "type": cast_type})
                    if cast_id in cast_data.keys():
                        if t_id not in cast_data[cast_id]["titles"]:
                            cast_data[cast_id]["titles"].append(t_id)
                    else:
                        cast_data[cast_id] = {"name": real_name, "pic": pic, "titles": [t_id]}
                except:
                    pass
        elif "writer" in heading_text or "writing" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")
            for tr in trs[:5]:
                try:
                    try:
                        cast_id = tr.find("td", {"class": "name"}).find("a")[
                            "href"].split("/")[2]
                    except:
                        cast_id = ""
                    cast_name = tr.find("td", {"class": "name"}).text.strip()
                    real_name = tr.find("td", {"class": "name"}).text.strip()
                    cast_type = "writer"
                    pic = ""
                    data[t_id].append({"cast_id": cast_id, "played_as": cast_name, "type": cast_type})
                    if cast_id in cast_data.keys():
                        if t_id not in cast_data[cast_id]["titles"]:
                            cast_data[cast_id]["titles"].append(t_id)
                    else:
                        cast_data[cast_id] = {"name": real_name, "pic": pic, "titles": [t_id]}
                except:
                    pass
        elif "cast" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")[1:]
            for tr in trs[:200:2]:
                try:
                    td = tr.findAll("td")
                    try:
                        cast_id = td[0].find("a")['href'].split("/")[2]
                    except:
                        cast_id = ""
                    try:
                        pic = td[0].find("img")['loadlate']
                    except:
                        pic = ""
                    real_name = td[1].text.strip()
                    cast_name = td[3].text.strip().replace(
                        "&nbsp", "").split()[0]
                    cast_type = "cast"
                    data[t_id].append({"cast_id": cast_id, "played_as": cast_name, "type": cast_type})
                    if cast_id in cast_data.keys():
                        if t_id not in cast_data[cast_id]["titles"]:
                            cast_data[cast_id]["titles"].append(t_id)
                    else:
                        cast_data[cast_id] = {"name": real_name, "pic": pic, "titles": [t_id]}
                except:
                    pass
    return [t_id, data, cast_data]


# Third Scrape getting seasons
def get_season(file):
    data = ret_json(file)
    links = []
    for t_id_k, t_id_v in data.items():
        try:
            if t_id_v["title_type"] == "tvSeries" or t_id_v["title_type"] == "tvMiniSeries":
                links.append(f"https://www.imdb.com/title/{t_id_k}/episodes")
        except:
            data.pop(t_id_k, None)
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i: i+RANGE_OF_SOUP])
        for page in pages:
            try:
                t_id_data = season_helper(page)
                data[t_id_data[0]]["seasons"] = t_id_data[1]
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            write_json(data,file)
        write_json(data, file)

# third scrape helper
def season_helper(soup):
    t_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
    season_soup = soup.find("select", {"id": "bySeason"}).findAll("option")
    seasons = []
    for s_s in season_soup:
        seasons.append(s_s['value'])

    year_soup = soup.find("select", {"id": "byYear"}).findAll("option")[1:]
    years = []
    for y_s in year_soup:
        years.append(y_s['value'])

    if len(seasons) > len(years):
        years = years + [years[-1]] * (len(seasons) - len(years))

    ret = []
    for i, season in enumerate(seasons):
        ret.append([season, years[i]])
    return [t_id, ret]

# fourth scrape getting episodes
# def get_episode(file):
#     data = ret_json(file)
#     links = []
#     for t_id_k, t_id_v in data.items():
#         if t_id_v[11]:
#             for s_no in t_id_v[11]:
#                 links.append(
#                     f"https://www.imdb.com/title/{t_id_k}/episodes?season={s_no[0]}")
#     for i in range(0, len(links),  RANGE_OF_SOUP):
#         pages = getSoup_list(links[i: i+RANGE_OF_SOUP])
#         for page in pages:
#             try:
#                 t_id_data = episode_helper(page)
#                 if t_id_data[1] not in data[t_id_data[0]][12]:
#                     data[t_id_data[0]][12].append(t_id_data[1])
#             except:
#                 pass
#         if i % (10*RANGE_OF_SOUP) == 0:
#             print(i)
#             write_json(data, file)
#     write_json(data, file)

# fourth scrape helper


# def episode_helper(soup):
#     t_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
#     eps = soup.find("div", {"class": "list detail eplist"})
#     eps = eps.findAll("div", {"class": "list_item"})
#     ret = []

#     s = soup.find("select", {"id": "bySeason"}).find(
#         "option", {"selected": "selected"}).text.strip()
#     series_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
#     for ep in eps:
#         ep_id = ep.find("a", {"itemprop": "name"})['href'].split("/")[-2]
#         ep_no = s+"_"+ep.find("meta", {"itemprop": "episodeNumber"})['content']
#         ep_name = ep.find("strong").text.strip()
#         air_date = ep.find("div", {"class": "airdate"}).text.strip()
#         try:
#             ep_rating = ep.find(
#                 "span", {"class": "ipl-rating-star__rating"}).text
#         except:
#             ep_rating = ""
#         try:
#             ep_image = ep.find("img")['src']
#         except:
#             ep_rating = ""
#         ret.append([ep_id, series_id, ep_no, ep_name,
#                     air_date, ep_rating, ep_image])
#     return [t_id, ret]


# main driver
def title_driver(ids, masters, cast):
    get_general(ids, masters)
    print("General Done")
    add_type(ids, masters)
    print("Type Done")
    get_cast(ids, masters, cast)
    print("Cast Done")
    get_season(masters)
    print("Season Done")
