import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()

y=[]
for i in range(0,358):
    y.append(data[i][3] // 1000)

x=list(range(0,358))

