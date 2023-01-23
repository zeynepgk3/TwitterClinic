import joblib 
from textblob import TextBlob


modal=joblib.load("C:/Users/gokz/Documents/GitHub/TwitterClinics/TwitterClinic/modal/mental_illness_detector.pkl","r")

import re
import string;
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from html import unescape
import en_core_web_sm
nlp = en_core_web_sm.load()

EMOJI_PATTERN=re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", re.UNICODE);
PUNCT_TO_REMOVE = string.punctuation.replace("'", "")
STOP_WORDS=stopwords.words("english")
STOP_WORDS.extend(["'s","'m","'ve","s","#"])

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
#     print(tweet)
    # ans = tweet[1].lower() # lowercase
    ans = tweet.lower() # lowercase
    ans = re.sub('@[^\s]+', '', ans)   # remove mentions
    soup = BeautifulSoup(unescape(ans), 'lxml')
    ans = soup.text
#     print("after -----------")
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
    
#     print(ans)
    return ans


