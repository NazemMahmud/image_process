import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
# from read_and_plot_from_dir import read_and_plot_images
from blur_detect_laplacian import calculate_laplacian_var

load_dotenv()

focal_measures = []
separator = os.getenv('DIRECTORY_SEPARATOR')
directory = os.getenv('FOLDER_PATH')
print(os.path.sep)
print(directory)
print(os.sep)


def read_image_files(directory):
    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename)
            image = cv.imread(image_path)
            focal_measurement = calculate_laplacian_var(image)
            focal_measures.append(focal_measurement)
            with open('files/focal_measures.txt', 'a+') as fileObj:
                fileObj.write(f'{filename}: {focal_measurement} \n')


# read_and_plot_images(directory)
read_image_files(directory)

