import Predicting as prd
import UserRecommendation as rec

post = 'I am tired and i is cheap and unclear,disproportionate,unlikely,hurt,disallow,stunt,'

list = prd.predictPost(post)
print list
print list[prd.RULEBASED]

user_list = rec.prefered_users("Politics")
print user_list

