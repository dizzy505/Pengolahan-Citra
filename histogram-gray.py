import cv2
import matplotlib.pyplot as plt
import numpy as np

#bikin variabel zzz_img untuk load gambarnya
zzz_img = cv2.imread('img/zzz.png')

#ubah gambar ke grayscale
zzz_gray = cv2.cvtColor(zzz_img, cv2.COLOR_BGR2GRAY)

#ekualisasi histogram untuk grayscale
ekualisasi_gray = cv2.equalizeHist(zzz_gray)

#tampilin gambar asli dan hasil ekualisasi
cv2.imshow('Gambar Asli (Grayscale)', zzz_gray)
cv2.imshow('Gambar Setelah Ekualisasi (Grayscale)', ekualisasi_gray)

#simpen gambar hasil ekualisasi
cv2.imwrite('img/gambar_ekualisasi_gray.jpg', ekualisasi_gray)

#buat histogram
fig, axs = plt.subplots(1, 2, figsize=(12, 6))  #setting ukuran canvas

#histogram gambar asli
axs[0].hist(zzz_gray.ravel(), bins=256, range=[0, 256], color='gray', alpha=0.7)
axs[0].set_title('Histogram Asli (Grayscale)')

#histogram gambar setelah ekualisasi
axs[1].hist(ekualisasi_gray.ravel(), bins=256, range=[0, 256], color='gray', alpha=0.7)
axs[1].set_title('Histogram Ekualisasi (Grayscale)')

plt.tight_layout()  #supaya layoutnya rapi

#simpen histogram
plt.savefig('img/histogram_perbandingan_gray.png')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()