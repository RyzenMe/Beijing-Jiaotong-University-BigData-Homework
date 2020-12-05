import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('churn.txt')             #读取文件

data['counter'] = range(len(data))      #新增自增列
a = range(len(data))
print(type(a))
print(data)
#print(data.tail())
#print(data.head())
#print(data.index)
print(data.describe())      #输出每一列的 计数 均值 方差 四分位点
data.plot.scatter(x='counter',y = 'CustServ Calls')
plt.show()