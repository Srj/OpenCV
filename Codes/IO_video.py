import cv2

#Capture Video. Provide video name or device index. {0,-1} for default.
cap = cv2.VideoCapture(0)
#fourcc code for wrting video. (Codec)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # or 'X','V','I','D'

#initializes video writer
out = cv2.VideoWriter('out.avi',fourcc,20.0,(640,480))

while cap.isOpened() : # Checks whether file or cam is opened

    #ret is a boolean containing whether frame is available or not. Image will be saved in frame.
    ret,frame = cap.read()
    if ret == True:

        #Get different properties of video
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        #Save the frame
        out.write(frame)

        #convert image color
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        # putting any large number will freeze frames for that ms.
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

#Release the resources    
cap.release()

#Save the file
out.release()

cv2.destroyAllWindows()

