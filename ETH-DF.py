

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:24:15 2022

@author: saba
"""
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import yfinance as yf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

df = yf.download('ETH-USD')

#diky-fuller
from statsmodels.tsa.stattools import adfuller
print("Observations of Dickey-fuller test")
dftest = adfuller(df['Close'],autolag='AIC')
dfoutput=pd.Series(dftest[0:4],index=['Test Statistic','p-value','#lags used','number of observations used'])
for key,value in dftest[4].items():
    dfoutput['critical value (%s)'%key]= value
print(dfoutput)
#diff
df_diff =df.diff(periods=1)
df_diff = df_diff[1:]
#diky-fuller
from statsmodels.tsa.stattools import adfuller
print("Observations of Dickey-fuller test")
dftest = adfuller(df_diff['Close'],autolag='AIC')
dfoutput=pd.Series(dftest[0:4],index=['Test Statistic','p-value','#lags used','number of observations used'])
for key,value in dftest[4].items():
    dfoutput['critical value (%s)'%key]= value
print(dfoutput)


plt.figure(figsize=(10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(df_diff['Adj Close'], 'green')
plt.legend()


plot_acf(df_diff['Close'], lags=10)
plot_pacf(df_diff['Close'], lags=10)
