# Rectangle or Circle?

> A 20-line (very basic) "artificial intelligence" that can distinguish between 16x16 images of rectangles and circles. Inspired by a Veritasium video.

## Why?

I was bored.

## How?

*Currently, only images till `10.png` are read.*

0. Activate the virtual environment.
1. Make an image of a circle or rectangle.
2. Put it in the `train/` folder, with a filename of `<number>.png`. Eg: `2.png`.
3. Run `train.py`.
4. At the prompt, enter `1` if the image is a circle, or `0` if it is a rectangle.
5. `train.py` edits the `weights.png` image. If the image is a circle, the alpha (transparency) of the pixel is increased by 10. If it is a rectangle, the alpha is reduced by 10.
6. Then, make another image of a circle or rectangle and put it in the `tests/` folder.
7. Run `test.py`.
8. Be amazed! (or don't)

Thanks.
