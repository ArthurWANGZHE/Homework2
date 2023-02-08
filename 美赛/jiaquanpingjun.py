import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


counts ={}
df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
wordlist = []
for i in range(0,351):
    a = data[i][5]*1+data[i][6]*2+data[i][7]*3+data[i][8]*4+data[i][9]*5+data[i][10]*6+data[i][11]*7
    wordlist.append(a)

import xlwt
f = xlwt.Workbook('encoding = utf-8')
sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True)
for i in range(len(wordlist)):

    sheet1.write(i,0,wordlist[i])
f.save('text.xls')



