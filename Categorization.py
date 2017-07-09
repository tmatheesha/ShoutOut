from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize
from pymongo import MongoClient
from stop_words import get_stop_words
import customLib

#Database connection
connection = MongoClient()
db = connection.Classification

#Preprocess of the post
def preprocess(post):
    # Preprocessing of the post
    post = post.lower()
    stop_wordset1 = set(stopwords.words("english"))
    stop_wordsset2 = get_stop_words('english')
    stop_words_mergedlist = []
    stop_words_mergedlist.extend(stop_wordset1)
    stop_words_mergedlist.extend(stop_wordsset2)
    stop_words_mergedlist.extend(customLib.wordArray)
    lemmatizer = WordNetLemmatizer()

    # Remove tags and special characters and stopword and added to new collection keyword
    data = lemmatizer.lemmatize(post)
    p = re.compile(r'<.*?>')
    t = (p.sub('', data))
    t1 = re.sub(r'[^\w]', ' ', t)
    words = word_tokenize(t1)
    filteredData = []
    for w in words:
        if w not in stop_words_mergedlist:
            # if w not in filteredData:
            if not w.isdigit():
                filteredData.append(w)
    return filteredData

#class classify():
def categorization(post):

    weightMusic = []
    weightMovie = []
    weightSport = []
    weightPolitic = []
    weightIT = []

    collection = db.probabilityFeature
    weightCollection = db.weightMatrix

    #post = 'the movie premier on the first of june and actor and actress will have presented for the premier at cinema hall'
    filteredData = preprocess(post)

    #print filteredData

    for weight in weightCollection.find():
        if (weight['category'] == "sport"):
            weightSport.append(weight['weight'])
        if (weight['category'] == "movie"):
            weightMovie.append(weight['weight'])
        if (weight['category'] == "music"):
             weightMusic.append(weight['weight'])
        if (weight['category'] == "politic"):
            weightPolitic.append(weight['weight'])
        if (weight['category'] == "IT"):
            weightIT.append(weight['weight'])

                # Get unique word from the filteredData
    uniquewordWithCount = []
    for word in filteredData:
        check = 'false'
        for w in uniquewordWithCount:
            if w['word'] == word:
                check = 'true'
                w['count'] += 1
                break
            else:
                check = 'false'
        if check == 'false':
            uniquewordWithCount.append({
                'word': word,
                'count': 1.0,
            })

    totalFreqArray = []

        # Get total probability of each category
    for obj in collection.find():
        keyword = obj['keywords']
        feature = obj['category']
        #print feature
        probabilityArray = []
        for word in uniquewordWithCount:
            for w in keyword:
                if ((w['word'] == word['word'])):
                   # print w['word']
                    #print w['probability']
                    probabilityArray.append(
                        (word['count'] * w['probability'])
                        )

        if (probabilityArray == []):
                break
            #print ('Null')
        else:
            #
            frequency=sum(probabilityArray)
            totalFreqArray.append({
                    'totalFrequency': frequency,
                    'category': feature})
                # for p in totalProbArray:
                #     print p['category']
                #     print p['totalProbability']

    if(totalFreqArray==[]):
        maxF='Other'
    else:
        maxProb=totalFreqArray[0]
        for tp in totalFreqArray:
            if (maxProb['totalFrequency']<tp['totalFrequency']):
                 maxProb=tp
    # print maxProb

                # Weighted Value
        for freqObj in totalFreqArray:
            if (freqObj['category'] == "sport"):
                val = weightSport[len(weightSport) - 1]
            if (freqObj['category'] == "music"):
                val = weightMusic[len(weightMusic) - 1]
            if (freqObj['category'] == "movie"):
                val = weightMovie[len(weightMovie) - 1]
            if (freqObj['category'] == "politic"):
                val = weightPolitic[len(weightPolitic) - 1]
            if (freqObj['category'] == "IT"):
                val = weightIT[len(weightIT) - 1]
            # frequency=freqObj['totalFrequency']
            freqObj['totalFrequency'] = freqObj['totalFrequency'] * val
            freqObj['weight'] = val

            # Print Weighted Value
    #for freqObj in totalFreqArray:
        #print ('Probability of dataset belong ' + freqObj['category'] + ' is')
        #print freqObj['totalFrequency']
        maxF=''
        if (totalFreqArray == []):
            maxF='Other'

        else:
            maxFreq = totalFreqArray[0]
            for freq in totalFreqArray:
                if (freq['totalFrequency'] > maxFreq['totalFrequency']):
                    maxFreq = freq
            # print trueCategory
        #print ('Category is ' + maxFreq['category'])
            maxF = maxFreq['category']

        connection.close()

    return maxF
#classify().categorization()