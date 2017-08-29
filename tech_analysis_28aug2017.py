import pandas as pd
import matplotlib.pyplot as plt

stocks = pd.read_csv('tsla_3m_20jun.csv', parse_dates = ['date'])
stocks.drop(stocks.index[0], inplace = True) # removing random outlier dated august

ma_20 = [round(stocks['close'][i:i+30].mean(), 2) for i in xrange(len(stocks)-30)]
x_ma20 = stocks['date'][:34]

ma_50 = [round(stocks['close'][i:i+10].mean(), 2) for i in xrange(len(stocks)-10)]
x_ma50 = stocks['date'][:54]





fig = plt.figure(figsize = (15,5))
ax = fig.add_subplot(1,1,1)
ax.plot(stocks['date'], stocks['close'], 'black')
ax.plot(x_ma20, ma_20, 'b')
ax.plot(x_ma50, ma_50, 'g')
plt.show()
