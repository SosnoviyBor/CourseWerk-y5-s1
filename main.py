import os
from pystray import Icon, Menu, MenuItem
from PIL import Image


class Main:
    icon = Icon('test', Image.open("static/icon.png"),
                menu=Menu(
                    # TODO item constructor
                    MenuItem(
                        "Config",
                        lambda: os.startfile("config.toml")
                    ),
                    MenuItem(
                        "About",
                        lambda: os.startfile("static/about.txt")
                    ),
                    Menu.SEPARATOR,
                    MenuItem(
                        'Exit',
                        lambda icon: icon.stop()
                    ),
                )
            )
    
    def __init__(self):
        self.icon.run()


if __name__ == "__main__":
    Main()