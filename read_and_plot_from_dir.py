import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()


def plot_image(image_path):
    print(image_path)

    img = cv.imread(image_path)
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    fig, ax = plt.subplots(1, 2, figsize=(16, 8))
    fig.tight_layout()

    ax[0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    ax[0].set_title("Original")

    ax[1].imshow(cv.cvtColor(gray_image, cv.COLOR_BGR2RGB))
    ax[1].set_title("Grayscale")
    plt.show()


def read_and_plot_images(directory):
    for folder in os.listdir(directory):
        counter = 0
        counter = counter + 1
        subFolder = os.path.join(directory, folder)
        if counter == 1:
            for filename in os.listdir(subFolder):
                if os.path.isfile(os.path.join(subFolder, filename)):
                    print(filename)
                    plot_image(os.path.join(subFolder, filename))
                    break
        else:
            break


def read_images(directory):
    for folder in os.listdir(directory):
        counter = 0
        counter = counter + 1
        subFolder = os.path.join(directory, folder)
        if counter == 1:
            for filename in os.listdir(subFolder):
                if os.path.isfile(os.path.join(subFolder, filename)):
                    print(filename)
                    break
        else:
            break


separator = os.getenv('DIRECTORY_SEPARATOR')
folder = os.getenv('FOLDER_PATH')
print(os.path.sep)
print(folder)
print(os.sep)

read_and_plot_images(folder)
