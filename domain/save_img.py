import cv2 as cv
import os


def save_image(image, save_path, file_name):
    #   create folder if path not existing
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    full_path = os.path.join(save_path, file_name)
    cv.imwrite(full_path, image)
