import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Homogenous filter : each output is mean of its kernal neighbour
kernel = np.ones((5,5),np.float32)/25
dst =cv2.filter2D(img,-1,kernel)#Homogenous filter

blur = cv2.blur(img,(5,5)) # blur image

#Gaussian Filter. Good for high freq noise
gblur = cv2.GaussianBlur(img,(5,5),0)

#Medain filter. Replace with averge. good for salt & pepper noise
median = cv2.medianBlur(img,5)#Kernel must me odd

#bilateral filter .Preserve edges
bfilter = cv2.bilateralFilter(img,9,75,75)

titles = [ 'image','2d Convolution0','blur','GBlur','Median','bilateral']
images = [img,dst,blur,gblur,median,bfilter]

for i in range(6):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()