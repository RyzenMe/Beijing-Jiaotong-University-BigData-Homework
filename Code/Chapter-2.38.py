import pandas as pd
import numpy as np

def skewness(data):
    x_skewness = 3*(stock_mean-stock_median)/stock_sd
    print(x_skewness)

if __name__ == '__main__':
    data = pd.read_csv('churn.txt')
    data_calls = data['Day Mins']
    stock_ndarray = np.array(data_calls)  # stock_ndarray 是ndarray格式
    stock_mean = np.mean(stock_ndarray)
    stock_median = np.median(stock_ndarray)
    stock_sd = np.std(stock_ndarray, ddof=1)  # ddof = 1 表明计算的为无偏标准差，即除n-1