# Importing Required Dependencies
import cv2

# Load The input Image
img = cv2.imread('image.png')
cv2.imshow('Original', img)
cv2.waitKey(0)

# Using the cvtColor() function to grayscale the image
grayscaleImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', grayscaleImage)
cv2.waitKey(0)

# Destroy the windows
cv2.destroyAllWindows()