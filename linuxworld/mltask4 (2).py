import cv2

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_face.xml')

cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the Webcam
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Apply the desired effect to the frame
    for (x, y, w, h) in faces:
        # Blur the background and keep the face clear
        blurred_frame = cv2.GaussianBlur(frame, (99, 99), 0)
        blurred_frame[y:y+h, x:x+w] = frame[y:y+h, x:x+w]
    
    # Display the modified frame
    cv2.imshow('Advanced Face Detection', blurred_frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
