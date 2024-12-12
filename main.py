from pystray import Icon, Menu, MenuItem
from PIL import Image

import falloffImage
import menu
from keyHandler import Handler


class Main:
    def __init__(self):
        try:    image = Image.open("static/icon.png")
        except: image = falloffImage.generate(64, 64, 'black', 'white')
        
        self.app = Icon('test name', image, menu=Menu(
            *menu.generate(),
            Menu.SEPARATOR,
            MenuItem("Exit", lambda: self.stopApp())
        ))
        
        self.app.run_detached()
        self.keyHandler = Handler()
    
    
    def stopApp(self):
        self.app.stop()
        self.keyHandler.listener.stop()


if __name__ == "__main__":
    Main()