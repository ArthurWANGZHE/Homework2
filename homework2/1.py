import pandas as pd
import numpy as np

df_test = pd.read_csv('test.csv')
# 2800 rows * 784 columns (783个变量，1个序号）
df_train = pd.read_csv('train.csv')
# 42000 rows * 785 columns (783个变量，1个标签，1个序号）
df_answer = pd.read_csv('标准答案.csv')
# print(df_train)
df_test = np.array(df_test)
df_train = np.array(df_train)
df_answer = np.array(df_answer)
df_answer = np.array(df_answer)
def caculate_distance(test, train):
    dist = 0
    a = 0
    for i in range(783):
        s = (float(test[i]) - float(train[i + 1])) ** 2
        #   print(s)
        a += 1
        dist += s
    distance_ = (dist/783) ** 0.5
    print(distance_)
    return distance_

caculate_distance(df_test[0], df_train[0])