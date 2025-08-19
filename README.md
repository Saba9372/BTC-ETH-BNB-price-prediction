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

## Usage

To replicate the project and run the forecasting models:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/crypto-forecasting.git
