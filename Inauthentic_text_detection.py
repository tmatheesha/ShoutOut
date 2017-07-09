import nltk
import numpy as np
from sklearn.externals import joblib
import enchant

def main(txt):
    not_english_word_count=0
    word_length_bd = []
    word_length_mk = []
    mean_arr_mk = []
    std_arr_mk = []
    mean_arr_bd = []
    std_arr_bd = []
    dic=enchant.Dict("en_US")
    sent_text_bd = nltk.sent_tokenize(txt)
    # take each sentence
    mean_count=0.0
    std_count=0.0
    for sentences_bd in sent_text_bd:
        # take the words array from the sentence
        tokend_bd = nltk.word_tokenize(sentences_bd)
        if not dic.check(tokend_bd):
            not_english_word_count += 1
        # Average =( sum of total number of characters/ number of words)
        average_bd = float(sum(len(word) for word in tokend_bd) / len(tokend_bd))
        # append it to the array
        mean_arr_bd.append(average_bd)
        #mean_count += average_bd
        # print average_bd
        # take each word
        for con_bd in tokend_bd:
            # append it to the word length array
            word_length_bd.append(len(con_bd))
        # take the standard diviation from the word
        std_word_bd = float(np.std(word_length_bd, axis=0))
        # append to the standard deviation array
        std_arr_bd.append(std_word_bd)
        #std_count += std_word_bd

    model_clone = joblib.load('inauthentic_text_detection.pkl')
    mk_result_count = 0
    bd_result_count = 0

    for mean_itt, std_itt in zip(mean_arr_bd, std_arr_bd):
        result_np_arr = np.array([mean_itt, std_itt], dtype=float)

        result_np_arr = np.array(result_np_arr).reshape((1, -1))

        Result_temp = model_clone.predict(result_np_arr)

        if Result_temp == [1]:
            mk_result_count += 1

        elif Result_temp == [0]:

            bd_result_count += 1

    if mk_result_count >= bd_result_count:
        Result_authenticity = False
    else:
        Result_authenticity = True

        #print Result_authenticity


    #if not_english_word_count > 0:
       # Result_authenticity = "1"
    #else:
        #Result_authenticity == "0"


    return Result_authenticity

if __name__=='__main__':

    main()