from PIL import Image, ImageDraw


def getImage() -> Image:
    PATH_TO_IMAGE = "./static/icon.png"
    
    try:    image = Image.open(PATH_TO_IMAGE)
    except: image = generate(64, 64, 'black', 'white')
    
    return image


def generate(width:int, height:int, color1:str, color2:str) -> Image:
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image