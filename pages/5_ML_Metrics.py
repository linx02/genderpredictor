import streamlit as st
import os
import pandas as pd

# Vars

ROOT_DIR = os.getcwd()
IMAGES_DIR = os.path.join(ROOT_DIR, 'assets', 'images')
IMAGE_PATHS = {
    'train_plot': os.path.join(IMAGES_DIR, 'metrics_over_epochs.png'),
    'eval_plot': os.path.join(IMAGES_DIR, 'evaluation_metrics.png'),
    'train_cm': os.path.join(IMAGES_DIR, 'train_cm.png'),
    'test_cm': os.path.join(IMAGES_DIR, 'test_cm.png'),
}

metrics = {
    'max_train_accuracy': 95.22,
    'max_val_accuracy': 95.44,
    'min_train_accuracy': 74.94,
    'min_val_accuracy': 64.78,
    'eval_accuracy': 92.94
}

st.title('Machine Learning Metrics')

st.info(f'''
The model was trained over 10 epochs, achieving:

* Peak accuracy of {metrics["max_train_accuracy"]}\% on the training data
* Peak accuracy of {metrics["max_val_accuracy"]}\% on the validation data
* Low accuracy of {metrics["min_train_accuracy"]}\% on the training data
* Low accuracy of {metrics["min_val_accuracy"]}\% on the validation data
* Accuracy of {metrics["eval_accuracy"]}\% on the test data
''')

st.success('Below are the metrics from the model training over epochs.')
st.image(IMAGE_PATHS['train_plot'], caption='Metrics from model training', use_column_width=True)

st.success('Below are the metrics from the model evaluation on the test data.')
st.image(IMAGE_PATHS['eval_plot'], caption='Metrics from model evaluation', use_column_width=True)

st.markdown('### Model performance')

st.success('Below are the confusion matrixes from model evaluation on the train and test data.')

st.image(IMAGE_PATHS['train_cm'], caption='Confusion matrix - train data', use_column_width=True)
st.image(IMAGE_PATHS['test_cm'], caption='Confusion matrix - test data', use_column_width=True)

st.success('Below are the classification reports from model evaluation on the train and test data.')

cr_train = pd.read_csv(os.path.join(ROOT_DIR, 'assets', 'train_cr.csv'))
st.table(cr_train)
cr_test = pd.read_csv(os.path.join(ROOT_DIR, 'assets', 'test_cr.csv'))
st.table(cr_test)