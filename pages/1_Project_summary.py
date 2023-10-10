# Import streamlit
import streamlit as st

# Page title and text
st.title('Project Summary')

st.write('General info')
st.write('* lorem ipsum')

st.write('Project Dataset')
st.markdown('* The available dataset contains 3000 out of 200k+ images taken from the [Gender Classification 203K Images | CelebA](https://www.kaggle.com/datasets/ashishjangra27/gender-recognition-200k-images-celeba) dataset which is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).')

st.markdown('Additional information can be found on the projects README.md file which can be found [here](https://github.com/linx02/genderpredictor#readme)')

st.write('Business requirements')
st.write('* The client is interested in a machine learning solution to predict the gender of a person based on a picture of their face')
st.write('* The client is interested in a study of the data presented visually in order to understand the data better')