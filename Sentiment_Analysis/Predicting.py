import csv
from nltk.corpus import stopwords
import re
import string
import cPickle
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk import pos_tag
lemmatizer = WordNetLemmatizer()
from nltk import ngrams


neg_lex_path = 'Resources/negative-words.txt'
pos_lex_path = 'Resources/positive-words.txt'

NAIVEBAYES = "NaiveBayes"
SVM = "SVM"
RULEBASED = "RuleBased"
POSITIVE = "Positive"
NEGATIVE = "Negative"

# sent="not a Good thoughts. Instead of deferring to the one that was asked first, would it make never more sense to migrate some of" \
#      " the Sci Fi questions if they fit better on Movies (according to criteria 2-4)? Has that ever been done before? " \
#      "(Migrating questions after a not new site is created and is a better fit for questions asked elsewhere)"

def predictPost(sent):
    sent = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', sent)
    sent = re.sub('<[^>]*>', '', sent)
    sent = re.sub(":\)", 'happy', sent)
    sent = re.sub(":\-\)", 'happy', sent)
    sent = re.sub(":D", 'very happy', sent)
    sent = re.sub(":\(", 'sad', sent)
    sent = re.sub(":\-\(", 'sad', sent)
    sent = re.sub("\(y\)", 'great', sent)
    sent = re.sub("\(Y\)", 'great', sent)
    sent = re.sub("\:\*", 'love', sent)
    sent = re.sub("\<3", 'love', sent)
    sent = re.sub("\:\'\(", 'cry', sent)
    sent = re.sub(":\(\(", 'unhappy', sent)
    sent = re.sub(":\)\)", 'laugh', sent)
    sent = re.sub("\|\-\)", 'sleepy', sent)
    sent = re.sub(">:O", 'upset', sent)
    sent = re.sub(":O", 'confused', sent)
    sent = re.sub("'", '', sent)
    sent = sent.lower()
    sent = re.sub("not", 'NOT', sent)
    sent = re.sub("won't", 'WILL NOT', sent)
    sent = re.sub("amn't", 'AM NOT', sent)
    sent = re.sub("isn't", 'IS NOT', sent)
    sent = re.sub("arn't", 'ARE NOT', sent)
    sent = re.sub("wasn't", 'WAS NOT', sent)
    sent = re.sub("weren't", 'WERE NOT', sent)
    sent = re.sub("doesn't", 'DOES NOT', sent)
    sent = re.sub("don't", 'DO NOT', sent)
    sent = re.sub("didn't", 'DID NOT', sent)
    sent = re.sub("cann't", 'CAN NOT', sent)
    sent = re.sub("couldn't", 'COULD NOT', sent)
    sent = re.sub("wouldn't", 'WOULD NOT', sent)
    sent = re.sub("hasn't", 'HAS NOT', sent)
    sent = re.sub("haven't", 'HAVE NOT', sent)
    sent = re.sub("hadn't", 'HAD  NOT', sent)
    sent = re.sub("no", 'NO', sent)
    sent = re.sub("more", 'MORE', sent)

    sent = re.sub('[0-9]+', '', sent)
    for c in string.punctuation: sent = sent.replace(c, '')
    sent = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*').sub('', sent)

    sent = re.sub('NOT', 'not', sent)
    sent = re.sub('WILL NOT', 'not', sent)
    sent = re.sub('AM NOT', 'not', sent)
    sent = re.sub('IS NOT', 'not', sent)
    sent = re.sub('ARE NOT', 'not', sent)
    sent = re.sub('WAS NOT', 'not', sent)
    sent = re.sub('WERE NOT', 'not', sent)
    sent = re.sub('DOES NOT', 'not', sent)
    sent = re.sub('DO NOT', 'not', sent)
    sent = re.sub('DID NOT', 'not', sent)
    sent = re.sub('CAN NOT', 'not', sent)
    sent = re.sub('COULD NOT', 'not', sent)
    sent = re.sub('WOULD NOT', 'not', sent)
    sent = re.sub('HAS NOT', 'not', sent)
    sent = re.sub('HAVE NOT', 'not', sent)
    sent = re.sub('HAD NOT', 'not', sent)
    sent = re.sub('NO', 'no', sent)
    sent = re.sub('MORE', 'more', sent)
    sent = sent.lower()
    tokenize = word_tokenize(sent)
    pos_tagged = pos_tag(tokenize)
    lemmatized_sentence = []
    for tag in pos_tagged:
        if tag[1].startswith('J'):
            lemmatized_sentence.append(lemmatizer.lemmatize(tag[0], pos='a'))
        elif tag[1].startswith('V'):
            lemmatized_sentence.append(lemmatizer.lemmatize(tag[0], pos='v'))
        elif tag[1].startswith('N'):
            lemmatized_sentence.append(lemmatizer.lemmatize(tag[0], pos='n'))
        elif tag[1].startswith('R'):
            lemmatized_sentence.append(lemmatizer.lemmatize(tag[0], pos='r'))
        else:
            lemmatized_sentence.append(tag[0])
    Preprocessedpost=' '.join(lemmatized_sentence)


    syn_file='Resources/Data/Synonms.txt'

    post=word_tokenize(Preprocessedpost)
    k=0
    while k<post.__len__():
        a = [];
        i = 0;
        b = '';
        csvReader = csv.reader(open(syn_file, 'rb'), delimiter=' ', quotechar='|');
        for row in csvReader:
            a.append(row);
        for i in range(0, len(a)):
            m=0
            while m < a.__len__():
                if post[k] in a[m]:
                    Preprocessedpost = re.sub(post[k], a[m][0], Preprocessedpost)
                m=m+1
        k=k+1
    # print sent

    Post=word_tokenize(Preprocessedpost)

    features = 'Resources/Data/features.csv'
    with open(features, 'r') as f:
        for line in f:
            words = line.split(",")
            # print words

    vect = []
    j=0
    while j < words.__len__():
        k = 0
        l = 0
        while k < Post.__len__():
            if words[j] == Post[k]:
                l = l + 1
            k = k + 1
        j = j + 1
        vect.append(l)
    # print vect

    predictionList = {NAIVEBAYES: '', SVM: '', RULEBASED: ''}

    classifierNB='Resources/Data/NBclassifier.pkl'
    with open(classifierNB, 'rb') as fid:
        gnb_loaded = cPickle.load(fid)
        if gnb_loaded.predict(vect)==1:
            predictionList[NAIVEBAYES] = 'Positive'
        else:
            predictionList[NAIVEBAYES] = 'Negative'

    # print gnb_loaded.predict(vect)

    classifierSVM = 'Resources/Data/SVMclassifier.pkl'
    with open(classifierSVM, 'rb') as f:
        loaded = cPickle.load(f)
        if loaded.predict(vect)==1:
            predictionList[SVM] = 'Positive'
        else:
            predictionList[SVM] = 'Negative'

    # print loaded.predict(vect)

    bigrams=[]
    bi = ngrams(sent.split(), 2)
    for grams in bi:
        bigrams.append(grams)
    # print bigrams

    a=['not','never','none','nobody','nowhere','neigher','nor']
    i=0
    negation=[]
    while i<a.__len__():
        for k in bigrams:
            j= ' '.join(k)
            if a[i] in j.split(' ', 1)[0]:
                x= j.split(' ', 1)[1]
                negation.append(x)
        i=i+1

    post_text=word_tokenize(sent)

    pos_words=[]
    with open(pos_lex_path ,'r')as f:
        reader = csv.reader(f, delimiter=',')
        for r in reader:
            pos_words.append(r)
    pos_word_list = []
    for i in pos_words:
        pos_word_list.append(i[0])

    i=0
    count_pos = 0
    while i<post_text.__len__():
        j=0
        while j<pos_word_list.__len__():
            if post_text[i]==pos_word_list[j]:
                count_pos=count_pos+1
            j=j+1
        i=i+1

    i=0
    count_negative = 0
    while i<negation.__len__():
        j=0
        while j<pos_word_list.__len__():
            if negation[i]==pos_word_list[j]:
                count_negative=count_negative+1
            j=j+1
        i=i+1

    neg_words=[]
    with open(neg_lex_path ,'r')as f:
        reader = csv.reader(f, delimiter=',')
        for r in reader:
            neg_words.append(r)
    neg_word_list = []
    for i in neg_words:
        neg_word_list.append(i[0])

    i=0
    count_neg = 0
    while i<post_text.__len__():
        j=0
        while j<neg_word_list.__len__():
            if str(post_text[i])== str(neg_word_list[j]):
                count_neg=count_neg+1
            j=j+1
        i=i+1

    i=0
    count_positive = 0
    while i<negation.__len__():
        j=0
        while j<neg_word_list.__len__():
            if negation[i]==neg_word_list[j]:
                count_positive=count_positive+1
            j=j+1
        i=i+1

    positive_word_count = count_pos + count_positive - count_negative
    negative_word_count = count_neg + count_negative - count_positive

    # print positive_word_count
    # print negative_word_count

    if positive_word_count > negative_word_count:
        predictionList[RULEBASED] = 'Positive'

    elif negative_word_count > positive_word_count:
        predictionList[RULEBASED] = 'Negative'

    elif negative_word_count == positive_word_count:
        predictionList[RULEBASED] = 'Neutral'


    return predictionList





