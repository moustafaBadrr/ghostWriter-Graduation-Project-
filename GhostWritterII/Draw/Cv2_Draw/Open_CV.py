import numpy as np
import cv2
import os


def clear(height, width):
    paint_window = np.zeros((height, width, 3)) + 255
    cv2.imshow("OpenCV", paint_window)

    return paint_window


def screen(height, width):
    paint_window = np.zeros((height, width, 3)) + 255
    cv2.imshow("OpenCV", paint_window)
    return paint_window


def draw_line(paint_window, xp, yp, x, y, color_of_drawing, thickness):

    cv2.line(paint_window, (xp, yp), (x, y), color_of_drawing, thickness)
    cv2.imshow("OpenCV", paint_window)


def save_as_image(paint_window,imageNum):
    file_dir = os.path.dirname(os.path.realpath('_file_'))
    path = os.path.join(file_dir, 'Results\\IMAGE\\')
    path = os.path.join(path, "page_"+str(imageNum)+".png")
    cv2.imwrite(path, paint_window)


