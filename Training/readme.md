# Potato Disease Classification

This project involves developing a Convolutional Neural Network (CNN) model to detect diseases in potatoes. The model is deployed on a web server using FastAPI and hosted on Google Cloud Platform (GCP).

## Table of Contents
- Installation
- Usage
- Project Structure
- Model Training
- Deployment

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd Potato-Disease-Classification
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

2. **Access the web application:**
    Open your browser and go to `http://127.0.0.1:8000`.

## Project Structure


## Model Training

1. **Data Preparation:**
    - Collect and preprocess the potato disease images.
    - Split the data into training and validation sets.

2. **Model Development:**
    - Use TensorFlow and Keras to build the CNN model.
    - Train the model on the training data.
    - Evaluate the model on the validation data.

3. **Save the Model:**
    ```python
    model.save('model.keras')
    ```

## Deployment

1. **FastAPI Setup:**
    - Create a FastAPI application to serve the model.
    - Define API endpoints for image upload and disease prediction.

2. **Deploy on GCP:**
    - Use Google Cloud Platform to deploy the FastAPI application.
    - Ensure the application is accessible via a public URL.


