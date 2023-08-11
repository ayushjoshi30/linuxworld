'''import cv2

cap=cv2.VideoCapture(0)
status, photo=cap.read()

facemodel = cv2.CascadeClassifier("haarcascade_face.xml")
print(len(facemodel.detectMultiScale(photo)))

while True:
    status , pics = cap.read()
    myfacecoord= facemodel.detectMultiScale(pics)
    if len(myfacecoord)==1:
        x1= myfacecoord[0][0]
        y1= myfacecoord[0][1]
        x2= myfacecoord[0][0] + myfacecoord[0][2]
        y2= myfacecoord[0][0] + myfacecoord[0][3]
        cv2.rectangle(pics,(x1,y1),(x2,y2),[0,255,0],2)

    cv2.imshow("my pic", pics)
    if cv2.waitKey(10) ==13:  #it is in millisecond 5000 millisecond == 5 sec
        break

cv2.destroyAllWindows()'''

import cv2

cap = cv2.VideoCapture(0)
status, photo = cap.read()

facemodel = cv2.CascadeClassifier("haarcascade_face.xml")

while True:
    status, pics = cap.read()
    myfacecoord = facemodel.detectMultiScale(pics)
    
    for (x, y, w, h) in myfacecoord:
        x1 = x
        y1 = y
        x2 = x + w
        y2 = y + h
        cv2.rectangle(pics, (x1, y1), (x2, y2), [0, 255, 0], 2)
        
        # Display the cropped face region in a separate window
        face_roi = pics[y1:y2, x1:x2]
        cv2.imshow("Detected Face", face_roi)

    cv2.imshow("Webcam", pics)
    
    if cv2.waitKey(10) == 13:  # Wait for Enter key to exit
        break

cap.release()
cv2.destroyAllWindows()
