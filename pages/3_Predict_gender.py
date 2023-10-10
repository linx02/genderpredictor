import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

model = load_model('model.h5')

st.title('Predict Gender from image')

st.write('Upload image files and make predictions by presing the button')
uploaded_files = st.file_uploader("Choose a file...", type=["jpg", "png"], accept_multiple_files=True)

if st.button("Predict"):
    if uploaded_files is not None:
        for image in uploaded_files:
            img_pil = Image.open(image)
            st.info(f'Sample: **{image.name}**')

            resized_img = img_pil.resize((200, 200))
            img_array = np.array(resized_img)
            img_array = img_array / 255
            img_array = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_array)

            st.write(prediction)
    else:
        st.write('No files uploaded')
