import praw
from common import writeToFile
from connection import reddit_connect

reddit=reddit_connect()

suicide_watch_posts = reddit.subreddit('SuicideWatch').hot(limit=1000)
submissions=[]
counter=0
for submission in suicide_watch_posts:
    counter += 1
    print(counter)
    print(submission.title)
    print(submission.url)
    print(submission.selftext)
    print(type(submission))
    submissions.append(submission)

# writeToFile(submission,["id","title","url"],"redditSuicideWatchTitles")