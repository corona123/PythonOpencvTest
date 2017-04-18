import numpy as np
import logging
import sys
import cv2
import os
import common


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

out = cv2.VideoWriter('recording_000.avi',fourcc, 20.0, (640,480))

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
       
        ret, frame = cap.read()
        
        if ret==True:
            frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # write the flipped frame
            filename(fourcc)
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
