import requests
from flask import Flask, redirect, url_for
from bson.objectid import ObjectId
from flask import Flask, render_template, jsonify, json, request
# from rq import Queue
# from worker import conn
import numpy as np
# from rq.job import Job
# from fabric.api import *
from sklearn.externals import joblib
import Inauthentic_text_detection
import opinion_spam
import Categorization
import main
import Sentiment_Analysis.UserRecommendation as ur
import Sentiment_Analysis.Predicting as pd
from bs4 import BeautifulSoup
app = Flask(__name__)
url_original = ""

# q=Queue(connection=conn)
def spam_detection(url):
    errors = []
    resp_json={}

    #Thisun---------------------------------------------------------------------------------------
    #Result_authenticity = True if Inauthentic_text_detection.main(url) == "[1]" else False
    Result_authenticity=Inauthentic_text_detection.main(url)
    Result_opinion_spam= True if opinion_spam.main(url) == "[1]" else False

    #navodya--------------------------------------------------------------------------------------
    Result_classification = Categorization.categorization(url)

    #chanuka--------------------------------------------------------------------------------------
    Result_semantic_search =main.answerQuestion(url)

    #Dilsi----------------------------------------------------------------------------------------
    list = pd.predictPost(url)
    sentiment=list[pd.RULEBASED]
    user_list = ur.prefered_users(Result_classification).encode('utf-8')

    #-------------------------------------------------------------------------------------------

    #resp_json['Is_inauthentic'] = str(Result_authenticity)
    #resp_json['Classification'] = str (Result_classification)
    Result_out=jsonify(Is_inauthentic = str(Result_authenticity),Is_Opinion_spam=str(Result_opinion_spam),Classification=str(Result_classification),Sentiment=str(sentiment),Semantic_Search=str(Result_semantic_search),
                       Recommandation=((str(user_list)).strip()).split("\n"))
    #Result_out=json.dumps(resp_json)
    return Result_out


#------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def getAnnalysed():
    #data=requests.json()
    #data = json.load(request.data.decode())
    data = json.loads(request.data.decode())
    url = data["url"]
    url_original=url
    #---------------Preprocessing----------------------------
    souped_url = BeautifulSoup(str(url), "lxml")
    prepros_url = souped_url.get_text()

    #if 'http://' not in url[:7]:
        #url = 'http://' + url
    # start job
    #resp_raw = spam_detection(url)
    #resp_json=json.dump({'response': resp_raw})
    return url


@app.route("/results/<resp_raw>", methods=['GET'])
def get_results(resp_raw):
    #resp_raw=True if resp_raw == "0" else False
    #resp_raw=resp_raw.encode('utf-8')
    #data = jsonify(Is_inauthentic = str(resp_raw))
    resp = spam_detection(resp_raw)
    #data = jsonify(resp)
    return resp


if __name__ == "__main__":
    app.run()
