# - blur detect - show me the blurred image names and normal image names
# - normal image file names
# - Advanced, removing blurry to normal
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()
focal_measures = []


def read_images(directory):
    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename)
            image = cv.imread(image_path)
            focal_measurement = calculate_laplacian_var(image)
            focal_measures.append(focal_measurement)
            with open('files/focal_measures.txt', 'a+') as fileObj:
                fileObj.write(f'{filename}: {focal_measurement} \n')


def calculate_laplacian_var(image_path):
    """
        * convert RGB image to Gray scale image
        * Measure focal measure score (laplacian approach)
    """
    gray_image = cv.cvtColor(image_path, cv.COLOR_BGR2GRAY)
    fvar = cv.Laplacian(gray_image, cv.CV_64F).var()
    return fvar
