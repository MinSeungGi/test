# -*- coding: cp949 -*-
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style


class Perceptron():
    def __init__(self, thresholds=0.0, eta=0.01, n_iter=10):
        self.thresholds = thresholds
        self.eta =eta
        self.n_iter = n_iter

    def fit(self, X,y):
        self.w_ = np.zeros(1+X.shape[1])
        self.errors_ =[]

        for _ in range(self.n_iter):
            errors=0
            for xi, target in zip(X,y):
                update = self.eta * (target-self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
                errors += int(update !=0.0)
            self.errors_.append(errors)
            print self.w_

        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) > self.thresholds, 1,-1)

if __name__ =='__main__':
    style.use('seaborn-talk')

    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

    y = df.iloc[0:100, 4].values
    y = np.where(y=='iris-setosa', -1,1)
    X = df.iloc[0:100, [0,2]].values

    plt.scatter(X[50, 0], X[:50,1], color='r', marker='o', label='setosa')
    plt.scatter(X[50:100,0], X[50:100,1], color ='b', marker='x', label ='versicolor')
    plt.xlabel('꽃잎 길이(cm)')
    plt.ylabel('꽃받침 길이(cm)')
    plt.legend(loc=4)
    plt.show()

    ppn=Perceptron(eta=0.1)
    ppn.fit(X,y)
    print ppn.errors_
    
