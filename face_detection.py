import cv2

video = cv2.VideoCapture("src/baby_boy_video.webm")
if not video.isOpened():
    print("ERROR : Cannot open video")
    exit()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = video.read()
    if not ret:
        print("INFO : End of video.")

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=6,
    )

    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    frame = cv2.putText(frame, "Press (Q) to quit", (10, 20),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.imshow("Video Windows", frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
