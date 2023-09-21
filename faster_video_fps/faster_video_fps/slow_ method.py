from imutils.video import FPS
import imutils
import argparse
import numpy as np
import cv2

source = r"C:\Users\yoonh\Downloads\Jurassic Park Trailer.mp4"
stream = cv2.VideoCapture(source)
fps = FPS().start()

if not stream.isOpened():
    print("ERROR!")
else:
    while stream.isOpened():
        ret, frame = stream.read()

        if not ret:
            break

        #frame = imutils.resize(frame, width=450)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = np.dstack([frame, frame, frame])

        cv2.putText(frame, "Slow Method", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        fps.update()

    fps.stop()
    print(f"Elapsed Time: {fps.elapsed()}")
    print(f"Approximate FPS: {fps.fps()}")

    stream.release()
    cv2.destroyAllWindows()