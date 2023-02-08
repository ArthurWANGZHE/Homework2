import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

counts = {}
df = pd.read_excel("data.xlsx", header=None)
data = df.values.tolist()
for i in range(0, 355):
    word = list(data[i][2])
    for item in word:
        if item not in counts:
            counts[item] = (data[i][5] * 7 + data[i][6] * 6 + data[i][7] * 5 + data[i][8] * 4 + data[i][9] * 3 +
                            data[i][10] * 2 + data[i][11]) * data[i][3] / 100
        else:
            counts[item] += data[i][5] * 7 + data[i][6] * 6 + data[i][7] * 5 + data[i][8] * 4 + data[i][9] * 3 + \
                            data[i][10] * 2 + data[i][11] * data[i][3] / 100
wordlist = []
for i in range(0, 355):
    wordlist.append(data[i][2])
list_message = []
for item in wordlist:
    list_message += list(item)

count = {}
for i in list_message:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
fl = {" ": 0}
for i in list("abcdefghijklmnopqrstuvwxyz"):
    score = {i: counts[i] / count[i] // 100}
    fl.update(score)

ans = {}
for i in range(0, 355):
    word = list(data[i][2])
    sc = 0
    for item in word:
        sc += fl[item]
    fls = {data[i][2]: sc}
    ans.update(fls)

efs = {}
l1 = []
for i in range(0, 355):
    word = data[i][2]
    ef = {word: data[i][4] / data[i][3] * 100}
    l1.append(data[i][4] / data[i][3] * 100)
    efs.update(ef)

answ = {}
l2 = []
for i in range(0, 355):
    words = data[i][2]
    ys = {}
    yy = 0
    word = list(words)
    for item in word:
        if item in ["a", "e", "i", "o", "u", ]:
            yy += 1
        ys = {words: yy}
    answ.update(ys)
    l2.append((yy))

counts = []
df = pd.read_excel("data.xlsx", header=None)
data = df.values.tolist()
for i in range(0, 355):
    word = list(data[i][2])
    nn = data[i][2]
    count = {}
    words = 0
    for i in word:
        if i not in count:
            count[i] = 1
            words += 1
        else:
            count[i] += 1
    counts.append(words)


l3 = []
for i in range(len(counts)):
    l=[counts[i],l2[i]]
    l3.append(l)

print(l3)
print(l1)