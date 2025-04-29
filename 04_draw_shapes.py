import numpy as np
import cv2
img = cv2.imread('bmw.jpeg', 1)

rectangle = cv2.rectangle(img,(90,40),(200,200),(0,255,0),5)

cv2.imshow('image', rectangle)
cv2.waitKey(0)

# Menulis teks pada gambar
txt="mobil"
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,txt,(10,100),font, 2, (0, 0, 0), 2, cv2.LINE_AA)

# Menampilkan gambar dengan persegi panjang
cv2.imshow('Rectangle', rectangle)
cv2.waitKey(0)

# Menampilkan gambar dengan teks
cv2.imshow('Text', img)
cv2.waitKey(0)

cv2.destroyAllWindows()