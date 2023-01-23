import joblib 
from textblob import TextBlob

from common import EMOJI_PATTERN


modal=joblib.load("C:/Users/gokz/Documents/GitHub/TwitterClinics/TwitterClinic/modal/mental_illness_detector.pkl","r")

import re
import string;
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from html import unescape
import en_core_web_sm
nlp = en_core_web_sm.load()

def predict(text):
    print("text")
    print(text)
    result=modal.predict(text)
    return result

def get_prediction_proba(text):
    result=modal.predict_proba([text])
    return result

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

def preprocess(tweet):
    ans = tweet.lower() # lowercase
    ans = re.sub('@[^\s]+', '', ans)   # remove mentions
    soup = BeautifulSoup(unescape(ans), 'lxml')
    ans = soup.text
    ans = EMOJI_PATTERN.sub(r'', ans)  #remove emojis TODO: remove also symbols like :) :D vs.
    ans = re.sub(r'http\S+', '', ans)  # remove links
    ans = " ".join(ans.split())        # remove unnecessarily spaces
    
    data = nlp(ans)
    filtered_tokens=[]
    for token in data:
        if token.is_stop or token.is_punct:
            continue;
        filtered_tokens.append(token.lemma_) #lemmatizes token

    ans = " ".join(filtered_tokens) 
    return ans


