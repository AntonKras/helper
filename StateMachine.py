import cv2

import face as fac

videoCapture, faceCascade = fac.init()

statemachine = {
    '1': "Wait",
    '2': "Find bookshelf",
    '3': "Turn on 60 degrees ",
    '4': "Turn to a bookshelf",
    '5': "Make a step",
    '6': "Find user",
    '7': "Fly to a user",
    '8': "Give a book",
    '9': 'EndState',
    '10': 'Receive a book'

}
state = '1'
while True:
    if state == '1':
        print(statemachine[state])
        print(statemachine['2'])
        print(statemachine['4'])
        print(statemachine['10'])
        state='6'

    if state == '3':
        print(statemachine[state])
        for i in range(10):
            faces = fac.detect(videoCapture, faceCascade, statemachine[state])
        state='6'
    if state == '4':
        print(statemachine['4'])
        break
    if state == '6':
        print(statemachine[state])
        flag = False
        for i in range(10):
            faces = fac.detect(videoCapture,faceCascade,statemachine[state])
            if len(faces) > 0:
                flag = True
        if flag:
            state = '7'
        else:
            state='3'
    if state == '7':
        print(statemachine[state])
        flag = False
        faces = None
        for i in range(10):
            faces = fac.detect(videoCapture, faceCascade, statemachine[state])
            if len(faces) > 0:
                flag = True
        if flag==False:
            state = '6'
        for (x, y, w, h) in faces:
            if w*h >100000:
                state='8'
    if state == '8':
        print(statemachine[state])

        state='9'
    if state == '9':
        print(statemachine[state])
        videoCapture.release()
        cv2.destroyAllWindows()
        exit(0)
    # if case: # default, could also just omit condition or 'if True'
    #   print ("something else!")
    #  case = str(input())
