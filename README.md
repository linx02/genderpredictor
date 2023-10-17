# Gender Prediction using CNN

An image classifier machine learning project for gender prediction utilizing convolutional neural networks (CNN).
<iframe src="https://giphy.com/embed/SU2ic3wTfuC6JhD1lA" width="100" height="100" frameBorder="0"></iframe><iframe src="https://giphy.com/embed/LMt9638dO8dftAjtco" width="100" height="100" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

# Table of Contents

1. [Project Dataset](#project-dataset)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)
4. [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
   - [Epics](#epics)
   - [User Stories](#user-stories)
      1. [Data Collection and Preparation](#data-collection-and-preparation)
      2. [Data Visualization](#data-visualization)
      3. [Model Training, Optimization, and Evaluation](#model-training-optimization-and-evaluation)
      4. [Dashboard Planning, Designing, and Development and Deployment](#dashboard-planning-designing-and-development-and-deployment)
      5. [API Development and Deployment](#api-development-and-deployment)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
   - [Page 1: Home](#page-1-home)
   - [Page 2: Project Summary](#page-2-project-summary)
   - [Page 3: Data Visualization](#page-3-data-visualization)
   - [Page 4: Predict Gender](#page-4-predict-gender)
   - [Page 5: Hypothesis and Validation](#page-5-hypothesis-and-validation)
   - [Page 6: ML Metrics](#page-6-ml-metrics)
   - [Page 7: API](#page-7-api)
7. [Deployment](#deployment)
8. [Main Data Analysis & Machine Learning Libraries](#main-data-analysis--machine-learning-libraries)
9. [Run locally](#run-locally)
10. [Credits](#credits)

## Project Dataset
Dataset used provided by __Ashish Jangra__ under the __CC BY-NC-SA 4.0 license__.

Link to dataset: [Gender Classification 203K Images | CelebA](https://www.kaggle.com/datasets/ashishjangra27/gender-recognition-200k-images-celeba)
License Details: [CC BY-NC-SA 4.0 License Deed](https://creativecommons.org/licenses/by-nc-sa/4.0/)
Original source of dataset: [Large-scale CelebFaces Attributes (CelebA) Dataset](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets) and dataset consists of 200k+ images of peoples faces.

_I have not included the actual data in this repo, if you would like to inspect the dataset, please follow the steps in [Run locally](#run-locally) to download the dataset to your local machine._

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

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Epics:

- __Data collection and preparation__
- __Data visualization__
- __Model training, optimization and evaluation__
- __Dashboard planning, designing, and development and deployment__
- __API Development and deployment__

### User stories:

#### Data Collection and Preparation

1. **User Story:** As a developer, I can source and acquire the data to create a reliable and well-prepared dataset for the project.
   - **Task:** Download the dataset and extract the relevant data, save it in a new relevant folder structure.

#### Data Visualization

1. **User Story:** As a developer, I can generate informative visualizations to understand the data, providing valuable insights.
   - **Task:** Choose appropriate visualization techniques, generate visualizations and save them.

2. **User Story:** As a developer, I can integrate data visualizations into the dashboard for user-friendly data exploration.
   - **Task:** Design the layout and implement interactive features.

#### Model Training, Optimization, and Evaluation

1. **User Story:** As a developer, I can find the optimal hyperparamaters for my model in a set range of parameters.
   - **Task:** Find the optimal parameters using techniques such as Grid Search or Randomized Search.

2. **User Story:** As a developer, I can train and fine-tune the machine learning model based on the optimal hyperparameters found.
   - **Task:** Define model architecture and implement a function to build the model based on the found optimal hyperparameters.

3. **User Story:** As a developer, I can evaluate my models performance using a variety of metrics.
	- **Task:** Perform model evaluation using a Machine Learning library, visually represent the results and save the visualizations.

4. **User Story:** As a user, I can access model evaluation results, helping me understand the model's performance.
   - **Task:** Provide a user interface for accessing model evaluation reports.

#### Dashboard Planning, Designing, and Development and Deployment

1.  **User Story:** As a developer, I can implement Streamlit features, making it interactive and user-friendly. 
	-  **Task:** Develop and integrate interactive Streamlit features and functionalities into the dashboard.

2.  **User Story:** As a developer, I can deploy the Streamlit dashboard, ensuring it is accessible to users. 
	- **Task:** Deploy the streamlit app to Heroku and ensure the dashboard is accessible online.

3. **User Story:** As a user, I can access and interact with the deployed Streamlit app, enabling me to navigate through the project, explore data visualizations, and make live predictions on the model.
	-  **Task:** Provide navigation options, interactive data exploration features and a page for making live predictions with a way to download sample images for making predictions.

#### API Development and Deployment

1.  **User Story:** As a user, I can access the API in order to integrate the machine learning solution into my applications.
	-  **Task:** Develop an API and provide an endpoint for users to interact with the model.

2. **User Story:** As a user, I can access information for usage of the API in order to learn how to use it.
	- **Task:** Provide usage instructions along with example code on how to use the API inside the dashboard.


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

## API
As part of the business requirement _"The client is interested in an API in order to integrate the solution into their own applications"_, but also in order to tackle the slug size limitation set by Heroku, I developed a simple flask application to be able to interact with the model via POST requests. This app is hosted in a different Heroku app instance.

More information about the API can be found in [this GitHub repository](https://github.com/linx02/genderpredictor-api)

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

## Run locally

This repo covers the entire process of creating a ML model. From collecting and processing the data, to conducting hyperparameter optimization, data augmentation, defining and training the model on the data.

__To use this repo, follow these steps:__

1. Fork or clone this repository
2. Install dependencies by running:
	```bash
	pip install -r "requirements-dev.txt"
	```
3. Register an account with [Kaggle](https://www.kaggle.com/) and create a new API token, download the kaggle.json and place it in the projects root directory.
4. Run the notebooks in the jupyter_notebooks folder in the specified order.
	- __DataCollection.ipynb:__ Downloads the dataset and extracts specified number of images.
	- __DataVisualization.ipynb:__ Conducts studies on the data and saves insightful plots.
	- __Model.ipynb:__ Prepares data, performs data augmentation and hyperparameter optimization, defines model architecture, trains, evaluates and saves a ML model.
5. Start the web app by running:
	```bash
	streamlit run Home.py
	```
___If you encounter an error while importing opencv-python(cv2), run the following commands:___
```bash
sudo apt-get update
sudo apt-get install -y libgl1-mesa-dev
```

## Credits

[Churnometer repo by Code Institute](https://github.com/Code-Institute-Solutions/churnometer#readme): For the Readme template/structure.
[Streamlit documentation](https://docs.streamlit.io/): For getting the web app up and running.
[GIPHY](https://giphy.com/): For gifs in readme file