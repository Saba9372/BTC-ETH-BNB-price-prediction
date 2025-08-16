# BTC-ETH-BNB-price-prediction
Forecasting BTC, ETH, and BNB prices using a hybrid VMD-LSTM model. Automates technical analysis to predict next-day cryptocurrency prices, helping traders reduce risk and make informed decisions.
## Table of Contents
- Overview
- Dataset
- Methodology
- Results
- Installation
- Usage
- Future Work
- License
# Overview

Cryptocurrencies like Bitcoin (BTC), Ethereum (ETH), and Binance Coin (BNB) have created a rapidly evolving financial market due to their decentralized and borderless nature. Traders and investors face high volatility and require effective tools to make informed decisions. This project introduces a hybrid model combining **Variational Mode Decomposition (VMD)** and **Long Short-Term Memory (LSTM) networks** to forecast next-day prices of BTC, ETH, and BNB. By automating technical analysis, the model helps reduce trading risk and supports data-driven decision-making for cryptocurrency market participants.

This project explores time series forecasting techniques on cryptocurrency price data collected over several years:

Bitcoin: 7 years of historical data

Ethereum: 4 years of historical data

Binance Coin: 4 years of historical data

The goal is to implement and evaluate the performance of ARIMA, LSTM, and hybrid models to predict future cryptocurrency prices.

Data Sources

Cointelegraph

Yahoo Finance via yfinance Python library

All datasets include daily closing prices and have been preprocessed for modeling.

Models

ARIMA (AutoRegressive Integrated Moving Average)

Steps: Stationarity testing (ADF test), model identification (ACF/PACF), training, and forecasting.

Optimal parameters selected based on AIC/BIC and diagnostic checks.

LSTM (Long Short-Term Memory)

Steps: Data splitting, normalization (StandardScaler), network design, and training.

Hyperparameters tuned (e.g., number of epochs) to optimize performance.

Hybrid Decomposition-LSTM

Combines trend-seasonality decomposition with LSTM for improved prediction accuracy.

Implementation

Python and R were used for model implementation.

Python libraries include: pandas, numpy, yfinance, sklearn, tensorflow/keras.

R libraries include: forecast, tseries, ggplot2.

Code is modularized for easy replication and adaptation to other cryptocurrencies or financial time series.

Usage

Clone the repository:

git clone https://github.com/yourusername/crypto-forecasting.git


Install required packages:

pip install -r requirements.txt


Run individual model scripts (e.g., ARIMA.py, LSTM.py) to train and forecast.

Evaluate forecasts using MAE, MSE, and RMSE metrics.

Evaluation

The forecasting models are evaluated based on:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

Performance comparison tables are available in the results folder.

Technologies

Python

R

TensorFlow / Keras

scikit-learn

pandas & numpy

matplotlib & seaborn

License

This project is licensed under the MIT License. See the LICENSE file for details.
