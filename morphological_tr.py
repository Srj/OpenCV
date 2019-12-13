import cv2
import numpy as np 
import matplotlib.pyplot as plt

img  = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)

#Dilation
#Normally used in Binary images
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
#Removes black dot in the balls of mask
#if any element in the area of kernel is one that pixel is one
kernel = np.ones((5,5),np.uint8) #bigger the square better the result. but one problem some place will merge
dilation = cv2.dilate(mask,kernel,iterations=2)

#Erosion
#Value of kernel will be 1 only if all the element is 1
erosion = cv2.erode(mask,kernel,iterations=1)

#Opening
# Erosion then dilation
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

#Closing
#Dilation then erosion
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)


titles = ['image','mask','dilation','erosion','opening','closing',6,7]
images = [img,mask,dilation,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()