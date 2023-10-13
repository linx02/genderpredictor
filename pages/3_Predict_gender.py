# Import modules
import streamlit as st
from PIL import Image
import pandas as pd
import os
import requests

# Vars
ROOT_DIR = os.getcwd()
LIVE_PREDICTION_DIR = os.path.join(ROOT_DIR, 'assets', 'live_prediction_images.zip')

# Page title
st.title('Predict Gender from image')
st.info('This page aims to answer business requirement 1: "The client is interested in a machine learning solution to predict the gender of a person based on a picture of their face"')

# Allow users to download images

st.markdown("### Download images for live prediction")
with open(LIVE_PREDICTION_DIR, 'rb') as f:
   st.download_button('Download Zip', f, file_name='live_prediction_images.zip')

# File uploader
st.write('Upload image files (.jpg) and make predictions by presing the button')
uploaded_files = st.file_uploader("Choose a file...", type=["jpg"], accept_multiple_files=True)

if st.button("Predict"):
    # Check if file uploads not empty
    if len(uploaded_files) > 0:
        predictions = {}
        for image in uploaded_files:
            # Send image to API
            response = requests.post('https://gender-predictor-api-43d1edacb61c.herokuapp.com/predict', files={'file': image})
            # Save prediction
            predictions[image.name] = response.text
            st.write('Prediction: ', response.text)

            # Display image
            image = Image.open(image)
            st.image(image, caption='Uploaded Image.', use_column_width=False)

        df_report = pd.DataFrame(predictions.items(), columns=['filename', 'prediction'])
        st.success('Analysis report')
        st.table(df_report)
        csv_data = df_report.to_csv(index=False)
        st.download_button("Download Report", csv_data, "report.csv", key='csv_download_button')
            
    else:
        st.error('No files uploaded')