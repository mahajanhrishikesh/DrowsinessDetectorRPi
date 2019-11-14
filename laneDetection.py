import cv2
import numpy as np

video = cv2.VideoCapture('road_car_view.mp4')
#car_cascade = cv2.CascadeClassifier('carhaar2.xml')

while True:
    ret, frame = video.read()
    if not ret:
        video = cv2.VideoCapture('road_car_view.mp4')
        continue
    
    
    #frame = cv2.resize(orig_frame, (700, 500))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    lower = np.array([18,94,140])
    upper = np.array([48,255,255])
    
    mask = cv2.inRange(hsv, lower, upper)
    edges = cv2.Canny(mask, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap = 50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0,255,0), 2)
    
    #cars = car_cascade.detectMultiScale(gray, 1.3, 2)
    #for (x,y,w,h) in cars:
    #    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(3)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()