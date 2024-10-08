import cv2 as cv
import numpy as np

img = cv.imread("photos/cats 2.jpg")
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (img.shape[1]//2 + 30,img.shape[0]), 255, -1)
weird = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird', weird)

mask = cv.circle(blank, (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=weird)
cv.imshow('Masked', masked)


cv.waitKey(0)