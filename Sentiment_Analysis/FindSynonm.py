import csv
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import re

file='Resources/Data/NegativeKeywords1.csv'
# myfile = open('../Resources/syn.csv', 'wb')
# writer = csv.writer(myfile, delimiter=',', lineterminator='\n')

with open(file,"r") as f:
    csvFileArray = []
    for row in csv.reader(f, delimiter = '.'):
        csvFileArray.append(row)
m=0
while m<csvFileArray.__len__():
    data=(csvFileArray[m])
    sent = ','.join(data)
    tokenize = word_tokenize(sent)
    i = 0
    while i < tokenize.__len__():
        synonyms = []
        for syn in wordnet.synsets(tokenize[i]):
            for l in syn.lemmas():
                synonyms.append(l.name())
        print synonyms
        j = i + 1
        while j < tokenize.__len__():
            k = 0
            while k < synonyms.__len__():
                if tokenize[j] == synonyms[k]:
                    sent = re.sub(tokenize[j], tokenize[i], sent)
                k = k + 1
            j = j + 1
        i = i + 1
    m=m+1

