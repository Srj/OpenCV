import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt

#1 Simple Th (Same every pixel)
img = cv.imread('gradient.png',0)

#white for 50 to 255
_,th1 = cv.threshold(img,50,255,cv.THRESH_BINARY)

#black for 200 to 255
_,th2 = cv.threshold(img,200,255,cv.THRESH_BINARY_INV)

#same until 127. 127 for 127 to 255
_,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)

#black until 127. Same afterwards
_,th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)

#Inverse of TOZERO
_,th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)


titles = ['1','2','3','4','5','6']
images = [img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray') #(rows,cols,index,method,color mode)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])



# cv.imshow('Image',img)
# cv.imshow('th4',th1)
# cv.imshow('th4',th2)
# cv.imshow('th4',th3)
# cv.imshow('th4',th4)
# cv.imshow('th4',th5)
# cv.imshow('th1',th1)
# cv.imshow('th2',th2)
# cv.imshow('t3',th3)

# cv.waitKey(0)
# cv.destroyAllWindows()

plt.show()