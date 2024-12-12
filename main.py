from pystray import Icon, Menu, MenuItem

from fileHandlers.imageHandler import getImage
import menu
from keyHandler import Handler


class Main:
    
    def __init__(self):
        self.app = Icon('test name', getImage(), menu=Menu(
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