import streamlit as st
import os

IMAGES_DIR = os.path.join(os.getcwd(), 'assets', 'images')
IMAGE_PATHS = {
    'train_plot': os.path.join(IMAGES_DIR, 'metrics_over_epochs.png'),
    'eval_plot': os.path.join(IMAGES_DIR, 'evaluation_metrics.png'),
}

st.title('Machine Learning Metrics')

st.write('The model was trained over 10 epochs, achieving a peak accuracy of 97.62\% on the training data and 91.11\% on the validation data, with a minimum accuracy of 78.57\% on the training data and 85.11\% on the validation data.')
st.write('After evaluating the model on previously unseen test data, its accuracy was determined to be 92.22\%')
st.info('Click the checkboxes below to view metric plots')

train_plot = st.checkbox("Show metrics from model training")
eval_plot = st.checkbox("Show metrics from model evaluation")

if train_plot:
    st.image(IMAGE_PATHS['train_plot'], caption='Metrics from model training', use_column_width=True)
if eval_plot:
    st.image(IMAGE_PATHS['eval_plot'], caption='Metrics from model evaluation', use_column_width=True)