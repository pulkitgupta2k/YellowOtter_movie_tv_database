import json

if __name__ == "__main__":
    with open("data/ready3_2.json") as f:
        data = json.load(f)

    new_data = {}

    for key, value in data.items():
        if not value[11] == []:
            new_data[key] = value
    
    with open("data/remaining.json", "w") as f:
        json.dump(new_data, f)
