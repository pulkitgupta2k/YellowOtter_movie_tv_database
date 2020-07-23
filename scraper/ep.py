import json


if __name__ == "__main__":
    with open("data/smol_data.json") as f:
        data = json.load(f)
    u_d = []
    for d in data:
        if d[1] not in u_d:
            u_d.append(d[1])
            print(d[1])