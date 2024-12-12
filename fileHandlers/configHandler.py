import json


CONFIG_PATH = "./config.json"


with open(CONFIG_PATH, "r", encoding="UTF-8") as file:
    config = json.load(file)


def updateConfig(data):
    with open(CONFIG_PATH, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)


# def verify