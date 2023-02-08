# encoding:utf-8


import r123
import numpy as np


def sigmoid(x):

    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


class BPNNRegression:


    def __init__(self, sizes):

        self.num_layers = len(sizes)
        self.sizes = sizes

        self.biases = [np.random.randn(n, 1) for n in sizes[1:]]

        self.weights = [np.random.randn(r, c)
                        for c, r in zip(sizes[:-1], sizes[1:])]

    def feed_forward(self, a):
        for i, b, w in zip(range(len(self.biases)), self.biases, self.weights):
            if i == len(self.biases) - 1:
                a = np.dot(w, a) + b
                break
            a = sigmoid(np.dot(w, a) + b)
        return a

    def MSGD(self, training_data, epochs, mini_batch_size, eta, error=0.01):

        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batchs = [training_data[k:k + mini_batch_size]
                           for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batchs:
                self.updata_WB_by_mini_batch(mini_batch, eta)

            err_epoch = self.evaluate(training_data)
            print("Epoch {0} Error {1}".format(j, err_epoch))
            if err_epoch < error:
                break
            # if test_data:
            #     print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
            # else:
            # print("Epoch {0}".format(j))
        return err_epoch

    def updata_WB_by_mini_batch(self, mini_batch, eta):

        batch_par_b = [np.zeros(b.shape) for b in self.biases]
        batch_par_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_b, delta_w = self.back_propagation(x, y)
            batch_par_b = [bb + dbb for bb, dbb in zip(batch_par_b, delta_b)]
            batch_par_w = [bw + dbw for bw, dbw in zip(batch_par_w, delta_w)]
        self.weights = [w - (eta / len(mini_batch)) * dw
                        for w, dw in zip(self.weights, batch_par_w)]
        self.biases = [b - (eta / len(mini_batch)) * db
                       for b, db in zip(self.biases, batch_par_b)]

    def back_propagation(self, x, y):
        delta_b = [np.zeros(b.shape) for b in self.biases]
        delta_w = [np.zeros(w.shape) for w in self.weights]

        a = x

        activations = [x]

        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, a) + b
            zs.append(z)
            a = sigmoid(z)
            activations.append(a)
        # -------------
        activations[-1] = zs[-1]
        # -------------

        # delta = self.cost_function(activations[-1], y) * sigmoid_prime(zs[-1])
        delta = self.cost_function(activations[-1], y)  # 更改后
        # -------------
        delta_b[-1] = delta
        delta_w[-1] = np.dot(delta, activations[-2].T)
        for lev in range(2, self.num_layers):
            z = zs[-lev]
            zp = sigmoid_prime(z)
            delta = np.dot(self.weights[-lev + 1].T, delta) * zp
            delta_b[-lev] = delta
            delta_w[-lev] = np.dot(delta, activations[-lev - 1].T)
        return (delta_b, delta_w)

    def evaluate(self, train_data):
        test_result = [[self.feed_forward(x), y]
                       for x, y in train_data]
        return np.sum([0.5 * (x - y) ** 2 for (x, y) in test_result])

    def predict(self, test_input):
        test_result = [self.feed_forward(x)
                       for x in test_input]
        return test_result

    def cost_function(self, output_a, y):

        return (output_a - y)

    pass
