from helper import *
from pprint import pprint

RANGE_OF_SOUP = 600

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
    for i in range(0, len(links), RANGE_OF_SOUP):
        pages = getSoup_list(links[i : i+ RANGE_OF_SOUP])
        script_data = {}
        for page in pages:
            try:
                script_data.update(get_page_data_1(page))
            except:
                pass
        append_json("data/final_data.json", script_data)

def get_page_data_1(soup):
    data = soup.find("script", {"type": "application/ld+json"})
    data = json.loads(data.contents[0])
    t_id = data['url'][7:-1]
    name = data['name']
    try:
        desc = soup.find("div", {"class": "plot_summary"}).text.strip().split("\n")[0]
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
    try:
        trailer_link = data['trailer']['embedUrl']
    except:
        trailer_link = "#"

    cast = []
    tv_season = []
    epidode = []
    ret_data = {}
    ret_data[t_id] = [t_id, name, desc, genre, IMDB_rating, Rotten_rating, age_rating, cover_image, air_date, trailer_link, cast, tv_season, epidode]
    # pprint(ret_data)
    return ret_data

def get_page_info_2():
    data = ret_json("data/final_data.json")
    links = []
    for t_id in data.keys():
        links.append(f"https://www.imdb.com/title/{t_id}/fullcredits")
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i : i+RANGE_OF_SOUP])
        script_data =  {}
        for page in pages:
            t_id_data = get_page_data_2(page)
            script_data[ t_id_data[0] ] [10]= t_id_data[1]
        append_json("data/final_data.json", script_data)


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
                cast_name = ""
                real_name = tr.find("td", {"class":"name"}).text.strip()
                cast_type = "dir"
                pic = ""
                cast.append([cast_name, real_name, cast_type, pic])
        elif "writer" in heading_text or "writing" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")
            for tr in trs[:5]:
                cast_name = ""
                real_name = tr.find("td", {"class":"name"}).text.strip()
                cast_type = "writer"
                pic = ""
                cast.append([cast_name, real_name, cast_type, pic])
        elif "cast" in heading_text:
            table = table_soup[index]
            trs = table.findAll("tr")[1:]
            for tr in trs[:200:2]:
                try:
                    td = tr.findAll("td")
                    pic = td[0].find("img")['src']
                    cast_name = td[1].text.strip()
                    real_name = td[3].text.strip().replace("&nbsp", "").split()[0]
                    cast_type = "cast"
                    cast.append([cast_name, real_name, cast_type, pic])
                except:
                    pass
    pprint([ t_id, cast])
    print(len(cast))
    return [ t_id, cast]

def get_page_info_3():
    data = ret_json("data/final_data.json")
    links = []
    for t_id_k, t_id_v in data.items():
        if t_id_v[13] == "tvSeries" or t_id_v[13] == "tvMiniSeries":
            links.append(f"https://www.imdb.com/title/{t_id_k}/episodes")
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i : i+RANGE_OF_SOUP])
        script_data = {}
        for page in pages:
            t_id_data = get_page_data_2(page)
            script_data[ t_id_data[0] ] [11]= t_id_data[1]
        append_json("data/final_data.json", script_data)

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
    print(ret)
    return [t_id, ret]


def get_page_info_4():
    data = ret_json("data/final_data.json")
    links = []
    for t_id_k, t_id_v in data.items():
        if t_id_v[11]:
            for s_no in t_id_v[11]:
                links.append(f"https://www.imdb.com/title/{t_id_k}/episodes/season={s_no}")
    for i in range(0, len(links),  RANGE_OF_SOUP):
        pages = getSoup_list(links[i : i+RANGE_OF_SOUP])
        script_data = {}
        for page in pages:
            t_id_data = get_page_data_4(page)
            if t_id_data[1] not in script_data[ t_id_data[0] ][12]:
                script_data[ t_id_data[0] ][12].append(t_id_data[1])
        append_json("data/final_data.json", script_data)


def get_page_data_4(soup):
    t_id = soup.find("link", {"rel": "canonical"})["href"].split("/")[-2]
    eps = soup.find("div", {"class": "list detail eplist"})
    eps = eps.findAll("div", {"class": "list_item"})
    ret = []

    s = soup.find("select", {"id": "bySeason"}).find("option", {"selected": "selected"}).text.strip()
    print(s)

    for ep in eps:
        ep_id = ep.find("a", {"itemprop": "name"})['href'].split("/")[-2]
        ep_no = s+"_"+ep.find("meta", {"itemprop": "episodeNumber"})['content']
        ep_name = ep.find("strong").text.strip()
        air_date = ep.find("div", {"class": "airdate"}).text.strip()
        try:
            ep_rating = ep.find("span", {"class": "ipl-rating-star__rating"}).text
        except:
            ep_rating = ""
        try:
            ep_image = ep.find("img")['src']
        except:
            ep_rating = ""
        ret.append([ep_id, ep_no, ep_name, air_date, ep_rating, ep_image])
    pprint([t_id, ret])
    return [t_id, ret]

def driver():
    # clean_tsv()
    # get_imdb_info_1()
    # get_page_data_1(getSoup("https://www.imdb.com/title/tt0000002/"))
    # get_page_data_3(getSoup("https://www.imdb.com/title/tt0000001/fullcredits"))
    # get_page_data_3(getSoup("https://www.imdb.com/title/tt4574334/episodes"))
    get_page_data_4(getSoup("https://www.imdb.com/title/tt4574334/episodes?season=4"))