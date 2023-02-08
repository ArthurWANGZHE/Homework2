import pandas as pd

df = pd.read_excel("data.xlsx",header=None)
data = df.values.tolist()
wordlist = []
for i in range(0,358):
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
print(sorted(count.items(), key=lambda item: item[1], reverse=True))

print(len(count))
s=0
for i in range(0,28):
    s=s+count[i][1]

print(s)