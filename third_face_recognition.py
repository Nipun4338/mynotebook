import cv2
import numpy as np
import os
import profile
import time
from tkinter import *

def testme():
    start_time = time.time()

    print("--- %s seconds ---" % (time.time() - start_time))
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")

    font = cv2.FONT_HERSHEY_SIMPLEX

    # iniciate id counter
    #id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    #names = ['1778546619']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match

            if (confidence < 100):
                id = id

                if (round(100 - confidence) > 50.0):
                    # Do a bit of cleanup
                    print("\n [INFO] Exiting Program and cleanup stuff")
                    cam.release()
                    cv2.destroyAllWindows()
                    profile.myprofile(id)
                confidence = "  {0}%".format(round(100 - confidence))

            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(round(25-(time.time() - start_time),2))+"s remaining", (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('Testing...', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27 or (time.time() - start_time)>=25:
            print("Hello")
            window3= Tk()
            window3.title('Alert')
            window3.minsize(800, 400)
            window3.maxsize(800, 400)
            window3.configure(background='#456')
            Label(window3, text = "Unable to recognize!",font=('Impact', -20),bg='#456',fg="#df4759").place(relx = 0.5,
                               rely = 0.5,
                               anchor = 'center')
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
