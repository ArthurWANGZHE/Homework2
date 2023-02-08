import numpy
import pandas as pd


def sigmoid (x):
    return 1/(1+numpy.exp(-x))

def der_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

def mse_loss(y_tr,y_pre):
    return((y_tr - y_pre)**2).mean()


class nerualnetwo():
    def __init__(self):
       self.w1 = numpy.random.normal()
       self.w2 = numpy.random.normal()
       self.w3 = numpy.random.normal()
       self.w4 = numpy.random.normal()
       self.w5 = numpy.random.normal()
       self.w6 = numpy.random.normal()
       self.b1 = numpy.random.normal()
       self.b2 = numpy.random.normal()
       self.b3 = numpy.random.normal()
    def feedforward(self,x):
        h1 = x[0]*self.w1+x[1]*self.w2+self.b1
        h1f = sigmoid(h1)
        h2 = x[0]*self.w3+x[1]*self.w4+self.b2
        h2f = sigmoid(h2)
        o1 = h1f*self.w5+h2f*self.w6+self.b3
        of = sigmoid(o1)
        return h1,h1f,h2,h2f,o1,of
    def simulate (self,x):
        h1 = x[0]*self.w1+x[1]*self.w2+self.b1
        h1f = sigmoid(h1)
        h2 = x[0]*self.w3+x[1]*self.w4+self.b2
        h2f = sigmoid(h2)
        o1 = h1f*self.w5+h2f*self.w6+self.b3
        of = sigmoid(o1)
        return of
    def train(self,data,all_y_tr):
        epochs = 1000
        learn_rate = 0.1
        for i in range(epochs):
            for x , y_tr in zip(data,all_y_tr):
                valcell = self.feedforward(x)
                y_pre = valcell[5]
                der_L_y_pre = -2*(y_tr-y_pre)
                der_y_pre_h1 = der_sigmoid(valcell[4])*self.w5
                der_y_pre_h2 = der_sigmoid(valcell[4])*self.w6
                der_h1_w1 = der_sigmoid(valcell[0])*x[0]
                der_h1_w2 = der_sigmoid(valcell[0])*x[1]
                der_h2_w3 = der_sigmoid(valcell[2])*x[0]
                der_h2_w4 = der_sigmoid(valcell[2])*x[1]
                der_y_pre_w5 = der_sigmoid(valcell[4])*valcell[1]
                der_y_pre_w6 = der_sigmoid(valcell[4])*valcell[3]
                der_y_pre_b3 = der_sigmoid(valcell[4])
                der_h1_b1 = der_sigmoid(valcell[0])
                der_h2_b2 = der_sigmoid(valcell[2])

                self.w1 -= learn_rate * der_L_y_pre * der_y_pre_h1 * der_h1_w1
                self.w2 -= learn_rate * der_L_y_pre * der_y_pre_h1 * der_h1_w2
                self.w3 -= learn_rate * der_L_y_pre * der_y_pre_h2 * der_h2_w3
                self.w4 -= learn_rate * der_L_y_pre * der_y_pre_h2 * der_h2_w4
                self.w5 -= learn_rate * der_L_y_pre * der_y_pre_w5
                self.w6 -= learn_rate * der_L_y_pre * der_y_pre_w6
                self.b1 -= learn_rate * der_L_y_pre * der_y_pre_h1 * der_h1_b1
                self.b2 -= learn_rate * der_L_y_pre * der_y_pre_h2 * der_h2_b2
                self.b3 -= learn_rate * der_L_y_pre *der_y_pre_b3
                if i % 10 ==0 :
                    y_pred = numpy.apply_along_axis(self.simulate,1,data)
                    loss = mse_loss (all_y_tr , y_pred)
                    print(i,loss)

counts = {}
df = pd.read_excel("data.xlsx", header=None)
data = df.values.tolist()
for i in range(0, 355):
    word = list(data[i][2])
    for item in word:
        if item not in counts:
            counts[item] = (data[i][5] * 7 + data[i][6] * 6 + data[i][7] * 5 + data[i][8] * 4 + data[i][9] * 3 +
                            data[i][10] * 2 + data[i][11]) * data[i][3] / 1000
        else:
            counts[item] += data[i][5] * 7 + data[i][6] * 6 + data[i][7] * 5 + data[i][8] * 4 + data[i][9] * 3 + \
                            data[i][10] * 2 + data[i][11] * data[i][3] / 1000
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
    ef = {word: data[i][4] / data[i][3] }
    l1.append(data[i][4] / data[i][3] )
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


data = numpy.array(l3)
all_y_trues = numpy.array(l1)
ner = nerualnetwo()

ner.train(data,all_y_trues)
test = numpy.array([5, 2])
print(ner.simulate(test))