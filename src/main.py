import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntw
import snscrape.modules.reddit as snrd
from common import writeToFile
import joblib 

print("Starting")
modal=joblib.load("modal/mental_illness_detector.pkl","r")
print("Starting2")

def findTeenAccounts():
    query="(from:Mortieshaa)"
    tweets=[]
    limit=50

    for tweet in sntw.TwitterSearchScraper(query).get_items():
        if(len(tweets) == limit):
            break
        else:
            tweets.append([tweet.date, tweet.username, tweet.content, tweet.url])
        #print(vars(tweet.content))
        #break
        columns=['date', 'username', 'content','url']
        fileName='twitterDatas.html'
        writeToFile(tweets,columns,fileName)
    

def findTweetsByHashtags():
    return "asdas"

def retrieveSuicideWatchHeadlines(): #doesnt work right now but it must be eventually. get the titles from the posts and use them as a train data. Best suicidal texts are here!!!
    query = "SuicideWatch"
    posts=[]
    limit = 2
    snrd.RedditSubredditScraper(query)
    for post in snrd.RedditSubredditScraper(query).get_items():
        if(len(posts) == limit):
            break
        else:
            posts.append(post)
        print(post.title)
        break

# retrieveSuicideWatchHeadlines()

def predict(text):
    result=modal.predict([text])
    return result[0]

def get_prediction_proba(text):
    result=modal.predict_proba([text])
    return result

if __name__ =="__main__":
    result=predict("moving to another city")
    print(result)