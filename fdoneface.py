import cv2 
import time
import RPi.GPIO as GPIO
from threading import Thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 23
GPIO.setup(buzzer,GPIO.OUT)

def soundBuzzer():
    print("Buzzer On!!")
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(buzzer,GPIO.LOW)

start,stop = 0,0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

# capture frames from a camera 
cap = cv2.VideoCapture(0) 

# loop runs if capturing has been initialized. 
while 1: 

    # reads frames from a camera 
    ret, img = cap.read() 

    # convert to gray scale of each frames 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)     

    for (x,y,w,h) in faces:
        
        # To draw a rectangle in a face 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 

        # Detects eyes of different sizes in the input image 
        eyes = eye_cascade.detectMultiScale(roi_gray) 

        #To draw a rectangle in eyes 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
        
    if len(faces) == 1:
        if len(eyes) < 2:
            start = time.time()
        elif len(eyes) == 2:
            stop = time.time()
        total = start - stop
        print(total)
        if total > 2:
            cv2.putText(img, "DROWSINESS ALERT", (10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            t = Thread(target = soundBuzzer)
            t.deamon = True
            t.start()
            
              
    # Display an image in a window 
    cv2.imshow('img',img) 

    # Wait for Esc key to stop 
    k = cv2.waitKey(1) and 0xff
    if k == 27: 
        break

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 



