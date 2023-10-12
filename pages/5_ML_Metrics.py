import streamlit as st
import os
import pandas as pd

# Vars

ROOT_DIR = os.getcwd()
IMAGES_DIR = os.path.join(ROOT_DIR, 'assets', 'images')
IMAGE_PATHS = {
    'train_plot': os.path.join(IMAGES_DIR, 'metrics_over_epochs.png'),
    'eval_plot': os.path.join(IMAGES_DIR, 'evaluation_metrics.png'),
    'confusion_matrix': os.path.join(IMAGES_DIR, 'confusion_matrix.png'),
}

metrics = {
    'max_train_accuracy': 95.22,
    'max_val_accuracy': 95.44,
    'min_train_accuracy': 74.94,
    'min_val_accuracy': 64.78,
    'eval_accuracy': 92.94
}

st.title('Machine Learning Metrics')

st.write(f'The model was trained over 10 epochs, achieving a peak accuracy of {metrics["max_train_accuracy"]}\% on the training data and {metrics["max_val_accuracy"]}\% on the validation data, with a minimum accuracy of {metrics["min_train_accuracy"]}\% on the training data and {metrics["min_val_accuracy"]}\% on the validation data.')
st.write(f'After evaluating the model on previously unseen test data, its accuracy was determined to be {metrics["eval_accuracy"]}\%')
st.info('Click the checkboxes below to view metric plots')

train_plot = st.checkbox("Show metrics from model training")
eval_plot = st.checkbox("Show metrics from model evaluation")
cm = st.checkbox("Show confusion matrix")
cr = st.checkbox("Show classification report")

if train_plot:
    st.image(IMAGE_PATHS['train_plot'], caption='Metrics from model training', use_column_width=True)
if eval_plot:
    st.image(IMAGE_PATHS['eval_plot'], caption='Metrics from model evaluation', use_column_width=True)
if cm:
    st.image(IMAGE_PATHS['confusion_matrix'], caption='Confusion matrix', use_column_width=True)
if cr:
    cr_file = pd.read_csv(os.path.join(ROOT_DIR, 'assets', 'classification_report.csv'))
    st.table(cr_file)