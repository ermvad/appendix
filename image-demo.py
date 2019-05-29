import numpy
from matplotlib import pyplot as plt
from PIL import Image

color_red = (255, 0, 0)


def main():
    img = Image.open("image.jpg")
    img.show()
    width, height = img.size
    pixels = numpy.array(img.getdata())
    for i in range(0, width):
        pixels[i] = color_red
        pixels[width * height - 1 - i] = color_red
    for i in range(0, height):
        pixels[width * i] = color_red
        pixels[width * i + width - 1] = color_red
    plt.imshow(pixels.reshape((height, width, 3)))
    plt.show()


if __name__ == "__main__":
    main()
