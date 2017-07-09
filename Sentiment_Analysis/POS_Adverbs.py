import nltk
import csv
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

def pos_Adjectives(file1path,file2path):
    myfile = open(file2path, 'wb')
    writer = csv.writer(myfile, delimiter=',', lineterminator='\n')
    my_list = []
    t = []
    posts=[]
    data_list=[]
    with open(file1path, 'rb') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            posts.append([row])
        posts = sent_tokenize(str(posts))

    for sent in posts:
        data_list.append(sent)

    for sent in data_list:
        text=word_tokenize(sent)
        pos_text=nltk.pos_tag(text)
        for ss in pos_text:
            for s in ss:
                if(s=='RB'):
                 for i in ss:
                     if(i!= 'RB'):
                            my_list.append(i)
                            my_list=set(my_list)
                            my_list=list(my_list)
    for (words) in my_list:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        t.append((words_filtered))
        for w in words_filtered:
            writer.writerow([w])

file1='Resources/Data/Negative_Preprocessed.csv'
file2='Resources/Data/NegativeAdverbs.csv'
pos_Adjectives(file1,file2)

file3='Resources/Data/Positive_Preprocessed.csv'
file4='Resources/Data/PositiveAdverbs.csv'
pos_Adjectives(file3,file4)


















