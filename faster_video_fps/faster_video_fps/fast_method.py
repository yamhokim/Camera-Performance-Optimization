from imutils.video import FPS
from imutils.video import FileVideoStream
import numpy as np
import imutils
import time
import cv2

path = r"C:\Users\yoonh\Downloads\Jurassic Park Trailer.mp4"

fvs = FileVideoStream(path).start()
time.sleep(1.0)

fps = FPS().start()

if fvs.more() == False:
    print("Error opening file")

else:
    while fvs.more():
        frame = fvs.read()

        if frame is not None:
            #frame = imutils.resize(frame, width=450)
            
            cv2.putText(frame, f"Queue Size: {fvs.Q.qsize()}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

        fps.update()

fps.stop()
print(f"Elapsed Time: {fps.elapsed()}")
print(f"Approximate FPS: {fps.fps()}")

cv2.destroyAllWindows()
fvs.stop()
