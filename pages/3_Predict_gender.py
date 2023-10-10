# Import modules
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
import os

# Load model
model = load_model('model.h5')

# Page title
st.title('Predict Gender from image')

# File uploader
st.write('Upload image files (.jpg) and make predictions by presing the button')
uploaded_files = st.file_uploader("Choose a file...", type=["jpg"], accept_multiple_files=True)

if st.button("Predict"):
    # Check if file uploads not empty
    if len(uploaded_files) > 0:
        predictions = {}
        for image in uploaded_files:
            img_pil = Image.open(image)  # Open image using pillow
            # Process image for prediction
            resized_img = img_pil.resize((200, 200))  # Resize image
            img_array = np.array(resized_img)  # Convert to numpy array
            img_array = img_array / 255  # Normalize image
            img_array = np.expand_dims(img_array, axis=0)  # Reshape to (Sample size, 200, 200, 3)
            prediction = model.predict(img_array)  # Make prediction

            # If prediction = [smaller, bigger] (Male)
            if prediction[0][1] > prediction[0][0]:
                st.write('Predicted class: **Male**')
                predictions[image.name] = 'male'
            # If prediction = [bigger, smaller] (Female)
            elif prediction[0][1] < prediction[0][0]:
                st.write('Predicted class: **Female**')
                predictions[image.name] = 'female'
            # In the extremely rare case that predictions = [0.50, 0.50]
            elif prediction[0][1] == prediction[0][0]:
                st.write('Predicted class: **Unknown**')
                predictions[image.name] = 'unknown'

            # Show image
            st.image(img_pil)

            df_report = pd.DataFrame(predictions.items(), columns=['filename', 'prediction'])
            st.success('Analysis report')
            st.table(df_report)
            csv_data = df_report.to_csv(index=False)
            st.download_button("Download Report", csv_data, "report.csv", key='csv_download_button')
            
    else:
        st.error('No files uploaded')