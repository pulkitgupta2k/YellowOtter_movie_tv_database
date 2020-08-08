import json
from helper import *
from pprint import pprint

def add_ep():
    ready_1 = ret_json("data/ready_1.json")
    rem_1 = ret_json("data/rem_0.json")

    for tid in rem_1:
        try:
            if len(ready_1[tid[0]]) < 14:
                ready_1[tid[0]].append(tid[1])
        except:
            pass
    write_json(ready_1, "data/ready_2.json")
    

def check():
    ready_2 = ret_json("data/ready_2.json")

    for key, value in ready_2.items():
        if not len(value) == 14:
            pprint(value)

def manual():
    ready_2 = ret_json("data/ready_2.json")
    ready_2["tt11290556"].append('Movie')
    ready_2["tt7004686"].append('Short')
    write_json(ready_2, "data/ready_2.json")

if __name__ == "__main__":
    manual()
    check()

