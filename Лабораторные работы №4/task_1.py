# TODO решите задачу
import json

def task() -> float:
    name = "input.json"
    with open(name) as m:
        json_data = json.load(m)
    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_values, 3)

print(task())

