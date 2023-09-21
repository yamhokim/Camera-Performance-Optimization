import argparse
import cv2
from method_1.CounterPerSec import CountsPerSec
from method_1.VideoGet import VideoGet
from method_1.VideoShow import VideoShow

def putIterationsPerSec(frame, iterations_per_sec):
    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
                (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    
    return frame

def noThreading(source=0):

    cap = cv2.VideoCapture(source)
    cps = CountsPerSec().start()

    while True:
        ret, frame = cap.read()

        if not ret or cv2.waitKey(1) == ord('q'):
            break

        frame = putIterationsPerSec(frame, cps.countersPerSec())
        cv2.imshow("Video", frame)
        cps.increment()


def threadVideoGet(source=0):

    video_getter = VideoGet(source).start()
    cps = CountsPerSec().start()

    while True:
        if (cv2.waitKey(1) == ord('q')) or video_getter.stopped:
            video_getter.stop()
            break

        frame = video_getter.frame
        frame = putIterationsPerSec(frame, cps.countersPerSec())
        cv2.imshow("Video", frame)
        cps.increment()

def threadVideoShow(source=0):

    cap = cv2.VideoCapture(source)
    ret, frame = cap.read()
    video_shower = VideoShow(frame).start()
    cps = CountsPerSec().start()

    while True:
        ret, frame = cap.read()
        if not ret or video_shower.stopped:
            video_shower.stop()
            break

        frame = putIterationsPerSec(frame, cps.countersPerSec())
        video_shower.frame = frame
        cps.increment()


def threadBoth(source=0):

    video_getter = VideoGet(source).start()
    video_shower = VideoShow(video_getter.frame).start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        frame = putIterationsPerSec(frame, cps.countersPerSec())
        video_shower.frame = frame
        cps.increment()


if __name__ == "__main__":
    source = r"C:\Users\yoonh\OneDrive\Desktop\HFAST Lab Materials\Suzan - Driver Drowsiness\Participant05_1. Recording 11272021 24230 PM_HD Pro Webcam C920.mp4"
    threadBoth(source)