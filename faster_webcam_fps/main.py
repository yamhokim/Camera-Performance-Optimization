from __future__ import print_function
from FPS import FPS
from WebcamVideoStream import WebcamVideoStream
import imutils
import cv2

def no_threading():
    stream = cv2.VideoCapture(0)
    fps = FPS().start()

    while fps.numFrames < 1000:
        grabbed, frame = stream.read()
        frame = imutils.resize(frame, width=400)
        flippedFrame = cv2.flip(frame, 1)

        cv2.imshow("Frame", flippedFrame)
        key = cv2.waitKey(1) & 0xFF

        fps.update()

    fps.stop()
    print(f"Elapsed Time: {fps.elapsed()}")
    print(f"Approximate FPS: {fps.fps()}")

    stream.release()
    cv2.destroyAllWindows()

def with_threading():
    vs = WebcamVideoStream(src=0).start()
    fps = FPS().start()

    while fps.numFrames < 1000:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        flippedFrame = cv2.flip(frame, 1)

        cv2.imshow("Frame", flippedFrame)
        key = cv2.waitKey(1) & 0xFF

        fps.update()

    fps.stop()
    print(f"Elapsed Time: {fps.elapsed()}")
    print(f"Approximate FPS: {fps.fps()}")

    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
    print("With Threading Results")
    with_threading()
    print("---------------------------------")
    print("No Threading Results")
    no_threading()