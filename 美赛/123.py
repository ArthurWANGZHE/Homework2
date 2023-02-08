import pandas as pd
import matplotlib.pyplot as plt

counts =[]
df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
for i in range(0,355):
    word=list(data[i][2])
    nn=data[i][2]
    count = {}
    words = 0
    for i in word:
        if i not in count:
            count[i] = 1
            words += 1
        else:
            count[i] += 1
    counts.append(words)

print(counts)

import xlwt
f = xlwt.Workbook('encoding = utf-8') #设置工作簿编码
sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True) #创建sheet工作表
#要写入的列表的值
for i in range(len(counts)):
    sheet1.write(i,0,counts[i]) #写入数据参数对应 行, 列, 值
f.save('text.xls')#保存.xls到当前工作目录

