# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:20:54 2022

@author: saba
"""


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error


df = yf.download('ETH-USD')
plt.plot(df.index, df['Adj Close'])


# Train Test Split

to_row = int(len(df)*0.85)

training_data = list(df[0:to_row]['Adj Close'])
testing_data = list(df[to_row:]['Adj Close'])

# split data into train and training set

plt.figure(figsize=(10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(df[0:to_row]['Adj Close'], 'green', label='Train data')
plt.plot(df[to_row:]['Adj Close'], 'blue', label='Test data')
plt.legend()

model_predictions = []
n_test_obser = len(testing_data)


for i in range(n_test_obser):
    model = ARIMA(training_data, order=(3, 1, 2))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = list(output[0])[0]
    model_predictions.append(yhat)
    actual_test_value = testing_data[i]
    training_data.append(actual_test_value)
   


model_fit.summary()

plt.figure(figsize=(10,6))
plt.grid(True)
    
date_range = df[to_row:].index

plt.plot(date_range,model_predictions,color='blue',marker='o',linestyle='dashed',label='ETH Predicted Price')
plt.plot(date_range,testing_data,color='red',label='ETH Actual Price')

plt.title('ETH Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

mape=np.mean(np.abs(np.array(model_predictions)-np.array(testing_data))/np.abs(testing_data))*10
print('MAPE: '+str(mape))
