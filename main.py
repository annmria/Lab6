import cv2 # ska laddas ner
# import matplotlib.pyplot as plt
# import numpy as np

#reading the image:
image = cv2.imread('index.png')
# converting image to rgb
# cv2.cvtColor(src, code[, dst[, dstCn]]) -> dst
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # BGR till RGB, converts an image from one color space to another
#plotting the image
plt.imshow(image)
plt.show()
#saving image
cv2.imwrite('index.jpg', image)