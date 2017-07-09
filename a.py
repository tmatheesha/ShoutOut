import Sentiment_Analysis.UserRecommendation as ur
import Sentiment_Analysis.Predicting as pd

post = 'I am tired and i is cheap and unclear,disproportionate,unlikely,hurt,disallow,stunt,'

print pd.predictPost("I am bad.")

list = pd.predictPost(post)
# print list
print list[pd.RULEBASED]

user_list = ur.prefered_users("politic")
print user_list