import cv2
import matplotlib.pyplot as plt
import numpy as np

#bikin variabel zzz_img untuk load gambarnya
zzz_img = cv2.imread('img/zzz.png')

#pisahin pixelnya ke masing masing channel (blue, green, red)
b, g, r = cv2.split(zzz_img)

#ekualisasi per channel
ekualisasi_b = cv2.equalizeHist(b)
ekualisasi_g = cv2.equalizeHist(g)
ekualisasi_r = cv2.equalizeHist(r)

#gabungin lagi channel hasil ekualisasi
hasil_ekualisasi = cv2.merge((ekualisasi_b, ekualisasi_g, ekualisasi_r))

#tampilin gambar asli
cv2.imshow('Gambar Asli', zzz_img)

#tampilin gambar setelah ekualisasi
cv2.imshow('Gambar Setelah Ekualisasi', hasil_ekualisasi)

#simpen gambar hasil ekualisasi
cv2.imwrite('img/gambar_ekualisasi.jpg', hasil_ekualisasi)

#buat histogram
fig, axs = plt.subplots(2, 3, figsize=(18, 8)) #setting ukuran canvas
colors = ['blue', 'green', 'red'] #list warna yang dipake

#looping untuk bikin histogram masing masing channel
for i, color in enumerate(colors):
    axs[0, i].hist(cv2.split(zzz_img)[i].ravel(), bins=256, range=[0, 256], color=color, alpha=0.7) #kenapa 256, supaya pixel ke 255 nya diinclude juga. alpha 0.7 biar histogram agak transparan
    axs[0, i].set_title(f'Histogram {color.capitalize()} - Asli')
    axs[1, i].hist(cv2.split(hasil_ekualisasi)[i].ravel(), bins=256, range=[0, 256], color=color, alpha=0.7)
    axs[1, i].set_title(f'Histogram {color.capitalize()} - Ekualisasi')

plt.tight_layout() #supaya layoutnya rapih

#simpen histogram
plt.savefig('img/histogram_perbandingan.png')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()