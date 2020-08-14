import csv
import json
import grequests
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
#HTML
def getSoup_list(urls):
    MAX_CONNECTIONS = 100
    requests = []
    for x in range(0,len(urls),MAX_CONNECTIONS):
        rs = (grequests.get(u, stream=False) for u in urls[x:x+MAX_CONNECTIONS])
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
    for x in range(0,len(urls),MAX_CONNECTIONS):
        rs = (grequests.get(u, stream=False) for u in urls[x:x+MAX_CONNECTIONS])
        time.sleep(0.2)
        requests.extend(grequests.map(rs))
    req = requests[0]
    html = req.content
    soup = BeautifulSoup(html, "html.parser")
    return soup