import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as json_file:
        data_from_file = json.load(json_file)
    return round(sum(item["score"] * item["weight"] for item in data_from_file), 3)

print(task())
