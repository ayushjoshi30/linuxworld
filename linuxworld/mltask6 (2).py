import cv2

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_face.xml')

cap = cv2.VideoCapture(0)

# Load the accessory image
accessory_img = cv2.imread(r'C:\Users\HP\Desktop\training\sunglass.jpeg', cv2.IMREAD_UNCHANGED)

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected face
    for (x, y, w, h) in faces:
        # Resize the accessory image to match the size of the detected face
        accessory_resized = cv2.resize(accessory_img, (w, h))

        # Calculate the coordinates to overlay the accessory on the face
        x1 = x
        y1 = y - int(h / 2)
        x2 = x1 + w
        y2 = y1 + h

        # Overlay the accessory on the face region
        for c in range(3):
            frame[y1:y2, x1:x2, c] = accessory_resized[:, :, c] * (accessory_resized[:, :, 3] / 255.0) + \
                                      frame[y1:y2, x1:x2, c] * (1.0 - accessory_resized[:, :, 3] / 255.0)

    # Display the frame with accessories added
    cv2.imshow('Accessory Addition', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
