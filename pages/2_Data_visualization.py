# Import modules
import streamlit as st
import matplotlib.pyplot as plt
import os

# Vars
IMAGES_DIR = os.path.join(os.getcwd(), 'assets', 'images')
IMAGE_PATHS = {
    'data_sample': os.path.join(IMAGES_DIR, 'data_sample.png'),
    'label_distribution' : os.path.join(IMAGES_DIR, 'label_distribution.png'),
    'avg_std_male' : os.path.join(IMAGES_DIR, 'data_avg_std_0.png'),
    'avg_std_female' : os.path.join(IMAGES_DIR, 'data_avg_std_1.png'),
    'diff_avg' : os.path.join(IMAGES_DIR, 'diff_avg_genders.png'),
}

# Page title
st.title('Data visualization')

# Page description
st.write('Here we will visualize the data in order to understand it better. Below are checkboxes to show different visualizations.')
st.info('This page aims to answer business requirement 2: "The client is interested in a study of the data presented visually in order to understand the data better"')

# Checkboxes
data_sample = st.checkbox("Show sample from dataset")
label_distribution = st.checkbox("Show label distribution")
avg_images = st.checkbox("Show average images")
diff_avg = st.checkbox("Show difference between genders average images")

# On checkbox click
if data_sample:
    st.image(IMAGE_PATHS['data_sample'], caption='Sample of 4 images of each label from the dataset.', use_column_width=True)
if label_distribution:
    st.image(IMAGE_PATHS['label_distribution'], caption='As represented, the dataset is distributed equally with 1500 images of each gender.', use_column_width=True)
if avg_images:
    st.image(IMAGE_PATHS['avg_std_male'], caption='The average and standard deviation image of label female, calculated from the entire dataset of 3000 images', use_column_width=True)
    st.image(IMAGE_PATHS['avg_std_female'], caption='The average and standard deviation image of label male, calculated from the entire dataset of 3000 images', use_column_width=True)
if diff_avg:
    st.image(IMAGE_PATHS['diff_avg'], caption='The difference of the average images of label male and female', use_column_width=True)