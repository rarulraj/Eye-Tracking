import cv2
import numpy as np
import dlib

capture = cv2.VideoCapture(0)

detection = dlib.get_frontal_face_detector()
while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    faces = detection(gray) #an array where all of the faces are stored
    for face in faces:
        print(face)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()  # Moved these two lines outside the loop
