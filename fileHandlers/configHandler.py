from pynput import keyboard
import json


CONFIG_PATH = "./config.json"

defaultConfig = {
    "layouts": {
        "displayed": [
            "qwerty",
            "йцукен-ua"
        ],
        "auto": [
            "qwerty",
            "йцукен-ua"
        ],
        "active": "Auto"
    },
    "options": {
        "translate": {
            "do": True,
            "keybind": "<alt>+b"
        },
        "copy": {
            "do": True,
            "keybind": "<ctrl>+c"
        },
        "paste": {
            "do": True,
            "keybind": "<ctrl>+v"
        }
    }
}


def updateConfig(data:dict):
    with open(CONFIG_PATH, "w") as file:
        json.dump(data, file, indent=4)


def verifyConfig(config:dict):
    # minimum layout requirement
    if len(config["layouts"]["displayed"]) < 2:
        raise(Exception("You need to list at least 2 'displayed' layouts"))
    
    # check key format
    for option in config["options"].values():
        try:
            keyboard.HotKey.parse(option["keybind"])
        except:
            raise(Exception(f"Invalid syntax for '{option}' keybind\n"+
                            "They need look like 'a', 'a+b' or '<alt>+b'\n"+
                            "Details: https://pynput.readthedocs.io/en/latest/keyboard.html#"))

    # check json keys
    if key := verifyConfigKeys(defaultConfig, config):
        raise(Exception(f"Encountered unknown key '{key}'"))


def verifyConfigKeys(default:dict, actual:dict) -> str | bool:
    for key in actual.keys():
        # do keys match
        if key not in default.keys():
            return key
        # is current key corresponds to a dict
        elif type(actual[key]) is dict:
            if verifyConfigKeys(default[key], actual[key]):
                return key
    # if everything's okay
    return False


""" Init config """

with open(CONFIG_PATH, "r", encoding="UTF-8") as file:
    config = json.load(file)

verifyConfig(config)