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


plt.ylim((0, 50))
#my_x_ticks = np.arange(1, 35, 1)
#plt.xticks(my_x_ticks)
x=list(range(0,351))
plt.plot(x,g4)
plt.show()