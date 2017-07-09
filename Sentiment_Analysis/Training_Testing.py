import csv
import random
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import numpy as np
import cPickle


file='Resources/Data/featureVector.csv'
with open(file, 'rb') as f:
    reader = csv.reader(f,delimiter=',')
    feature_vector = []
    for row in reader:
        feature_vector.append(row)
    random.shuffle(feature_vector)
    training_dataset = feature_vector[:(len(feature_vector) * 80 / 100)]
    testing_dataset = feature_vector[(len(feature_vector) * 80 / 100):]

    testing_data=[]
    for testingdata in testing_dataset:
        testingdata = list(map(int, testingdata))
        testing_data.append(testingdata[:-1])
    # print testing_data
    testing_labels = []
    for testinglabels in testing_dataset:
        testing_labels.append(testinglabels[-1])
    testing_labels = list(map(int, testing_labels))

    training_data=[]
    for trainingdata in training_dataset:
        trainingdata = list(map(int, trainingdata))
        training_data.append(trainingdata[:-1])
    training_labels=[]
    for traininglabels in training_dataset:
        training_labels.append(traininglabels[-1])
    training_labels = list(map(int, training_labels))

    a=[]
    a=training_data
    b=[]
    b=training_labels
    X = np.array(a)
    Y = np.array(b)

    model = GaussianNB()
    model.fit(X, Y)
    GaussianNB(priors=None)

    clf_pf = GaussianNB()
    clf_pf.partial_fit(X, Y, np.unique(Y))
    GaussianNB(priors=None)

    c=[]
    c=testing_data
    d=[]
    d=testing_labels
    print classification_report(d,model.predict(c))
    # print accuracy_score(d,model.predict(c))

    classifierNB='Resources/Data/NBclassifier.pkl'

    with open(classifierNB, 'wb') as fid:
        cPickle.dump(model, fid)

    from sklearn.svm import SVC
    clf = SVC()
    clf.fit(X, Y)

    print classification_report(d, clf.predict(c))

    classifierSVM = 'Resources/Data/SVMclassifier.pkl'

    with open(classifierSVM, 'wb') as fid:
        cPickle.dump(model, fid)
