# Lung Cancer Prediction System

## Project Overview

The Lung Cancer Prediction System is a machine learning project that predicts a diagnosis class based on patient-related features such as age, gender, BMI, smoking status, genetic risk, physical activity, alcohol intake, and cancer history.

This project uses **Logistic Regression**, a supervised machine learning algorithm. The model is trained in Jupyter Notebook and deployed using Streamlit to provide a simple and interactive web application.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Model Training](#model-training)
- [Saving the Trained Model](#saving-the-trained-model)
- [Setting Up the Streamlit Application](#setting-up-the-streamlit-application)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Workflow](#project-workflow)
- [Future Enhancements](#future-enhancements)

## Features

- Predicts the diagnosis class using Logistic Regression.
- Uses eight patient-related input features.
- Checks for missing values and duplicate records.
- Splits the dataset into training and testing sets.
- Standardizes features using StandardScaler.
- Evaluates the model using accuracy, classification report, and confusion matrix.
- Saves the trained model as a `cancer_model.pkl` file.
- Provides a simple Streamlit interface for entering patient details.
- Displays predictions based on user inputs.

## Technologies Used

- **Python** – Programming language
- **Jupyter Notebook** – Data preprocessing and model training
- **Pandas** – Data loading and manipulation
- **Scikit-learn** – Logistic Regression, feature scaling, and model evaluation
- **Matplotlib** – Data visualization
- **Pickle** – Saving and loading the trained model
- **Streamlit** – Building the web application
- **PyCharm** – Developing and running the application

## Project Structure

```text
Lung-Cancer-Prediction/
│
├── LungCancerPrediction.csv
├── LungCancerPrediction.ipynb
├── cancer_model.pkl
├── app.py
└── README.md
```

### File Description

- **LungCancerPrediction.csv** – Contains the dataset used to train the model.
- **LungCancerPrediction.ipynb** – Contains the code for preprocessing, training, visualization, and model evaluation.
- **cancer_model.pkl** – Stores the trained machine learning pipeline generated after executing the notebook's model-saving cell.
- **app.py** – Contains the Streamlit code for collecting patient inputs and displaying predictions.
- **README.md** – Provides project information and setup instructions.

## Getting Started

### Prerequisites

Install Python, Jupyter Notebook, PyCharm, and the required libraries.

Install the libraries using:

```bash
pip install pandas scikit-learn matplotlib streamlit
```

## Model Training

The model is trained using Jupyter Notebook.

1. Open `LungCancerPrediction.ipynb`.
2. Load `LungCancerPrediction.csv` using Pandas.
3. Explore the dataset and handle missing values and duplicate records.
4. Separate the eight input features and the target column, `Diagnosis`.
5. Split the data into training and testing sets.
6. Apply `StandardScaler` to scale the input features.
7. Train the Logistic Regression model.
8. Generate predictions and evaluate the model using accuracy, classification report, and confusion matrix.

## Saving the Trained Model

After training the model, execute the following code in the last cell of your notebook:

```python
import pickle

with open("cancer_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
```

Here, `model` is the trained pipeline containing both `StandardScaler` and `LogisticRegression`.

After running this cell, `cancer_model.pkl` will be generated in the notebook's current working directory.

## Setting Up the Streamlit Application

1. Open PyCharm and create or open your project folder.
2. Run the Jupyter Notebook to train the model and generate `cancer_model.pkl`.
3. Locate the generated `cancer_model.pkl` file in the notebook's working directory.
4. Copy `cancer_model.pkl` into the same folder as `app.py`.
5. Create `app.py` and add the Streamlit interface code.
6. In `app.py`, load the saved model using Pickle.
7. Enter the patient details and click the **Predict** button to obtain the output.

**Important:** The `cancer_model.pkl` file must be generated first and placed in the same folder as `app.py`. Otherwise, the application cannot load the trained model.

## Running the Application

Open the terminal in PyCharm and execute:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to access the application.

## Usage

1. Train the model by running `LungCancerPrediction.ipynb`.
2. Generate `cancer_model.pkl`.
3. Copy the `cancer_model.pkl` file into the folder containing `app.py`.
4. Run the Streamlit application.
5. Enter all eight patient-related features.
6. Click the **Predict** button.
7. View the predicted diagnosis class.

The application loads the saved model and generates predictions without retraining it every time it starts.

## Project Workflow

**LungCancerPrediction.csv → LungCancerPrediction.ipynb → Data Preprocessing → Model Training → Generate `cancer_model.pkl` → Copy `cancer_model.pkl` File to the `app.py` Folder → Run Streamlit → Enter Patient Details → View Prediction**

## Future Enhancements

- Improve model performance through suitable feature selection and hyperparameter tuning.
- Display additional evaluation metrics.
- Add visualizations for exploring the dataset.
- Deploy the application online.

## Conclusion

The Lung Cancer Prediction System demonstrates the use of Logistic Regression to predict a diagnosis class from patient-related input features. The trained model is saved as a `.pkl` file and reused in a Streamlit application to provide predictions through a simple user interface.

This project provides practical experience in data preprocessing, model training, evaluation, model serialization, and application development.

**Disclaimer:** This project is for educational purposes only. Its predictions are not medical diagnoses and should not be used for clinical decisions.
