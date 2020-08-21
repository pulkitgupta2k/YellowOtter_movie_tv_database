from helper import *

RANGE_OF_SOUP = 100


def get_page_data_2(soup, data, cast_data):
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
                    try:
                        data[t_id].append({"cast_id": cast_id, "played_as": cast_name, "type": cast_type})
                    except:
                        data[t_id] = [{"cast_id": cast_id, "played_as": cast_name, "type": cast_type}]
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
                    try:
                        data[t_id].append({"cast_id": cast_id, "played_as": cast_name, "type": cast_type})
                    except:
                        data[t_id] = [{"cast_id": cast_id, "played_as": cast_name, "type": cast_type}]
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
                    try:
                        data[t_id].append({"cast_id": cast_id, "played_as": cast_name, "type": cast_type})
                    except:
                        data[t_id] = [{"cast_id": cast_id, "played_as": cast_name, "type": cast_type}]
                    if cast_id in cast_data.keys():
                        if t_id not in cast_data[cast_id]["titles"]:
                            cast_data[cast_id]["titles"].append(t_id)
                    else:
                        cast_data[cast_id] = {"name": real_name, "pic": pic, "titles": [t_id]}
                except:
                    pass
    return [t_id, data, cast_data]


def get_links(file, output_file):
    data = ret_json(file)
    try:
        links = ret_json(output_file)
    except:
        links = []

    for key, value in data.items():
        links.append(f"https://www.imdb.com/title/{key}/fullcredits")


    # for row in data:
    #     t_id = row['id']
    #     links.append(f"https://www.imdb.com/title/{t_id}/fullcredits")
    write_json(links, output_file)


def get_cast(links_file, output_file, cast_file):
    links = ret_json(links_file)
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
                t_id_data = get_page_data_2(page, data, cast_data)
                data.update(t_id_data[1])
                cast_data = t_id_data[2]
            except:
                pass
        if i % (10*RANGE_OF_SOUP) == 0:
            print(i)
            write_json(data, output_file)
            write_json(cast_data, cast_file)
    write_json(data, output_file)
    write_json(cast_data, cast_file)


def driver():
    get_links("data/ready_1.json", "data/links.json")
    get_cast("data/links.json", "data/cast_main.json", "data/cast_sep.json")


if __name__ == "__main__":
    driver()