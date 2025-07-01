import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

st.set_page_config(page_title="Ekualisasi Histogram", layout="wide")
st.title("Ekualisasi Histogram")

zzz = 'img/zzz.png'

mode = st.selectbox("Pilih mode ekualisasi:", ["RGB (Per Channel)", "Grayscale"])
negasi = st.checkbox("Aktifkan gambar negatif")

brightness = st.slider("Brightness", -100, 100, 0)
kontras = st.slider("Kontras", 1.0, 3.0, 1.0)

zzz_img = cv2.imread(zzz)

if zzz_img is None:
    st.error(f"Gambar tidak ditemukan: {zzz}")
    st.stop()

zzz_img = cv2.convertScaleAbs(zzz_img, alpha=kontras, beta=brightness)

if negasi:
    zzz_img = 255 - zzz_img

if mode == "RGB (Per Channel)":
    b, g, r = cv2.split(zzz_img)
    eq_b = cv2.equalizeHist(b)
    eq_g = cv2.equalizeHist(g)
    eq_r = cv2.equalizeHist(r)
    hasil_eq = cv2.merge((eq_b, eq_g, eq_r))

    col1, col2 = st.columns(2)
    col1.image(cv2.cvtColor(zzz_img, cv2.COLOR_BGR2RGB), caption="Gambar Asli", use_column_width=True)
    col2.image(cv2.cvtColor(hasil_eq, cv2.COLOR_BGR2RGB), caption="Setelah Ekualisasi", use_column_width=True)

    fig, axs = plt.subplots(2, 3, figsize=(15, 6))
    colors = ['blue', 'green', 'red']
    for i, (ori, eq, color) in enumerate(zip([b, g, r], [eq_b, eq_g, eq_r], colors)):
        axs[0, i].hist(ori.ravel(), bins=256, range=[0, 256], color=color)
        axs[0, i].set_title(f'{color.upper()} - Asli')
        axs[1, i].hist(eq.ravel(), bins=256, range=[0, 256], color=color)
        axs[1, i].set_title(f'{color.upper()} - Ekualisasi')
    st.pyplot(fig)

    hasil_pil = Image.fromarray(cv2.cvtColor(hasil_eq, cv2.COLOR_BGR2RGB))
    buf = io.BytesIO()
    hasil_pil.save(buf, format="PNG")
    st.download_button("Download Gambar Ekualisasi", buf.getvalue(), file_name="hasil_ekualisasi_rgb.png", mime="image/png")

else:
    gray = cv2.cvtColor(zzz_img, cv2.COLOR_BGR2GRAY)
    eq_gray = cv2.equalizeHist(gray)

    col1, col2 = st.columns(2)
    col1.image(gray, caption="Asli (Grayscale)", channels="GRAY", use_column_width=True)
    col2.image(eq_gray, caption="Setelah Ekualisasi", channels="GRAY", use_column_width=True)

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    axs[0].hist(gray.ravel(), bins=256, range=[0, 256], color='gray')
    axs[0].set_title('Histogram Asli')
    axs[1].hist(eq_gray.ravel(), bins=256, range=[0, 256], color='gray')
    axs[1].set_title('Histogram Ekualisasi')
    st.pyplot(fig)

    hasil_gray_pil = Image.fromarray(eq_gray)
    buf = io.BytesIO()
    hasil_gray_pil.save(buf, format="PNG")
    st.download_button("Download Gambar Ekualisasi", buf.getvalue(), file_name="hasil_ekualisasi_gray.png", mime="image/png")
