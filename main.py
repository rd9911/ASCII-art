from PIL import Image
import numpy as np


def show_ascmi(image):
    image = Image.open(image)
    image.show()
    #
    # def asmci(image):
    #     img_data = np.array(image.get_da)

    her = np.array(image.getdata())
    print("Successfully constructed pixel matrix!")
    print(f"Pixel matrix size is: {image.size[0]}x{image.size[1]}")
    print(her)

show_ascmi("/home/rd9911/Downloads/ascii-pineapple.jpeg")

# "/home/rd9911/Downloads/ascii-pineapple.jpeg"