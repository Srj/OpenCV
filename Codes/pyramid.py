import cv2
import numpy as np 
img = cv2.imread('lena.jpg')

#Gaussian Pyramid
# Repeated filtering & subsampling
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# hr2 = cv2.pyrUp(lr2)

# cv2.imshow('Original Image',img)
# cv2.imshow('Pyr Down',lr1)
# cv2.imshow('Pyr 2',lr2)
# cv2.imshow('Pyup ',hr2)

#Layering
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

#Laplacian Pyramid
layer = gp[5]
cv2.imshow('upper level',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()

