# Import streamlit
import streamlit as st

# Page title and text
st.title('Project Summary')

st.info('''
__General info__
* In order to respect the privacy of users, as well as to apply to a broader group of people, businesses often allow users to register to their sites with gender information outside of the male/female binary.

_Gender data is commonly used in the following ways:_
1. Analysis of user data in order to understand the userbase better.
2. Personalization of user experience in order to provide a more tailored experience to the user.
3. Personalization of advertisements in order to increase the effectiveness of the advertisement.''')

st.success('''
__Project Dataset__
* The available dataset is sourced from [Kaggle](https://www.kaggle.com/datasets) and contains 3000 out of 200k+ images taken from the [Gender Classification 203K Images | CelebA](https://www.kaggle.com/datasets/ashishjangra27/gender-recognition-200k-images-celeba) dataset which is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
* The original source of this dataset is the [CelebA dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
''')

st.markdown('__Additional information can be found on the projects README.md file which can be found [here](https://github.com/linx02/genderpredictor#readme)__')

st.warning('''
__Business requirements__
1. The client is interested in a machine learning solution to predict the gender of a person based on a picture of their face
2. The client is interested in a study of the data presented visually in order to understand the data better
3. The client is interested in an API in order to integrate the solution into their own applications
''')