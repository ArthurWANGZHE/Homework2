import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

counts ={}
df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
for i in range(0,351):
    word=list(data[i][2])
    for item in word:
        if item not in counts:
            counts[item] = (data[i][5]*7+data[i][6]*6+data[i][7]*5+data[i][8]*4+data[i][9]*3+data[i][10]*2+data[i][11])*data[i][3]/100
        else:
            counts[item] += data[i][5]*7+data[i][6]*6+data[i][7]*5+data[i][8]*4+data[i][9]*3+data[i][10]*2+data[i][11]*data[i][3]/100
wordlist = []
for i in range(0,351):
    wordlist.append(data[i][2])
list_message=[]
for item in wordlist:
    list_message +=list(item)

count = {}
for i in list_message:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
zmdf={" ":0}
for i in list("abcdefghijklmnopqrstuvwxyz"):
    score = {i:counts[i]/count[i]//10}
    zmdf.update(score)
print(zmdf)
# 加权平均
jiaquan = []
for i in range(0,351):
    word=list(data[i][2])
    sc = 0
    for item in word:
        sc += zmdf[item]
        jiaquan.append(sc)



#元音
answ ={}
yygs = []
for i in range(0,351):
    words=data[i][2]
    ys ={}
    yy = 0
    word = list(words)
    for item in word :
        if item in ["a","e","i","o","u",]:
            yy +=1
        ys = {words:yy}
    answ.update(ys)
    yygs.append(yy)

#hard占比
efs = {}
for i in range(0, 351):
    word = data[i][2]
    ef = {word: data[i][4] / data[i][3] * 100}
    efs.update(ef)

#字母个数
counts =[]
zmgs = []
df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
for i in range(0,351):
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


g1=[]
g2=[]
g3=[]
g4=[]
g5=[]
g6=[]
g7=[]
for i in range(0,351):
    g1.append(data[i][5])
    g2.append(data[i][6])
    g3.append(data[i][7])
    g4.append(data[i][8])
    g5.append(data[i][9])
    g6.append(data[i][10])
    g7.append(data[i][11])

print(jiaquan)
print(yygs)
print(counts)
print(g1)

jiaquan_ = []
for i in range(len(yygs)):
    re = [int(jiaquan[i])]
    jiaquan_.append(re)


