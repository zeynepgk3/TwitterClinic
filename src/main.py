import gradio as gr
from common import writeToFile
from get_tweets_and_users import getUserTweets
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H_%M_%S")

tweets=[]
columns = ['username', 'rawContent', 'label', 'polarity', 'subjectivity', 'url']

def scanUser(username, limitOfTweets):
    result,tweets = getUserTweets(username, limitOfTweets)
    fileName = username+'_'+current_time+'_results'
    writeToFile(tweets,columns,fileName)
    return result

gradio = gr.Interface(fn=scanUser, inputs=["text", "text"], outputs="textbox")

def main():
    gradio.launch()

if __name__ == "__main__":
    print("Starting the server... Date: ", current_time)
    main()
