import pandas as pd
import numpy as np


def z_score(data):
    for i in range(len(data)):
        x_final = (data[i] - stock_mean) / stock_sd
        if x_final > 3.0 or x_final < -3.0:
            print('z_score离群值',data[i],i)
            data.pop(i)
    print('z_score去除离群值后的极差',max(data)-min(data))


def IQR(data,data_ndarray):
    x_quartile = np.percentile(data_ndarray, (25,75), interpolation='midpoint')                 #求四分位点
    print(x_quartile)
    x_IQR = x_quartile[1] - x_quartile[0]
    for i in range(len(data)):
        if data[i] < x_quartile[0] -1.5 * x_IQR or data[i] > x_quartile[1] + 1.5 * x_IQR:
            print('IQR离群值',data[i],i)
            data.pop(i)                                 #将离群值去掉。
    print('IQR极差',max(data) - min(data))


if __name__ == '__main__':
    data = pd.read_csv('churn.txt')
    data_calls = data['CustServ Calls']
    stock_ndarray = np.array(data_calls)  # stock_ndarray 是ndarray格式
    stock_mean = np.mean(stock_ndarray)
    stock_median = np.median(stock_ndarray)
    stock_sd = np.std(stock_ndarray, ddof=1)  # ddof = 1 表明计算的为无偏标准差，即除n-1

    print('极差',max(data_calls)-min(data_calls))
    z_score(data_calls)

    data = pd.read_csv('churn.txt')                         #这里需要重新载入数据，因为在z_score中将数据更改了
    data_calls = data['CustServ Calls']
    IQR(data_calls,stock_ndarray)
    print(data.describe())