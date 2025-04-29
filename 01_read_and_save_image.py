#import library opencv
import cv2 as cv
#import library system
import sys

#mencari dan membaca file gambar "bmw.jpeg" dan disimpan pada variabel img
img =cv.imread(cv.samples.findFile("bmw.jpeg"))

#jika variabel img tidak ada isi maka ada pesan error
if img is None:
    sys.exit("Could not read the image.")

#menampilkan gambar dengan judul gambar Display Window
cv.imshow("Display window", img)

#tekan sembarang tombol untuk berhenti
k = cv.waitKey(0)

#tekan huruf s untuk menyimpan file gambar
if k == ord("s"):
    cv.imwrite("contoh_save.png",img)