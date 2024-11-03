import cv2 as cv

def capture_video(device: str='mac'):
    # 0 means default camera
    if device == 'win':
        num = 0

    camera = cv.VideoCapture(1)

    while True:
        check, frame = camera.read()
        if not check:
            break
        frame = cv.flip(frame, 1)
        cv.imshow("Camera", frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            break

    camera.release()
    cv.destroyAllWindows()

capture_video()
