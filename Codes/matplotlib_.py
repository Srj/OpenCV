import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('lena.jpg',-1)
cv2.imshow('image',img) # reads file as bgr format

#Convert to rgb format for matplotlib
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img) # reads as rgb format
plt.xticks([]) , plt.yticks([]) # Hide labels for axes
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
