from flask import Flask
import tweepy

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/timeline')
def display_timeline():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)
        return tweet.text


if __name__ == '__main__':
    app.run()
