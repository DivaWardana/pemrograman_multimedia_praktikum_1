import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('bmw.jpeg', 1)

# Resize gambar menjadi setengah ukuran asli
height, width = img.shape[:2]
resized_img = cv2.resize(img, (int(width/2), int(height/2)), interpolation=cv2.INTER_AREA)

# Rotate gambar 90 derajat searah jarum jam
h, w = img.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 90, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

# Resize gambar asli dan rotate agar ukurannya sama dengan resized_img untuk penggabungan
img_small = cv2.resize(img, (int(width/2), int(height/2)), interpolation=cv2.INTER_AREA)
rotated_small = cv2.resize(rotated_img, (int(width/2), int(height/2)), interpolation=cv2.INTER_AREA)

# Fungsi untuk menambahkan teks di atas gambar
def add_label(image, label):
    # Buat area kosong di atas gambar untuk teks (misal 30 piksel tinggi)
    labeled_img = cv2.copyMakeBorder(image, 30, 0, 0, 0, cv2.BORDER_CONSTANT, value=[255,255,255])
    # Tambahkan teks (putText) di area kosong tersebut
    cv2.putText(labeled_img, label, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2, cv2.LINE_AA)
    return labeled_img

# Tambahkan label pada setiap gambar
img_labeled = add_label(img_small, "Original")
resized_labeled = add_label(resized_img, "Resized")
rotated_labeled = add_label(rotated_small, "Rotated")

# Gabungkan ketiga gambar secara horizontal
combined = np.hstack((img_labeled, resized_labeled, rotated_labeled))

# Tampilkan gambar gabungan dengan label
cv2.imshow('Original | Resized | Rotated', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()