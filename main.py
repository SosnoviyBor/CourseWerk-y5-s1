from pystray import Icon
from PIL import Image

import falloffImage
import menu


class Main:
    try:    image = Image.open("static/icon.png")
    except: image = falloffImage.generate(64, 64, 'black', 'white')
    
    app = Icon('Layman', image, menu=menu.generate())
    
    def __init__(self):
        self.app.run()


if __name__ == "__main__":
    Main()