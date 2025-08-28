import cv2

import os 
import numpy as np

import matplotlib.pyplot as plt

#Load the image in grayscale
apollo_image = cv2.imread('Data/Apollo_11_Launch.jpg', cv2.IMREAD_GRAYSCALE)

#View Image
plt.imshow(apollo_image,cmap="gray")
plt.show()

#crop the image 
cropped_image = apollo_image[200:600, 200:900]
plt.imshow(cropped_image,cmap="gray")
plt.show()

#edit brightness of the image
matrix = np.ones(cropped_image.shape, dtype = "uint8") * 100
img_brighter = cv2.add(cropped_image, matrix)
plt.imshow(img_brighter,cmap="gray")
plt.show()