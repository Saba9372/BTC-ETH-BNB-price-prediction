# Cryptocurrency Price Forecasting

This project explores time series forecasting techniques on cryptocurrency price data collected over several years. It implements and evaluates ARIMA, LSTM, and hybrid models to predict future cryptocurrency prices.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Models](#models)
  - [ARIMA](#arima)
  - [LSTM](#lstm)
  - [Hybrid Decomposition-LSTM](#hybrid-decomposition-lstm)
- [Implementation](#implementation)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Technologies](#technologies)
- [License](#license)

## Project Overview
## Overview

Cryptocurrency markets are highly volatile, making accurate price forecasting critical for investors and analysts. This project explores:

- **Data Analysis**: Daily closing prices for Bitcoin (7 years), Ethereum (4 years), and Binance Coin (4 years).  
- **Forecasting Models**: Implementation of **ARIMA**, **LSTM**, and **Hybrid Decomposition-LSTM** models to predict future prices.  
- **Preprocessing Techniques**: Stationarity testing, trend-seasonality decomposition, normalization, and hyperparameter tuning.  
- **Evaluation**: Model performance assessed using **MAE**, **MSE**, and **RMSE**.  
- **Tools & Libraries**: Python (`pandas`, `numpy`, `yfinance`, `TensorFlow/Keras`), R (`forecast`, `tseries`, `ggplot2`).  
- **Goal**: Provide insights into cryptocurrency price trends and identify the most accurate forecasting approach.


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

### Hybrid Decomposition-LSTM
- Combines trend-seasonality decomposition with LSTM  
- Aims for improved prediction accuracy compared to standalone models  

## Implementation
- Programming Languages: Python and R  
- Python libraries: `pandas`, `numpy`, `yfinance`, `sklearn`, `tensorflow/keras`  
- R libraries: `forecast`, `tseries`, `ggplot2`  
- Code is modularized for easy replication and adaptation to other cryptocurrencies or financial time series  

## Usage
Clone the repository:
```bash
git clone https://github.com/yourusername/crypto-forecasting.git
cd crypto-forecasting
