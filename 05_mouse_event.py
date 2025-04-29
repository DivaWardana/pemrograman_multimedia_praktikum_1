import cv2 as cv
import numpy as np

# Fungsi callback untuk mouse event
def drawfunction(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        # Menggambar lingkaran putih dengan radius 20 di posisi (x,y)
        cv.circle(img, (x, y), 10, (255, 0, 0), -1)

# Membaca gambar
img = cv.imread('bmw.jpeg')

# Membuat window dan menghubungkan mouse callback
cv.namedWindow('image')
cv.setMouseCallback('image', drawfunction)

while True:
    cv.imshow('image', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:  # Tekan ESC untuk keluar
        break

cv.destroyAllWindows()