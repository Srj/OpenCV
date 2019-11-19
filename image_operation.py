import numpy as np 
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) #a tuple of row,cols,channels
print(img.size) #total number of pixels
print(img.dtype) #datatype of image


b,g,r = cv2.split(img) # split image into channels
img = cv2.merge((b,g,r)) # merge channels to single image

#ROI = Region of interest 
ball = img[280:340,330:390]
img[273:333,100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
dst = cv2.addWeighted(img,0.9,img2,0.2,0) # only same sized image can be added

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()