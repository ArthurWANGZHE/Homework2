import random
ret = random.choice([0,1,-1])
print(ret)

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
t1=[]
t2=[]
t3=[]
t4=[]
t5=[]
t6=[]
t7=[]
for i in range(0,351):
    g1.append(data[i][5])
    s1 = data[i][5]+random.choice([0.1,1,-1])*random.uniform(0,1)
    if s1>0:
        t1.append(s1)
    else:
        t1.append(0)

    g2.append(data[i][6])
    s2 = data[i][6]+random.choice([0.1,1,-1])*random.uniform(0,5)
    if s2>0:
        t2.append(s2)
    else:
        t2.append(0)


    g3.append(data[i][7])
    s3 = data[i][7]+random.choice([0.1,1,-1])*random.uniform(0,5)
    if s3>0:
        t3.append(s3)
    else:
        t3.append(0)
    g4.append(data[i][8])
    s4 = data[i][8]+random.choice([0.1,1,-1])*random.uniform(0,5)
    if s4>0:
        t4.append(s4)
    else:
        t4.append(0)
    g5.append(data[i][9])
    s5 = data[i][9]+random.choice([0.1,1,-1])*random.uniform(0,5)
    if s5>0:
        t5.append(s5)
    else:
        t5.append(0)


    g6.append(data[i][10])
    s6 = data[i][10]+random.choice([0.1,1,-1])*random.uniform(0,5)
    if s6>0:
        t6.append(s6)
    else:
        t6.append(0)

    g7.append(data[i][11])
    s7 = data[i][11]+random.choice([0.1,1,-1])*random.uniform(0,5)
    if s7>0:
        t7.append(s7)
    else:
        t7.append(0)

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

plt.figure(figsize=(100, 5))
#plt.ylim((0, 50))
#my_x_ticks = np.arange(1, 35, 1)
#plt.xticks(my_x_ticks)
x=list(range(0,351))
plt.plot(x,g2)
plt.plot(x,t2)
plt.show()