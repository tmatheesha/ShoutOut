import csv

neg_lex_path = 'Resources/negative-words.txt'
pos_lex_path = 'Resources/positive-words.txt'

neg_adj_path = 'Resources/Data/NegativeAdjectives.csv'
pos_adj_path = 'Resources/Data/PositiveAdjectives.csv'

neg_adverb_path = 'Resources/Data/NegativeAdverbs.csv'
pos_adverb_path = 'Resources/Data/PositiveAdverbs.csv'

negpost_file ='Resources/Data/Negative_Preprocessed.csv'
pospost_file ='Resources/Data/Positive_Preprocessed.csv'

myfile = open('Resources/Data/featureVector.csv', 'wb')
writer = csv.writer(myfile, delimiter=',', lineterminator='\n')

neg_fname='Resources/Data/NegativeKeywords.csv'
pos_fname='Resources/Data/PositiveKeywords.csv'

negative_fname='Resources/Data/NegativeKeywords1.csv'
positive_fname='Resources/Data/PositiveKeywords1.csv'

words_file = open('Resources/Data/features.csv', 'wb')
writer_words = csv.writer(words_file, delimiter=',', lineterminator='\n')

with open(neg_lex_path, 'r') as file1:
    with open(neg_adj_path, 'r') as file2:
        same = set(file1).intersection(file2)

with open(neg_fname, 'w') as file_out:
    for line in same:
        file_out.write(line)

with open(neg_lex_path, 'r') as file1:
    with open(neg_adverb_path, 'r') as file2:
        same = set(file1).intersection(file2)

with open(negative_fname, 'w') as file_out:
    for line in same:
        file_out.write(line)
neg_words = 0

with open(neg_fname, 'r') as f:
    for line in f:
        words = line.split()
        neg_words += len(line)

negative_words = 0

with open(negative_fname, 'r') as f:
    for line in f:
        words = line.split()
        negative_words += len(line)

with open(pos_lex_path, 'r') as file3:
    with open(pos_adj_path, 'r') as file2:
        same = set(file3).intersection(file2)

with open(pos_fname, 'w') as file_out:
    for line in same:
        file_out.write(line)

with open(pos_lex_path, 'r') as file3:
    with open(pos_adverb_path, 'r') as file2:
        same = set(file3).intersection(file2)

with open(positive_fname, 'w') as file_out:
    for line in same:
        file_out.write(line)

pos_words = 0

with open(pos_fname, 'r') as f:
    for line in f:
        words = line.split()
        pos_words += len(line)

positive_words = 0

with open(positive_fname, 'r') as f:
    for line in f:
        words = line.split()
        positive_words += len(line)

with open(neg_fname, 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    negList = []
    for row in reader:
        for w in row:
            negList.append(w)

with open(negative_fname, 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    negativeList=[]
    for row in reader:
        for w in row:
            negativeList.append(w)


with open(pos_fname, 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    posList = []
    for row in reader:
        for w in row:
            posList.append(w)

with open(positive_fname, 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    positiveList=[]
    for row in reader:
        for w in row:
            positiveList.append(w)

negation_words=['never','nobody','none','nothing','nowhere','not','no','neigher','nor']
sentiment=['Sentiment']
merge = negList + negativeList + posList + positiveList +  negation_words


unique_merge = []

for i in merge:
    if i not in unique_merge:
        unique_merge.append(i)
features=[]
# for w in unique_merge:
#     features.append(w)0
#     writer_words.writerow([w])

writer_words.writerow(unique_merge)

# writer.writerow(unique_merge+sentiment)

feature_vector=[]
neg=[0]
featureVector=[]
with open(negpost_file, "r") as f:
    reader = csv.reader(f, delimiter=",")
    csvfile = open(negpost_file, 'rb')
    csvFileArray = []
    for row in csv.reader(csvfile, delimiter='.'):
        csvFileArray.append(row)
i = 0
while i < csvFileArray.__len__():
    data = (csvFileArray[i])
    s = ','.join(data)
    wrd = s.split()
    j = 0
    mappingn = []
    while j < unique_merge.__len__():
        k = 0
        l = 0
        while k < wrd.__len__():
            if unique_merge[j] == wrd[k]:
                l = l + 1
            k = k + 1
        j = j + 1
        mappingn.append(l)
    nmap = []
    nmap = mappingn + neg
    writer.writerow(nmap)
    writer.writerow(nmap)
    i = i + 1

pos=[1]

with open(pospost_file, "r") as f:
    reader = csv.reader(f, delimiter=",")
    csvfile = open(pospost_file, 'rb')
    csvFileArray = []
    for row in csv.reader(csvfile, delimiter='.'):
        csvFileArray.append(row)
i = 0
while i < csvFileArray.__len__():
    data = (csvFileArray[i])
    s = ','.join(data)
    wrd = s.split()
    j = 0
    mappingp = []
    while j < unique_merge.__len__():
        k = 0
        l = 0
        while k < wrd.__len__():
            if unique_merge[j] == wrd[k]:
                l = l + 1
            k = k + 1
        j = j + 1
        mappingp.append(l)

    pmap = []
    pmap = mappingp + pos
    writer.writerow(pmap)
    writer.writerow(pmap)
    i = i + 1






