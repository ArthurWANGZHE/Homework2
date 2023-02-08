import pandas as pd
import matplotlib.pyplot as plt

counts ={}
df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
wordlist = []
for i in range(0,351):
    word=data[i][2]
    a = (data[i][5]*7+data[i][6]*6+data[i][7]*5+data[i][8]*4+data[i][9]*3+data[i][10]*2+data[i][11])*data[i][3]/100
    wordlist.append(a)
print(wordlist)

import xlwt
f = xlwt.Workbook('encoding = utf-8') #设置工作簿编码
sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True) #创建sheet工作表
#要写入的列表的值
for i in range(len(wordlist)):
    sheet1.write(i,1,wordlist[i])
f.save('text.xls')#保存.xls到当前工作目录
