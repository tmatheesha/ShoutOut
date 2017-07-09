from  __future__ import division


import zlib,sys,time,base64
import nltk
import numpy as np
import sklearn
import matplotlib.pyplot as  plt
from matplotlib import style
from sklearn.externals import joblib
from sklearn import datasets, linear_model
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
import math
from pymongo import MongoClient
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


def main(val_spm2):
    Numerals_spm_perc_arr = []
    Cap_spm_perc_arr = []


    AllCap_spm_perc_arr = []

    P_spm_Id = []
    souped_spm = BeautifulSoup(val_spm2, "lxml")
    prepros_spm = souped_spm.get_text()
    tokend_words_spm = nltk.word_tokenize(prepros_spm)

    if len(prepros_spm) != 0 and len(tokend_words_spm) != 0:

        Cap_spm_perc_arr.append(sum(1 for c in prepros_spm if c.isupper()) / len(prepros_spm) * 100)
        AllCap_spm_perc_arr.append(sum(1 for cp in tokend_words_spm if cp.isupper()) / len(tokend_words_spm) * 100)
        Numerals_spm_perc_arr.append(sum(1 for c in prepros_spm if c.isdigit()) / len(prepros_spm) * 100)

    else:
        Cap_spm_perc_arr.append(0)
        AllCap_spm_perc_arr.append(0)
        Numerals_spm_perc_arr.append(0)

    temp = np.array([AllCap_spm_perc_arr, Cap_spm_perc_arr, Numerals_spm_perc_arr])

    temp = np.array(temp).reshape((1, -1))

    model_clone = joblib.load('opinion_spam_capital_word_feat_detection_IT_meta.pkl')

    Result_opinion_spam = str(model_clone.predict(temp))

    return Result_opinion_spam

if __name__ == '__main__':
    main()