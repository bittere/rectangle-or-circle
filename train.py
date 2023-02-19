from PIL import Image

weights = Image.open("weights.png")


def darken(initial: tuple[float, float, float, float], amount: int):
    final = [255, 255, 255, initial[3]]
    final[3] += 10 * amount
    return tuple(final)


# heatmap (alpha):
# 255 -> +3
# 245 -> +2
# 235 -> +1
# 225 -> =0
# 215 -> -1
# 205 -> -2
# 195 -> -3

for i in range(1, 11):
    case = Image.open(f"train/{i}.png")
    isCircle = bool(int(input(f"is image {i} a circle? yes = 1, no = 0: ")))

    for x in range(case.height):
        for y in range(case.width):
            casePixel = case.getpixel((x, y))
            weightPixel = weights.getpixel((x, y))
            if casePixel == (0, 0, 0, 255):
                if isCircle:
                    weights.putpixel((x, y), darken(weightPixel, 1))
                elif not isCircle:
                    weights.putpixel((x, y), darken(weightPixel, -1))

weights.save("weights.png")
