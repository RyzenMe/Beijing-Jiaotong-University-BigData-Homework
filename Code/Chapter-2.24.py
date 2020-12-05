import numpy as np

def z_score(data):
    for i in range(len(data)):
        x_final = (data[i] - stock_mean) / stock_sd
        if x_final > 3.0 or x_final < -3.0:
            print('z_score离群值',data[i])

def IQR(data,data_ndarray):
    x_quartile = np.percentile(data_ndarray, (25,75), interpolation='midpoint')
    print(x_quartile)
    x_IQR = x_quartile[1] - x_quartile[0]
    for i in range(len(data)):
        if data[i] < x_quartile[0] -1.5 * x_IQR or data[i] > x_quartile[1] + 1.5 * x_IQR:
            print('IQR离群值',data[i])




if __name__ == '__main__':
    stock = [10, 7, 20, 12, 75, 15, 9, 18, 4, 12, 8, 14]
    stock_ndarray = np.array(stock)     #stock_ndarray 是ndarray格式
    stock_mean = np.mean(stock_ndarray)
    stock_median = np.median(stock_ndarray)
    stock_sd = np.std(stock_ndarray,ddof = 1)        #ddof = 1 表明计算的为无偏标准差，即除n-1



    z_score(stock)
    IQR(stock,stock_ndarray)

    stock_no = [10, 7, 20, 12, 15, 9, 18, 4, 12, 8, 14]
    stock_no_ndarray = np.array(stock_no)
    stock_no_mean = np.mean(stock_no_ndarray)
    print(stock_no_mean)
    stock_no_median = np.median(stock_no_ndarray)
    print(stock_no_median)