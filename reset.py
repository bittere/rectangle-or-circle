from PIL import Image

weights = Image.open("weights.png")

for x in range(weights.height):
    for y in range(weights.width):
        weights.putpixel((x, y), (255, 255, 255, 225))

weights.save("weights.png")
