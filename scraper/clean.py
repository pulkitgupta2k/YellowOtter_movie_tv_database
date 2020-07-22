import json

if __name__ == "__main__":
    with open("data/smol_data.json") as f:
        smol_data = json.load(f)
    with open("data/final_data.json") as f:
        final_data = json.load(f)
    
    smol_remaining = []

    for row in smol_data:
        if row[0] not in final_data.keys():
            smol_remaining.append(row)
    
    with open("data/smol_rem_data.json", "w") as f:
        json.dump(f, smol_remaining)