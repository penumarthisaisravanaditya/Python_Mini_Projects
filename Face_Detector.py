#pip install opencv-python

import cv2
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera!")
    exit()
while True:
    success, frame = camera.read()
    if not success:
        print("Failed to capture frame!")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(
            frame,
            (x,y),     #start point
            (x+w,y+h), # end point
            (0,255,0), #green color code
            2          # boder thikness
        )
        cv2.putText(
            frame,
            "Face Detected",
            (x,y-10),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (0,255,0),
            2
        )
    cv2.imshow("Face Detection using Python", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):  # Press q on keyboard to Exit
        break
camera.release()
cv2.destroyAllWindows()
        
    