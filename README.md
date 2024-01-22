# EEG Seizure Prediction Flask App

## Project Overview
This Flask web application is designed to predict epileptic seizures using EEG (Electroencephalogram) data. It uses a Python backend with Flask to create an interactive platform where users can input EEG data and receive seizure predictions.

## Features
- EEG Data Visualization: Visualizes EEG signal data as plots.
- Seizure Prediction: Utilizes a predictive model to assess the likelihood of a seizure from EEG data.

## Prerequisites
- Python 3.x
- Flask
- Numpy
- Pandas
- Matplotlib
- A pre-trained seizure prediction model (`predict` function in `model.py`).

## Installation and Setup
1. Install Python 3.x and pip.
2. Install Flask, Numpy, Pandas, and Matplotlib:
   ```bash
   pip install Flask numpy pandas matplotlib
   ```
3. Set up the seizure prediction model in `model.py`.

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open `http://127.0.0.1:5000/` in a web browser.
3. Input the EEG data index (assumed to be a row index of a CSV file).
4. Submit to view the EEG signal plot and receive the seizure prediction.

## Code Structure
- `app.py`: The main Flask application file with routes and logic for data processing and prediction.
- `model.py`: Contains the `predict` and `base` functions for seizure prediction.
- `templates/index.html`: HTML template for the user interface.
- `static/`: Folder for storing generated EEG signal plots.

## Functionality Details
- The application reads EEG data from a CSV file (`Epileptic Seizure Recognition.csv`).
- Users submit an index, which corresponds to a row in the CSV file.
- The app visualizes the EEG signal for the specified index and uses the predictive model to assess seizure risk.
- The results, including the EEG signal plot and prediction, are displayed on the web page.

## Thank you
- Pianalytix for creating their Data Science Bundle course.
