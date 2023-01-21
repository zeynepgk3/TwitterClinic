#Redis connection
import redis
import logging
import praw
logging.basicConfig(level=logging.DEBUG)


def redis_connect():
    print("Starting")
    redis_host = 'localhost'
    redis_port =6379
    try:
        r=redis.StrictRedis(host= redis_host, port= redis_port, decode_responses=True)
        r.set("initMessage","Hello, World!")
        initMessage=r.get("initMessage")
        print(initMessage)
        logging.info("Connected to redis")
  
    except Exception as e:
        logging.error("Failure to connect to redis: {}".format(e))

# Postgresql connection

# Reddit connection

def reddit_connect():
    id="0_X4f7RzbJxHzXQ813VSvw"
    secret="YB71xFlumH9aqqz69sZfeVJqTN76Hw"
    user_agent="twitterClinic"
    try:
        reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent=user_agent)
        logging.info("Connected to reddit")
        print(type(reddit))
        return reddit
    except Exception as e:
        logging.error("Failure to connect to reddit: {}".format(e))

reddit_connect()
