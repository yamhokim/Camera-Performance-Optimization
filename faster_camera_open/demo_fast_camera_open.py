import cv2
width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

if cam.isOpened() == False:
    print("Something went wrong")

else:
    while cam.isOpened():

        ret, frame = cam.read()
        if ret == None:
            break

        if ret == True:
            cv2.imshow("My Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord('x'):
                break

cam.release()
cv2.destroyAllWindows()


    
