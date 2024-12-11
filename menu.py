import os
from pystray import Menu, MenuItem
import json


# important shit
with open("./config.json", "r", encoding="UTF-8") as file:
    config = json.load(file)


def generate() -> Menu:
    mainMenu = Menu(
        MenuItem("Layman", None, enabled=False),
        Menu.SEPARATOR,
        layoutPickerMenu(),
        Menu.SEPARATOR,
        MenuItem("Config", lambda: os.startfile("config.json")),
        Menu.SEPARATOR,
        MenuItem("Exit", lambda app: app.stop()),
    )
    
    return mainMenu


def layoutPickerMenu():
    # generate schemes for translation
    displayedLayouts = config["layouts"]["displayed"]
    schemes = []
    for i in range(len(displayedLayouts)):
        for j in range(i+1 , len(displayedLayouts)):
            schemes.append(f"{displayedLayouts[i]} -> {displayedLayouts[j]}")
            schemes.append(f"{displayedLayouts[j]} -> {displayedLayouts[i]}")
    # sort them by name so they look neat
    schemes.sort(key=lambda v: v)
    
    # generate the menu itself
    menu = MenuItem(
        "Layouts",
        Menu(*[
            MenuItem(
                scheme,
                setActiveLayout(scheme),
                checked=getActiveLayout(scheme),
                radio=True
            )
            for scheme in schemes
        ]),
        default=True
    )
    
    return menu


""" radio logic """

activeLayout = config["layouts"]["active"]


def setActiveLayout(v):
    def inner(icon, item):
        global activeLayout
        activeLayout = v
        
        # config update
        if config["layouts"]["active"] != activeLayout:
            config["layouts"]["active"] = activeLayout
            with open("./config.json", "w", encoding="UTF-8") as file:
                json.dump(config, file, indent=4)
        
    return inner


def getActiveLayout(v):
    def inner(item):
        return activeLayout == v
    return inner