import streamlit as st

st.title('Hypothesis and Validation')

st.info('''
We suspect that men and women have gender-specific facial features that differentiate them.

* An average image study can help to investigate this hypothesis
''')

st.success('''
This hypothesis was validated by:

* Calculating 2 averages images from the available dataset. One image for the male gender and one for the female gender.
* Calculating an image for the difference between the averages by subtracting one of the images from the other in order to visually see the exact difference.
''')