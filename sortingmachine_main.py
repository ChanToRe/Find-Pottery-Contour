import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('sample.jpeg')

def findCt(image):
    gau = cv2.GaussianBlur(image, (11, 11), 0)
    gray = cv2.cvtColor(gau, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 180, 255, 0)
    thresh = cv2.bitwise_not(thresh)
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    image_contour = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)
    contour = contours[0]
    x, y, w, h = cv2.boundingRect(contour)
    result = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.show()
    
findCt(image)