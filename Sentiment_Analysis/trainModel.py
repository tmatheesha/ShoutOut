import Preprocessing as pp


fileN1='../Resources/Data/NegativeDatasetNew.csv'
fileN2='../Resources/Data/Negative_Preprocessed.csv'
pp.preprocessing(fileN1,fileN2)

fileP1='../Resources/Data/PositiveDatasetNew.csv'
fileP2='../Resources/Data/Positive_Preprocessed.csv'
a=pp.preprocessing(fileP1,fileP2)
print a



