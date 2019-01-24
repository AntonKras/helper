import cv2
import logging as log
from time import sleep


def init():
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log', level=log.INFO)
    return cv2.VideoCapture(0),faceCascade


def detect(videoCapture,faceCascade, title):
    ret, frame = videoCapture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, title, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0))
    r = (255,0,0)
    b =(0,255,0)
    if len(faces)==0:
        cv2.putText(frame, 'Lost person', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, r)
    else:
        (x,y,w,h) = faces[0]
        cv2.putText(frame, 'Person x {0} y {1} '.format(x,y), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, b)
    cv2.imshow('Video', frame)
    cv2.waitKey(30)
    return faces

# video_capture.release()
# cv2.destroyAllWindows()