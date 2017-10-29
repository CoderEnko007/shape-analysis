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
            #shape = "circle"
            #print image.shape
            (x, y, w, h) = cv2.boundingRect(c)
            mask = np.zeros(image.shape, image.dtype)
            cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)
            #cv2.imshow("mask", mask)
            img = cv2.bitwise_and(image, image, mask=mask)
            #cv2.imshow("undefined", img)
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100)
            if circles is not None:
                shape = "circle"
                # print(circles.shape)
                # print(circles)
                # circles = np.round(circles[0, :]).astype("int")
                # print(circles)
                # for (x, y, r) in circles:
                #     cv2.circle(img, (x, y), r, (0, 255, 0), 3)
                #     cv2.circle(img, (x, y), 2, (255, 0, 0), 3)
                # cv2.imshow("img", img)

        return shape

