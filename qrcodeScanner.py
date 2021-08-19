###########################################################################
# READING QR CODE SHOWN ON THE CAMERA AND DETECTING THE TEXT ON THE SCREEN
###########################################################################
# CODE STARTED FROM HERE AND IMPORTING ESSENTIALS FROM PYTHON LIBRARY
###########################################################################
# UNUSED MODULES
# import numpy as np
###########################################################################

import cv2
import pyzbar.pyzbar as pyzbar

img = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

def MainFunc():
    while True:
        _, frame = img.read()
        # cv2.addText("Sachin Accharya")
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            cv2.putText(frame, str(obj.data), (50, 50), font, 1, (255, 0, 0), 1)
            if str(obj.data) == "Sachin Acharya":
                print("Welcome, Sachin Acharya")
            else:
                print("NONE: Unknown Person")
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break