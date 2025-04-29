#import library numpy dengan nama np
import numpy as np
#import library cv2
import cv2
#import library matplotlib dengan nama plt
import matplotlib.pyplot as plt
#load an color image in grayscale
img = cv2.imread('bmw.jpeg')
#Using cv2.split() to split channels of coloured image
b,g,r = cv2.split(img)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(b, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(g, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(r, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

# Gabungkan kembali ke RGB (matplotlib menggunakan RGB, bukan BGR)
img_rgb = cv2.merge([r, g, b])

plt.subplot(2, 2, 4)
plt.imshow(img_rgb)
plt.title('Merged RGB Image')
plt.axis('off')

plt.tight_layout()
plt.show()