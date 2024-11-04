import cv2 as cv

def detect_face(frame):
    """
    Detects faces in a given frame and draws rectangles around them.
    """
    # Görüntüyü gri tonlamaya çevir
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    xml_path = "/Users/olgudegirmenci/Desktop/opencv-projects/haarcascade_frontalface_default.xml"
    # Haar-cascade xml dosyasını yükle
    haar_cascade = cv.CascadeClassifier(xml_path)

    # Yüzleri algıla
    faces_rect = haar_cascade.detectMultiScale(gray_frame, 1.1, 9)

    rgb = (0, 165, 255)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), rgb, 2)

    return frame
