from PIL import Image

weights = Image.open("weights.png")

for i in range(1, 11):
    case = Image.open(f"cases/{i}.png")
    circle = 0
    for x in range(case.height):
        for y in range(case.width):
            casePixel = case.getpixel((x, y))
            weightPixel = weights.getpixel((x, y))

            weightSum = ((weightPixel[3] - 225) / 10) / \
                (case.height * case.width)

            if casePixel == (0, 0, 0, 255) and circle < 1:
                circle += weightSum
            elif circle == 1:
                circle -= weightSum

    print(f"{i}: c") if circle > (1 - circle) else print(f"{i}: r")