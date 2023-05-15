

records = {"student": [{"id": 1, "name": "marvel", "age": 14},
                       {"id": 2, "name": "mabel", "age": 12},
                       {"id": 3, "name": "pat", "age": 19}]}


with open("records.json", mode="w") as rec:
    json.dump(records, rec)

with open("records.json", mode="r") as rec2:
    print(json.dumps(json.load(rec2), indent=4))
