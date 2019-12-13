import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
#Laplacian
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

#SobelXY
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX = np.uint8(np.absolute(sobelX))#Image will be corrupted if not done
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY)
sobel =cv2.Sobel(img,cv2.CV_64F,1,1)
sobel = np.uint8(np.absolute(sobel))
titles = ['image','laplacian','SX','SY','Combined','Test']
images = [img,lap,sobelX,sobelY,sobelCombined,sobel]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])

    plt.yticks([])
plt.show()