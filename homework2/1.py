import pandas as pd
import numpy as np

df_test = pd.read_csv('test.csv')
# 2800 rows * 784 columns (783个变量，1个序号）
df_train = pd.read_csv('train.csv')
# 42000 rows * 785 columns (783个变量，1个标签，1个序号）
df_answer = pd.read_csv('标准答案.csv')
# print(df_train)

df_answer = np.array(df_answer)
answer = []
for i in range(28000):
    answer.append(df_answer[i][1])
print(answer)