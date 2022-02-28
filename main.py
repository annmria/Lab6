import cv2
import matplotlib.pyplot as plt
# import numpy as np

#reading the image:
image = cv2.imread('index.png')

# converting image to rgb
# cv använder bgr (blue green red), alltså bakvänt rgb (red green blue)
# cv2.cvtColor(src, code[, dst[, dstCn]]) -> dst
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # BGR till RGB, converts an image from one color space to another
cv2.imshow('RGB', rgb) # visar rgb-bild

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # färg till svartvit

# BGR to HSV (hue, saturation , color)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

#plotting the image
plt.imshow(image)
plt.show()

#saving image
cv2.imwrite('index.jpg', image)