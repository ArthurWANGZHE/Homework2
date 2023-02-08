# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
g1=[]
g2=[]
g3=[]
g4=[]
g5=[]
g6=[]
g7=[]
n=[]
for i in range(0,351):
    g1.append(data[i][5])
    g2.append(data[i][6])
    g3.append(data[i][7])
    g4.append(data[i][8])
    g5.append(data[i][9])
    g6.append(data[i][10])
    g7.append(data[i][11])
    n.append(data[i][3]//1000)

"""
y=list(range(100))
plt.plot(g1,y)
plt.plot(g2,y)
plt.plot(g3,y)
plt.plot(g4,y)
plt.plot(g5,y)
plt.plot(g6,y)
plt.plot(g7,y)
plt.show()
"""



#my_x_ticks = np.arange(1, 35, 1)
#plt.xticks(my_x_ticks)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import BPNN
from sklearn import metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
df1=pd.read_excel('1234.xls',0)
df1=df1.iloc[:,:]
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
df0=min_max_scaler.fit_transform(df1)
df = pd.DataFrame(df0, columns=df1.columns)
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
cut=30

x_train, x_test=x.iloc[:-cut],x.iloc[-cut:]
y_train, y_test=y.iloc[:-cut],y.iloc[-cut:]
x_train, x_test=x_train.values, x.values
y_train, y_test=y_train.values, y.values


bp1 = BPNN.BPNNRegression([3, 16, 1])
train_data = [[sx.reshape(3,1), sy.reshape(1,1)] for sx, sy in zip(x_train, y_train)]
test_data = [np.reshape(sx, (3,1)) for sx in x_test]

bp1.MSGD(train_data, 1000, len(train_data), 0.2)

y_predict=bp1.predict(test_data)
y_pre = np.array(y_predict)
y_pre=y_pre.reshape(351,1)
y_pre=y_pre[:,0]

"""
draw=pd.concat([pd.DataFrame(y_test),pd.DataFrame(y_pre)],axis=1);
draw.iloc[:,0].plot(figsize=(12,6))
draw.iloc[:,1].plot(figsize=(12,6))
plt.legend(('real', 'predict'),loc='upper right',fontsize='15')
plt.title("Test Data",fontsize='30') #添加标题
"""

print('测试集上的MAE/MSE')
print(mean_absolute_error(y_pre, y_test))
print(mean_squared_error(y_pre, y_test) )
mape = np.mean(np.abs((y_pre-y_test)/(y_test)))*100
print('=============mape==============')
print(mape,'%')

print("R2 = ",metrics.r2_score(y_test, y_pre)) # R2
x= list(range(len(y_pre)))
xxx =[]
x4=[]
for i in range(len(y_pre)):
    a=y_pre[i]*100-g4[i]-20
    b=y_pre[i]*100-30
    xxx.append(a)
    x4.append(b)
print(xxx)
print(len(y_pre))
print(len(g4))
x=list(range(0,351))
print(xxx)

plt.subplot(221)

plt.plot(x,g4)
plt.subplot(222)

plt.plot(x,x4)
plt.show()
