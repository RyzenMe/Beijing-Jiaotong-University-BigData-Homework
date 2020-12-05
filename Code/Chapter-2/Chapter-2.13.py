import numpy as np



def mean(data):
    sum = 0
    mean = 0
    for i in range(len(data)):
        sum = sum +data[i]
    mean = sum/(len(data))              #len(data)=12。range 是从0到11.
    return mean

def min_max(data):                      #max_min归一化
    x_max = max(data)
    x_min = min(data)
    print('中列数',(x_max+x_min)/2)
    x_final = (20 - x_min)/(x_max-x_min)
    print(x_final)

def x_score(data):                      #x分数归一化
    x_final = (20-mean(data))/stock_sd
    print(x_final)

def DecimalScaling(data):               #小数定标规范化
    x_max = max(data)
    for i in range(10):
        if x_max//10**i > 0:
            i+=1
        else:
            break
    x_decimal = 20/10**i
    print(x_decimal)

def skewness(data):
    x_skewness = 3*(mean(data)-stock_median)/stock_sd
    print(x_skewness)

if __name__ == '__main__':
    stock = [10, 7, 20, 12, 75, 15, 9, 18, 4, 12, 8, 14]

    mean_stock = mean(stock)
    print(mean_stock)                    #均值

    stock_ndarray = np.array(stock)     #stock_ndarray 是ndarray格式
    print(np.mean(stock_ndarray))        #均值
    stock_median = np.median(stock_ndarray)
    print(np.median(stock_ndarray))      #中位数
    counts = np.bincount(stock_ndarray)  #对[0,75]的数，进行一一映射，记录每个数出现的次数
    print(counts)
    print(np.argmax(counts))             #选择最大的计数，输出位置,众数

    stock_sd = np.std(stock_ndarray,ddof = 1)        #ddof = 1 表明计算的为无偏标准差，即除n-1
    print(stock_sd)

    min_max(stock)
    x_score(stock)

    DecimalScaling(stock)           #20的小数定标规范化数值

    skewness(stock)                 #数据倾斜度