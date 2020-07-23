import json

if __name__ == "__main__":
    with open("data/smol_rem_data.json") as f:
        data = json.load(f)

    s = len(data)

    datas = [data[:int(s/4)], data[int(s/4): int(2*s/4)], data[int(2*s/4): int(3*s/4)], data[int(3*s/4):]]
    for index, d in enumerate(datas):
        with open(f"data/smol_data_{index}.json") as f:
            json.dump(f, d)