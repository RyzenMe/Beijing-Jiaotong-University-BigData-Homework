import pandas as pd
import numpy as np


def z_score(data):
    data_final = []
    for i in range(len(data)):
        x_final = (data[i] - stock_mean) / stock_sd
        data_final.append(x_final)
#    data_final.to_excel(r"E:\1课程\研一\大数据\2.13-2.41\day mins的z_score归一化.xlsx")           list 不能直接用to_excel
    file = open('daymins的z_score归一化.txt', 'w')
    file.write(str(data_final))
    file.close()
    return data_final

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

    skewness(data_calls)
    data_z_score = z_score(data_calls)
    skewness(data_z_score)
