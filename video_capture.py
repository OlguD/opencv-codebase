import cv2 as cv
from detect_face import detect_face

def capture_video(device: str = 'mac'):
    # 0 varsayılan kamerayı temsil eder
    if device == 'win':
        num = 0
    else:
        num = 1

    camera = cv.VideoCapture(num)  # Kamera indeksini kontrol et (0 veya 1 olabilir)

    while True:
        check, frame = camera.read()
        if not check:
            break

        # Yüz algılama fonksiyonunu uygula
        frame_with_faces = detect_face(frame)

        # Çerçeveyi yansıt (gerekirse)
        frame_with_faces = cv.flip(frame_with_faces, 1)
        cv.imshow("Camera - Detected Faces", frame_with_faces)

        key = cv.waitKey(1)
        if key == ord('q'):
            break

    camera.release()
    cv.destroyAllWindows()

capture_video()
