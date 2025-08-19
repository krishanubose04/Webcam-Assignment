# Trying to install required dependencies bbefore importing
!pip install opencv-python
!pip install opencv-contrib-python

import cv2

# Trying to initializing the VideoCapture object
cap = cv2.VideoCapture(0)

while True:
    # Capturing frame by frame
    ret, frame = cap.read()

    # Checking if the frame was captured successfully
    if not ret:
        print("Error in grabbing the frame!")
        break

    # Converting the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Displaying the result frame
    cv2.imshow("Webcam by StarterYou!", gray_frame)

    # Breaking the loop on a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing the webcam and closing the windows
cap.release()
cv2.destroyAllWindows()

