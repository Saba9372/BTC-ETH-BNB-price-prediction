# 🪙 Cryptocurrency Price Prediction Using a Hybrid Learning Approach Based on VMD-LSTM Decomposition and Modeling (BTC, ETH, BNB)

## 📘 Project Overview
This project explores time series forecasting techniques on cryptocurrency price data, focusing on predicting future prices for major cryptocurrencies:

- **Bitcoin (BTC)** – 7 years of historical data  
- **Ethereum (ETH)** – 4 years of historical data  
- **Binance Coin (BNB)** – 4 years of historical data  

The project implements and evaluates a **VMD-LSTM (Variational Mode Decomposition with Long Short-Term Memory)** model to capture complex patterns in cryptocurrency prices.

### Key aspects include:
- Decomposition of time series into intrinsic mode functions using VMD  
- LSTM-based forecasting on decomposed components to improve prediction accuracy  
- Evaluation using metrics such as **MAE, MSE, and RMSE**  
- Comparison with other models like **ARIMA** and **standalone LSTM**  

The project uses **Python** and **R**, combining data preprocessing, modeling, and visualization to provide actionable insights into cryptocurrency price trends.

---

## 📊 Data Sources
- [Cointelegraph](https://cointelegraph.com/)  
- [Yahoo Finance](https://finance.yahoo.com/) via the `yfinance` Python library  

All datasets include daily closing prices and have been preprocessed for modeling.

---

## 🧠 Models

### 1. ARIMA (AutoRegressive Integrated Moving Average)
- Stationarity testing using **ADF test**  
- Model identification with **ACF** and **PACF** plots  
- Optimal parameters based on **AIC/BIC**

### 2. LSTM (Long Short-Term Memory)
- Data splitting and normalization with **StandardScaler**  
- Network design, training, and tuning  
- Performance optimization via hyperparameters (e.g., epochs)

### 3. VMD-LSTM (Hybrid Model)
- VMD decomposes the time series into intrinsic mode functions (IMFs)  
- Each IMF modeled using LSTM for detailed forecasting  
- Combines trend and high-frequency components for improved accuracy  

---

## ⚙️ Implementation
**Programming Languages:** Python & R  
**Python libraries:** `pandas`, `numpy`, `yfinance`, `sklearn`, `tensorflow/keras`  
**R libraries:** `forecast`, `tseries`, `ggplot2`

Code is modularized for easy replication and adaptation to other cryptocurrencies or financial time series.

---

## 💾 Clone the Repository
Download the project from GitHub to your computer:

```bash
git clone https://github.com/Saba9372/BTC-ETH-BNB-price-prediction.git
cd BTC-ETH-BNB-price-prediction

```

### 📦 Install Dependencies
Make sure you have Python 3.x installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

### 📂 Prepare Data
The scripts automatically download the required cryptocurrency data using the yfinance library. No manual CSV files are needed.

### Run Models

#### Run ARIMA model for Bitcoin:
```bash
python BTC-ARIMA.py
```

#### 🚀 Run LSTM model for Bitcoin :
```bash
python BTC-LSTM.py
```

Similarly, you can run other scripts (BNB-LSTM.py, BNB-ARIMA.py, etc.) depending on the asset and model you want.

### 📈 View Results

Each script will train the model and print evaluation metrics (e.g., MAPE, MSE).

Some scripts also generate plots showing predictions vs. actual values.

The results will either show in your terminal or pop up as graphs (via matplotlib).

## 🧮 Evaluation
Model performance is measured using:

- **MAE (Mean Absolute Error)** – average magnitude of errors
- **MSE (Mean Squared Error)** – penalizes larger errors
- **RMSE (Root Mean Squared Error)** – error in the same units as data

Performance comparison tables and charts are saved in the `results` folder.

## 📊 Results & Plots

- Forecasted vs. actual prices for Bitcoin, Ethereum, and Binance Coin  
- Error analysis plots for MAE, MSE, RMSE  
- VMD decomposition plots for LSTM  

Example:

![Bitcoin Forecast](results/bitcoin_forecast.png)

## 🧰 Technologies

- Python – data processing and modeling  
- R – statistical analysis  
- TensorFlow / Keras – LSTM modeling  
- scikit-learn – preprocessing and evaluation  
- pandas & numpy – data manipulation  
- matplotlib & seaborn – visualization

## 🪪 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


