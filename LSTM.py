# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:01:24 2022

@author: saba
"""

import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense , Dropout
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import math

df = pd.read_csv('BTC-Total.csv')
#datatest=pd.read_csv('Test.csv')
#Seprate dates for future plotting
train_dates= pd.to_datetime(df['date'])

#Variables for Training
cols = list(df)[1:6]

df_for_training=df[cols].astype(float)

df_for_plot=df_for_training.tail(850)
df_for_plot.plot.line()

#data normalized
scaler = StandardScaler()
scaler = scaler.fit(df_for_training)
df_for_training_scaled=scaler.transform(df_for_training)


#reshape
trainX=[]
trainY=[]

n_future=1
n_past=14

for i in range(n_past,len(df_for_training_scaled)-n_future+1):
    trainX.append(df_for_training_scaled[i-n_past:i,0:df_for_training.shape[1]])
    trainY.append(df_for_training_scaled[i+n_future - 1:i+n_future,0])
    
    
trainX , trainY = np.array(trainX),np.array(trainY)
  

#defice LSTM model
model=Sequential()
model.add(LSTM(64,activation='relu',input_shape=(trainX.shape[1],trainX.shape[2]),return_sequences=True))
model.add(LSTM(32,activation='relu',return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(trainY.shape[1]))

model.compile(optimizer='adam',loss='mse')
model.summary()

history=model.fit(trainX,trainY,epochs=20,batch_size=16,validation_split=0.1,verbose=1)

#forcasting
n_future=30

forecast_period_dates=pd.date_range(list(train_dates)[-1],periods=n_future,freq='1d').tolist()
forecast= model.predict(trainX[-n_future:])

forecast_copies=np.repeat(forecast,df_for_training.shape[1],axis=-1)
y_pred_future = scaler.inverse_transform(forecast_copies)[:,0]

forecast_dates = []
for time_i in forecast_period_dates:
    forecast_dates.append(time_i.date())

df_forecast = pd.DataFrame({'date':np.array(forecast_dates),'close':y_pred_future})
df_forecast['date']=pd.to_datetime(df_forecast['date'])






#mape
test = pd.read_csv('BTC-Test.csv')
cols1 = list(test)[0:1]
test_for_normalize=test[cols1].astype(float)


#mse 30 days forecast
array1 = np.array(test_for_normalize)
array2 = np.array(y_pred_future)



mape=np.mean((np.abs(array2-array1))/np.abs(array1))
print('MAPE: '+str(mape))







