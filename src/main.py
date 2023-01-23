import gradio as gr
from get_tweets_and_users import getUserTweets
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def scanUser(username, limit):
    # print("username")
    # print(username)
    # print("limit")
    # print(type(username))
    result = getUserTweets(username, limit)
    # print("result")
    # print(result)
    return result

gradio = gr.Interface(fn=scanUser, inputs=["text", "text"], outputs="textbox")

def main():
    gradio.launch()

if __name__ == "__main__":
    print("Starting the server... Date: ", current_time)
    main()
