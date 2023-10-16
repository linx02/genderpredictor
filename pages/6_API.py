import streamlit as st

# Page title and text
st.title('API')
st.info('This page aims to answer business requirement 3: "The client is interested in an API in order to integrate the solution into their own applications"')
st.markdown('__Link to the GitHub repository for the API can be found [here](https://github.com/linx02/genderpredictor-api)__')

st.info('API endpoint: https://gender-predictor-api-43d1edacb61c.herokuapp.com/predict')

st.success('''
To use the Gender Prediction API, you can send a POST request containing an image file to the provided endpoint.
The API will process the image and return a prediction of the gender ('male' or 'female') in JSON format.
Below are the steps to interact with the API:
''')

st.markdown('''
### Usage

* Send a POST request to the endpoint with an image file using the multipart/form-data content type.

__Example using cURL:__

```bash
curl -X POST -F "file=@path/to/your/image.jpg" https://gender-predictor-api-43d1edacb61c.herokuapp.com/predict
```

* Upon successful processing of the image, the API will respond with a JSON object containing the predicted gender.
* The response will include a 'gender' key with a value of either 'male' or 'female'.

__Example response:__

```json
{
    "gender": "female"
}
```

''')