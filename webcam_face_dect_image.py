import cv2
import cvlib as cv
import numpy as np
 
# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

#classifier
xml = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(xml)

#video caputure setting
capture = cv2.VideoCapture(0) # initialize, # is camera number
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1280) #CAP_PROP_FRAME_WIDTH == 3
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,1000) #CAP_PROP_FRAME_HEIGHT == 4

find_num = 0    
captured_num = 0
    
# loop through frames
while(True):

    # read frame from webcam 
    status, frame = webcam.read()
    find_num = find_num + 1
    
    # 이미지 내 얼굴 검출
    found_face, confidence = cv.detect_face(frame)
    
    # loop through detected faces
    for idx, f in enumerate(found_face):
        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]
 
        if find_num % 8  == 0:
            captured_num = captured_num + 1
            found_faces_img = frame[startY:endY, startX:endX, :]
            cv2.imwrite('./face/face'+str(captured_num)+'.jpg', found_faces_img) # 인식한 얼굴 사진 저장
 
#    frame = cv2.flip(frame, 1) # 좌우 대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,1.05, 5)

    if len(faces):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # display output
    cv2.imshow('webcam', frame)     
    
    # press button to stop
    if cv2.waitKey(1) > 0 : break
    
# release resources
webcam.release()
cv2.destroyAllWindows()   
