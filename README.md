# Auction Verification System

This repository contains the **Auction Verification System**, designed to verify auction-related data using machine learning models. It helps in ensuring the authenticity and accuracy of auction bids and items.

## Features

- **Real-time Bid Verification**: Verifies auction bids in real-time.
- **Model Predictions**: Uses a pre-trained model to predict the legitimacy of auction data.
- **Interactive Interface**: Built with Streamlit for ease of use and interaction.

## Deployed Application

The Auction Verification System is publicly deployed. You can access the live version of the app here:

[**Auction Verification - Live Demo**](https://auction-verification.onrender.com)

Feel free to explore the deployed application to experience real-time auction verification.

## Model Training

The model used in this application was trained using historical auction data. The following steps were followed to train the model:

1. **Data Collection**: Collected and preprocessed auction-related data, including bids and item details.
2. **Model Selection**: Chose a machine learning model (e.g., `RandomForestClassifier`, `KNeighborsClassifier`, etc.) for classification.
3. **Training**: Trained the model using the training data and evaluated its performance.
4. **Model Serialization**: Once the model was trained, it was serialized using `pickle` or `joblib` for easy deployment.

If you wish to retrain the model or use it for further experiments, you can follow these steps:

### Retraining the Model

To retrain the model on your own data, run the following script:

```bash
python train_model.py
