# Gender Prediction using CNN
An image classifier machine learning project for gender prediction utilizing convolutional neural networks (CNN).

## Project Dataset

The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets). The dataset consists of 200k+ images of peoples faces.
Link to dataset:  [Gender Classification 203K Images | CelebA](https://www.kaggle.com/datasets/ashishjangra27/gender-recognition-200k-images-celeba).
This dataset is licensed under: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
The original source of the data in the dataset used in this project can be found [here](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

_In order to respect the agreement in the above link, emphazising the following:_

"-   You agree **not to** further copy, publish or distribute any portion of the CelebA dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the dataset."

_I have not included the actual data in this repo, if you would like to inspect the dataset, please follow the steps in [LINK](link) to download the dataset to your local machine._

## Business requirements

The (fictional) business requirement story is as follows:

"A social media platform allows users to register their accounts with the profile information for the 'gender' field set to either 'Male,' 'Female,' or 'Other'.

Recently, the company has observed an increase in users registering or changing their profile information with the 'gender' field set to 'Other,' accompanied by a directly correlated decrease in advertisers on the site.

___The marketing team has proposed a possible explanation for this phenomenon:___
The platform's algorithm for personalizing advertisements becomes less efficient when users have their gender set to 'Other,' resulting in lower conversion rates for advertisements on the site. This has led advertisers to opt for other platforms to meet their marketing needs.

__The IT team has suggested a machine learning solution to provide the algorithm with a 'suggested' gender, aiming to enhance its efficiency while still respecting users' privacy and preferences.__"

_In short terms, the business requirements are the following:_

1. The client is interested in a machine learning solution to predict the gender of a person based on a picture of their face
2. The client is interested in a study of the data presented visually in order to understand the data better
3. The client is interested in an API in order to integrate the solution into their own applications

## Hypothesis and validation

__Hypothesis__: Men and women have gender-specific facial features that differentiate them.

__How to validate__: Conducting an average image study of the male and female face.

## ML Business Case

- We want an ML model to predict which gender the image of a face belongs to based on the image dataset provided. The target variable is categorical and contains 2-classes. We consider a  **classification model**. It is a supervised model, a 2-class, single-label, classification model which produces output: 0 (female) or 1 (male)
- Our aim is to have an accuracy of at least 75%
- Our ideal outcome is to provide the company with a dependable solution to provide their algorithm with reliable data.
- An API will be required for the company to integrate the solution into their platform in an automated way. The images will be gathered from profile pictures and posts made by users.

## Dashboard design (Streamlit App User Interface)

### Page 1: Home
-	Title
-	Link to GitHub profile
-	Link to GitHub repo

### Page 2: Project summary

- Project summary
	- General info
	- Project dataset
	- Business requirements

### Page 3: Data visualization

_Should answer business requirement 2: "The client is interested in a study of the data presented visually in order to understand the data better"_
- Show sample from available dataset
- Show label distribution
- Show average images and difference between average images

### Page 4: Predict gender

_Should answer business requirement 1: "The client is interested in a machine learning solution to predict the gender of a person based on a picture of their face"_

- Provide a download link for images of faces for live prediction
- Provide a file uploader and predict button to interact with the model
- Provide a download button for a report of the predictions

### Page 5: Hypothesis and validation
- State hypothesis
- State how to validate
- State how the hypothesis was validated

### Page 6: ML Metrics
- Provide metrics from model training presented visually
- Provide metrics from model evaluation presented visually
- Provide True Positives(TP), True Negatives(TN), False Positives(FN) and False Negatives(FN) from model evaluation presented visually
- Provide scikit-learns classification report from model evalutation

### Page 7: API
_Should answer business requirement 3: "The client is interested in an API in order to integrate the solution into their own applications"_
- Provide the API endpoint
- Provide instructions on how to use the API along with example code

## Deployment
This project was deployed to [Heroku](https://heroku.com/) using the following steps:
1.  Log in to Heroku and create an App
2.  At the Deploy tab, select GitHub as the deployment method.
3.  Select your repository name and click Search. Once it is found, click Connect.
4.  Select the branch you want to deploy, then click Deploy Branch.
5.  The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6.  If the slug size is too large then specify dependencies unnecessary for deployment by specifying your 'requirements.txt' and specify unnecessary files in a '.slugignore' in the root directory.

## Main Data Analysis & Machine Learning libraries
__Main Data analysis libraries used__:

- Numpy
	- For performing calculations on large amounts of data efficiently, mainly pixel data in this case
	- Normalizing pixel data
	- Calculating means and standard deviations
	- Base for other data analysis and ML libraries
- Pandas
	- Mainly for pandas DataFrame's for easy management of large data (sampling, shuffling, concatenation etc.)
- Matplotlib & Seaborn
	- For plotting and visualization of data
	- Showing images from pixel data
	- Metric plots & Histograms

__Main Machine Learning libraries used:__

- TensorFlow & Keras
	- Image augmentation
	- Model loading
	- Defining model architecture
	- Training model
	- One-hot encoding
	- tensorflow.data.Datset API
- Scikit Learn
	- Hyperparameter optimization using GridSearchCV
	- Generating confusion matrixes & classification reports
- OpenCV
	- Reading images pixel data as NumPy arrays
	- Resizing images
- Scikeras
	- For performing GridSearchCV on Keras models which is not compatible by default with scikit-learn. (KerasClassifier)

## Credits