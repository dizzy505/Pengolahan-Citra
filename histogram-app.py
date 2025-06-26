import streamlit as st
import cv2

st.set_page_config(page_title='Pengolahan Citra', layout='wide')
st.header("Pengolahan Citra")

mode = st.selectbox("PIlih Operasi", ('RGB', 'Negasi'))

zzz = cv2.imread('img/zzz.png')

col1, col2 = st.columns([0.5,0.5])
with col1:
    st.image(zzz, channels='BGR', use_container_width=True)
with col2:
    if mode == 'RGB':
        st.image(zzz, channels='BGR', use_container_width=True)
    if mode == 'Negasi':
        negasi = 255 - zzz
        st.image(negasi, channels='BGR', use_container_width=True)
