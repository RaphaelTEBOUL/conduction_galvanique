# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:44:49 2019

@author: tuoab
"""



from sklearn import svm, metrics

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

import pickle
import numpy as np
from sklearn.metrics import confusion_matrix


def load_data():
    

    input1 = pickle.load(open('data/1/input.pkl', 'rb'))
    input2 = pickle.load(open('data/2/input.pkl', 'rb'))
    input3 = pickle.load(open('data/3/input.pkl', 'rb'))
    input4 = pickle.load(open('data/4/input.pkl', 'rb'))
    
    inputs=np.concatenate((input1,input2,input3,input4) ,axis=0)
    
    target1 = pickle.load(open('data/1/targets.pkl', 'rb'))
    target2 = pickle.load(open('data/2/targets.pkl', 'rb'))
    target3 = pickle.load(open('data/3/targets.pkl', 'rb'))
    target4 = pickle.load(open('data/4/targets.pkl', 'rb'))
    
    targets=np.concatenate((target1, target2,target3,target4),axis = 0)
    
    return inputs, targets

def benchmark(clf):
    print('_' * 80)
    print("Training: ")
    print(clf)
    
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)

    score = metrics.accuracy_score(y_test, pred)
    print("Accuracy:   %0.3f" % score)

    if 1:
        print("classification report:")
        print(metrics.classification_report(y_test, pred))

    if 1:
        print("Confusion matrix:")
        print(metrics.confusion_matrix(y_test, pred))

    print('-'* 80)


classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

inputs, targets = load_data()

X_train, X_test, y_train, y_test = train_test_split(
   inputs, targets, test_size=0.33, random_state=42 , shuffle=True)


for clf in classifiers:
        benchmark(clf)
