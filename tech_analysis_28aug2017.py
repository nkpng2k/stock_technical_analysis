import pandas as pd
import matplotlib.pyplot as plt
import sklearn.ensemble as skle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

stocks = pd.read_csv('tsla_3m_20jun.csv', parse_dates = ['date'])
stocks.drop(stocks.index[0], inplace = True) # removing random outlier dated august

ma_20 = [round(stocks['close'][i:i+30].mean(), 2) for i in xrange(len(stocks)-30)]
x_ma20 = stocks['date'][:34]

ma_50 = [round(stocks['close'][i:i+10].mean(), 2) for i in xrange(len(stocks)-10)]
x_ma50 = stocks['date'][:54]

y = stocks.close.values
X = stocks.drop(['date','close'], axis = 1).values


X_train, X_test, y_train, y_test = train_test_split(X,y)


fig = plt.figure(figsize = (15,5))
ax = fig.add_subplot(1,1,1)
ax.plot(stocks['date'], stocks['close'], 'black')
ax.plot(x_ma20, ma_20, 'b')
ax.plot(x_ma50, ma_50, 'g')
plt.show()

stocks.volume = pd.to_numeric(stocks.volume)

gbr = skle.RandomForestRegressor(n_estimators = 500)
gbr.fit(X_train, y_train)

y_pred = gbr.predict(X_test)


fig = plt.figure(figsize = (15,5))
ax = fig.add_subplot(1,1,1)
ax.plot(range(len(y_pred)), y_pred, color = 'r')
ax.plot(range(len(y_test)), y_test, color = 'g')

plt.show()

mean_squared_error(y_test,y_pred)








"""
Bottom of Page
"""
