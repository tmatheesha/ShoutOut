import csv
from nltk.corpus import stopwords
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk import pos_tag

def preprocessing(filepath1,filepath2):
    myfile = open(filepath2, 'wb')
    writer = csv.writer(myfile, delimiter=',', lineterminator='\n')
    with open(filepath1, 'rb') as f:
        reader = csv.reader(f,delimiter=',')
        data_list=[]
        lemmatizer = WordNetLemmatizer()
        for row in reader:
            for sent in row:
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
                sentence = lemmatized_sentence
                fullsentence = ' '.join(sentence)
                data_list.append(fullsentence)

    for data in data_list:
        writer.writerow([data])

    return data_list



