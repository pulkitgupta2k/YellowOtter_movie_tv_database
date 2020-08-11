from helper import *
from pprint import pprint

RANGE_OF_SOUP = 600


# tsv to json
def clean_tsv():
    data = ret_tsv("data/data.tsv")
    ids = []
    for row in data:
        if row[1] != 'tvEpisode':
            ids.append([row[0], row[1]])
    write_json(ids, "data/smol_data.json")

# adding titleType to the json


def add_ep():
    ready_1 = ret_json("data/ready_1.json")
    rem_1 = ret_json("data/smol_data.json")

    for tid in rem_1:
        try:
            if len(ready_1[tid[0]]) < 14:
                ready_1[tid[0]].append(tid[1])
        except:
            pass
    write_json(ready_1, "data/ready_1.json")

# First scrape getting general data


def get_imdb_info_1():
    data = ret_json("data/smol_data.json")
    links = []
    script_data = {}
    for row in data:
        links.append(f"https://www.imdb.com/title/{row[0]}/")
    for i in range(0, len(links), RANGE_OF_SOUP):
        print(i)
        pages = getSoup_list(links[i: i + RANGE_OF_SOUP])
        for page in pages:
            try:
                script_data.update(get_page_data_1(page))
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(script_data, "data/ready_1.json")
    write_json(script_data, "data/ready_1.json")

# First scrape helper


def get_page_data_1(soup):
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
    try:
        trailer_link = data['trailer']['embedUrl']
    except:
        trailer_link = "#"

    cast = []
    tv_season = []
    epidode = []
    ret_data = {}
    ret_data[t_id] = [t_id, name, desc, genre, IMDB_rating, Rotten_rating,
                      age_rating, cover_image, air_date, trailer_link, cast, tv_season, epidode]
    # pprint(ret_data)
    return ret_data


# Second Scrape getting cast details
def get_page_info_2():
    data = ret_json("data/ready_1.json")
    links = []
    for t_id in data.keys():
        links.append(f"https://www.imdb.com/title/{t_id}/fullcredits")
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i: i+RANGE_OF_SOUP])
        for page in pages:
            try:
                t_id_data = get_page_data_2(page)
                data[t_id_data[0]][10] = t_id_data[1]
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(data, "data/ready_1.json")
    write_json(data, "data/ready_1.json")

# Second Scrape Helper


def get_page_data_2(soup):
    fullcredits_content = soup.find("div", {"id": "fullcredits_content"})
    headings_soup = fullcredits_content.findAll("h4")
    table_soup = fullcredits_content.findAll("table")

    t_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
    cast = []
    for index, heading in enumerate(headings_soup):
        heading_text = heading.text.lower()
        if "directed" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")
            for tr in trs[:5]:
                try:
                    cast_name = ""
                    real_name = tr.find("td", {"class": "name"}).text.strip()
                    cast_type = "dir"
                    pic = ""
                    cast.append([cast_name, real_name, cast_type, pic])
                except:
                    pass
        elif "writer" in heading_text or "writing" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")
            for tr in trs[:5]:
                try:
                    cast_name = ""
                    real_name = tr.find("td", {"class": "name"}).text.strip()
                    cast_type = "writer"
                    pic = ""
                    cast.append([cast_name, real_name, cast_type, pic])
                except:
                    pass
        elif "cast" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")[1:]
            for tr in trs[:200:2]:
                try:
                    td = tr.findAll("td")
                    pic = td[0].find("img")['src']
                    cast_name = td[1].text.strip()
                    real_name = td[3].text.strip().replace(
                        "&nbsp", "").split()[0]
                    cast_type = "cast"
                    cast.append([cast_name, real_name, cast_type, pic])
                except:
                    pass
    return [t_id, cast]


# Third Scrape getting seasons
def get_page_info_3():
    data = ret_json("data/ready_1.json")
    links = []
    for t_id_k, t_id_v in data.items():
        if t_id_v[13] == "tvSeries" or t_id_v[13] == "tvMiniSeries":
            links.append(f"https://www.imdb.com/title/{t_id_k}/episodes")
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i: i+RANGE_OF_SOUP])
        for page in pages:
            try:
                t_id_data = get_page_data_3(page)
                data[t_id_data[0]][11] = t_id_data[1]
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            write_json(data, "data/ready_1.json")
        write_json(data, "data/ready_1.json")

# third scrape helper


def get_page_data_3(soup):
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


def get_page_info_4():
    data = ret_json("data/ready_1.json")
    links = []
    for t_id_k, t_id_v in data.items():
        if t_id_v[11]:
            for s_no in t_id_v[11]:
                links.append(
                    f"https://www.imdb.com/title/{t_id_k}/episodes?season={s_no[0]}")
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i: i+RANGE_OF_SOUP])
        for page in pages:
            try:
                t_id_data = get_page_data_4(page)
                if t_id_data[1] not in data[t_id_data[0]][12]:
                    data[t_id_data[0]][12].append(t_id_data[1])
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(data, "data/ready_1.json")
    write_json(data, "data/ready_1.json")

# fourth scrape helper


def get_page_data_4(soup):
    t_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
    eps = soup.find("div", {"class": "list detail eplist"})
    eps = eps.findAll("div", {"class": "list_item"})
    ret = []

    s = soup.find("select", {"id": "bySeason"}).find(
        "option", {"selected": "selected"}).text.strip()
    series_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
    for ep in eps:
        ep_id = ep.find("a", {"itemprop": "name"})['href'].split("/")[-2]
        ep_no = s+"_"+ep.find("meta", {"itemprop": "episodeNumber"})['content']
        ep_name = ep.find("strong").text.strip()
        air_date = ep.find("div", {"class": "airdate"}).text.strip()
        try:
            ep_rating = ep.find(
                "span", {"class": "ipl-rating-star__rating"}).text
        except:
            ep_rating = ""
        try:
            ep_image = ep.find("img")['src']
        except:
            ep_rating = ""
        ret.append([ep_id, series_id, ep_no, ep_name,
                    air_date, ep_rating, ep_image])
    return [t_id, ret]


# main driver
def driver():
    # tsv file to be downloaded from imdb database
    clean_tsv()
    get_imdb_info_1()
    add_ep()
    get_page_info_2()
    get_page_info_3()
    get_page_info_4()
