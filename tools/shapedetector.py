import numpy as np
import cv2

class ShapeDetector:
    def __init__(self):
        pass

    @staticmethod
    def detect(c, image=None):
        shape = "undefined"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
            # img = np.zeros(image.shape, image.dtype)
            # cv2.drawContours(img, [c], -1, (255, 255, 255), -1)
            # cv2.imwrite("test.jpg", img)
            # cv2.imshow("undefined", img)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 90)
            # print circles
            # if circles is not None:
            #     shape = "circle"

        return shape

