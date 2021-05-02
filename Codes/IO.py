#imports opencv. Requires Numpy
import cv2

#Open a image file. 
#Doesn't raise exception if file not found.Returns None.
img = cv2.imread('data/IO.png',0)

print(type(img))
# display image
#Display only for a miliseconds
cv2.imshow('image',img)

#Number of ms you want to wait. Give 0 to wait until the window is closed.
#The pressed key will be saved in 'k'
#Some 64 bit machine requires '& 0xFF' after wait key
k = cv2.waitKey(0)


if k == 27: #27 is ESC
    #Destroys all windows
    cv2.destroyAllWindows()

elif k == ord('s'):
    #Writes a image
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()

