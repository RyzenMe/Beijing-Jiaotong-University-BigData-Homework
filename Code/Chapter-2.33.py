import pandas as pd
import numpy as np

data = pd.read_csv('churn.txt')             #读取文件
print(np.NaN)                               #np.nan  意思not a number
data = data.replace('null',np.NaN)          #将数据中null值，全换成np.NaN
data_null = data.isnull().any()             #统计每一列是否有缺失值
b = data.isnull().any().sum()               #统计每一列缺失值个数
print(data_null)
print(b)


data_new = data.groupby(['State'])['Area Code'].nunique()       #nunique返回不同的个数.由于groupby 是pandas下的  应该默认是pandas下的unique
print(data_new)
data_new1 = data.groupby(['State'])['Area Code'].unique()       #.groupby 会按照state进行分组，没有任何运算返回groupby对象，可再取出area code 这一列进行操作。.unique去除重复，返回无重复的元组或者列表
print(data_new1)

data_new2 = data.groupby(['Area Code'])['State'].unique()
print(type(data_new2))
data_new2.to_excel(r"E:\1课程\研一\大数据\2.13-2.41\areacode结果.xlsx")      #输出excel,<class 'pandas.core.series.Series'>
data_new3 = data.groupby(['Area Code'])['State'].nunique()
print(data_new3)
