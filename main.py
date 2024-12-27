import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder

# Kamera ayarları
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Toplam para miktarını takip etmek için değişken
currentTotal = 0

# Renk bulucu nesnesi
colorDetector = ColorFinder()

# Özel renk ayarları (örneğin, turuncu renk için HSV değerleri)
hsvParameters = {'hmin': 0, 'smin': 0, 'vmin': 145, 'hmax': 63, 'smax': 91, 'vmax': 255}

# Boş işlev (Trackbar için gerekli)
def noAction(x):
    pass

# Ayarları kontrol etmek için bir pencere oluştur
cv2.namedWindow("Ayarlar")
cv2.resizeWindow("Ayarlar", 640, 240)
cv2.createTrackbar("Alt Eşik", "Ayarlar", 219, 255, noAction)
cv2.createTrackbar("Üst Eşik", "Ayarlar", 233, 255, noAction)

# Ön işleme işlevi
# Görüntüyü bulanıklaştırır, kenarları algılar ve morfolojik işlemler uygular
def preprocessImage(frame):
    blurredImage = cv2.GaussianBlur(frame, (5, 5), 3)
    lowerThresh = cv2.getTrackbarPos("Alt Eşik", "Ayarlar")
    upperThresh = cv2.getTrackbarPos("Üst Eşik", "Ayarlar")
    edgeImage = cv2.Canny(blurredImage, lowerThresh, upperThresh)
    kernel = np.ones((3, 3), np.uint8)
    edgeImage = cv2.dilate(edgeImage, kernel, iterations=1)
    edgeImage = cv2.morphologyEx(edgeImage, cv2.MORPH_CLOSE, kernel)

    return edgeImage

while True:
    # Kameradan görüntü oku
    success, frame = camera.read()
    if not success:
        print("Kamera görüntüsü alınamadı!")
        break

    # Ön işleme uygula
    processedImage = preprocessImage(frame)

    # Konturları bul
    contourImage, detectedContours = cvzone.findContours(frame, processedImage, minArea=20)

    # Toplam parayı sıfırla
    currentTotal = 0
    blankCanvas = np.zeros((480, 640, 3), np.uint8)  # Para miktarını göstermek için boş bir görüntü

    # Konturlar üzerinde işlem yap
    if detectedContours:
        for idx, contour in enumerate(detectedContours):
            perimeter = cv2.arcLength(contour['cnt'], True)
            approximations = cv2.approxPolyDP(contour['cnt'], 0.02 * perimeter, True)

            # Şekil kontrolü (örneğin daire veya elips)
            if len(approximations) > 5:
                areaSize = contour['area']
                x, y, w, h = contour['bbox']
                croppedImage = frame[y:y + h, x:x + w]

                # Renk tespiti
                detectedColor, colorMask = colorDetector.update(croppedImage, hsvParameters)
                whitePixels = cv2.countNonZero(colorMask)

                # Alan büyüklüğüne göre para miktarını hesapla
                if areaSize < 2050:
                    currentTotal += 5  # Küçük nesne
                elif 2050 < areaSize < 2500:
                    currentTotal += 5  # Orta boyut
                else:
                    currentTotal += 10  # Büyük nesne

    # Para miktarını yazdır
    cvzone.putTextRect(blankCanvas, f'Toplam: {currentTotal} Kurus', (50, 50), scale=8, offset=20, thickness=6, colorR=(0, 255, 0))

    # Görüntüleri birleştir
    stackedImages = cvzone.stackImages([processedImage, contourImage, blankCanvas, frame], 2, 1)
    cvzone.putTextRect(stackedImages, f'Toplam: {currentTotal} Kurus', (30, 30), scale=3, offset=5, thickness=2, colorR=(0, 0, 255))

    # Görüntüyü göster
    cv2.imshow("Sonuc", stackedImages)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
camera.release()
cv2.destroyAllWindows()
