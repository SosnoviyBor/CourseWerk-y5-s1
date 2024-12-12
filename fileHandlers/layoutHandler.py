import json


def getLayout(filename:str) -> dict:
    with open(f"./layouts/{filename}.json", "r", encoding="UTF-8") as file:
        return json.load(file)