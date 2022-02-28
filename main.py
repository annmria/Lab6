import cv2
import matplotlib.pyplot as plt
import numpy as np

#reading the image:
image = cv2.imread('index.png') # placeholder

# converting image to rgb
# cv använder bgr (blue green red), alltså bakvänt rgb (red green blue)
# cv2.cvtColor(src, code[, dst[, dstCn]]) -> dst
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # BGR till RGB, converts an image from one color space to another
cv2.imshow('RGB', rgb) # visar rgb-bild

# färg till svartvit
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# BGR to HSV (hue, saturation , color)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

#plotting the image
plt.imshow(image)
plt.show()

#saving image
cv2.imwrite('index.jpg', image)

# masking (fokusera på vissa delar i bilden)
blank = np.zeros(image.shape[:2], dtype='uint8') # dimensions have to be the same size as the image
cv2.imshow('Blank Image', blank)

mask = cv2.circle(blank, (image.shape[1]//2, image.shape[0]//2, 100, 255, -1))
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Masked Image', masked)

