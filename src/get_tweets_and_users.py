import snscrape.modules.twitter as sntw
import snscrape.modules.reddit as snrd
import numpy as np
import pandas as pd
from common import writeToFile
from detection import getPolarity, getSubjectivity, predict, preprocess

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

prediction_index = {"Suicidal": -0.3, "Depressive": -0.2, "Stressed": -0.1,
 "Anxious": -0.1, "Lonely": -0.1, "Normal": 0.1, "Positive": 0.3}

# add polarity and multiply subjectivity
def getTotalScore(predictions, subjectivies, polarities):
    predictions=pd.Series(predictions)
    predictions=predictions.map(prediction_index)
    predictions=np.array(predictions)
    polarities=polarities.astype(float)
    subjectivies=subjectivies.astype(float)

    predictions = predictions + polarities
    # if subjectivity is zero, then it is not important
    predictions = predictions * (subjectivies+0.1)
    
    totalScore=predictions.sum()/len(predictions)
    return totalScore

def analyseTotalScore(result):
    if result < -0.9:
        return "Critical"
    elif result < -0.7:
        return "Dangerous"
    elif result < -0.4:
        return "Sirious"
    elif result < 0:
        return "Stable"
    elif result < 0.2:
        return "Good"
    elif result < 0.5:
        return "Great"
    elif result < 0.8:
        return "Perfect"
    else:
        return "Excellent"

def getUserTweets(user, limit):
    query = "(from:"+user+")"
    tweets = []

    for tweet in sntw.TwitterSearchScraper(query).get_items():
        if (len(tweets) == int(limit)):
            break
        else:
            polarity = getPolarity(tweet.rawContent)
            subjectivity = getSubjectivity(tweet.rawContent)
            processed_tweet=preprocess(tweet.rawContent)
            label=predict([processed_tweet])
            tweets.append([tweet.username, tweet.rawContent, label[0], polarity, subjectivity, tweet.url])
        print("tweets::")
        print(tweets)

    tweets = np.array(tweets)

    subjectivity_list=tweets[:,4]
    polarity_list=tweets[:,3]
    prediction_list=tweets[:,2]

    totalScore=getTotalScore(prediction_list, subjectivity_list, polarity_list)
    print("getTotalScore(predictions, tweets[:,4], tweets[:,3])")
    print(totalScore)
    analyse_result=analyseTotalScore(totalScore)
    print("analyseTotalScore(totalScore)")
    print(analyseTotalScore(totalScore))

    return analyse_result,tweets


def findTweetsByHashtags(hashtag):
    query = "(from:"+hashtag+")"

    return query
