import cv2
import numpy as np 

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3],np.uint8)

#Draw a line on the image
img = cv2.line(img,(0,0),(255,255),(255,0,0), 10)

#Draw an arrowed line
img = cv2.arrowedLine(img,(0,255),(255,255),(147,96,44),10)

#Draw a rectangle. Put -1 to fill the rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,255),10)

#Draw Circle
img = cv2.circle(img,(447,63),63,(0,255,0),-1)

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#Draw Text
img = cv2.putText(img,'OpenCv',(10,500),font,4,(255,255,255),10)






cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()