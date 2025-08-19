# Cryptocurrency Price Forecasting

This project explores time series forecasting techniques on cryptocurrency price data collected over several years. It implements and evaluates ARIMA, LSTM, and hybrid models to predict future cryptocurrency prices.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Models](#models)
  - [ARIMA](#arima)
  - [LSTM](#lstm)
  - [VMD-LSTM](#VariationalModeDecomposition+LSTM)
- [Implementation](#implementation)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Technologies](#technologies)
- [License](#license)

## Project Overview

This project explores **time series forecasting techniques** on cryptocurrency price data, focusing on predicting future prices for major cryptocurrencies:

- **Bitcoin** – 7 years of historical data  
- **Ethereum** – 4 years of historical data  
- **Binance Coin** – 4 years of historical data  

The project implements and evaluates a **VMD-LSTM (Variational Mode Decomposition with Long Short-Term Memory)** model to capture complex patterns in cryptocurrency prices. Key aspects include:

- **Decomposition of time series** into intrinsic mode functions using **VMD**  
- **LSTM-based forecasting** on decomposed components to improve prediction accuracy  
- **Evaluation of performance** using metrics such as **MAE, MSE, and RMSE**  
- **Comparison with other models** like ARIMA and standalone LSTM to demonstrate the advantages of the hybrid approach  

The project uses **Python and R**, combining data preprocessing, modeling, and visualization to provide actionable insights into cryptocurrency price trends.



## Data Sources
- [Cointelegraph](https://cointelegraph.com)   
- **Yahoo Finance** via the `yfinance` Python library  

All datasets include daily closing prices and have been preprocessed for modeling.

## Models

### ARIMA (AutoRegressive Integrated Moving Average)
- Stationarity testing using ADF test  
- Model identification using ACF and PACF plots  
- Training and forecasting  
- Optimal parameters selected based on AIC/BIC and diagnostic checks  

### LSTM (Long Short-Term Memory)
- Data splitting and normalization (`StandardScaler`)  
- Network design and training  
- Hyperparameter tuning (e.g., number of epochs) to optimize performance  

### VMD-LSTM (Variational Mode Decomposition + LSTM)

- VMD decomposes the original time series into intrinsic mode functions
- Each mode is modeled using LSTM for more accurate predictions
- Combines trend and high-frequency components to improve forecasting performance

## Implementation
- Programming Languages: Python and R  
- Python libraries: `pandas`, `numpy`, `yfinance`, `sklearn`, `tensorflow/keras`  
- R libraries: `forecast`, `tseries`, `ggplot2`  
- Code is modularized for easy replication and adaptation to other cryptocurrencies or financial time series  

## Clone the Repository
Download the project from GitHub to your computer:

git clone https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git
cd YOUR_PROJECT_NAME


Install Dependencies
Make sure you have Python 3.x installed, then install the required libraries:

pip install -r requirements.txt


(You’ll need to create a requirements.txt later — I can help with that if you don’t have it yet.)

Prepare Data
Place the CSV files (e.g., BTC-Total.csv, BTC-Test.csv, BNB-Total.csv, etc.) in the project folder.
These files are required for the models to run.

Run Models

To run ARIMA model for Bitcoin:

python BTC-ARIMA.py



### Run LSTM model for Ethereum

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saba9372/BTC-ETH-BNB-price-prediction/blob/main/ETH-LSTM.py)




Similarly, you can run other scripts (BNB-LSTM.py, BNB-ARIMA.py, etc.) depending on the asset and model you want.

View Results

Each script will train the model and print evaluation metrics (e.g., MAPE, MSE).

Some scripts also generate plots showing predictions vs. actual values.

The results will either show in your terminal or pop up as graphs (via matplotlib).

## Evaluation
Model performance is measured using:

- **MAE (Mean Absolute Error)** – average magnitude of errors
- **MSE (Mean Squared Error)** – penalizes larger errors
- **RMSE (Root Mean Squared Error)** – error in the same units as data

Performance comparison tables and charts are saved in the `results` folder.

## Results & Plots

- Forecasted vs. actual prices for Bitcoin, Ethereum, and Binance Coin  
- Error analysis plots for MAE, MSE, RMSE  
- VMD decomposition plots for LSTM  

Example:

![Bitcoin Forecast](results/bitcoin_forecast.png)

## Technologies

- Python – data processing and modeling  
- R – statistical analysis  
- TensorFlow / Keras – LSTM modeling  
- scikit-learn – preprocessing and evaluation  
- pandas & numpy – data manipulation  
- matplotlib & seaborn – visualization

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


