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
The project focuses on forecasting cryptocurrency prices:

- **Bitcoin**: 7 years of historical data  
- **Ethereum**: 4 years of historical data  
- **Binance Coin**: 4 years of historical data  

The main goal is to implement, compare, and evaluate ARIMA, LSTM, and hybrid models for predicting cryptocurrency prices.

## Data Sources
- **Cointelegraph**  
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
