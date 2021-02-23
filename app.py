from flask import Flask
import tweepy

app = Flask(__name__)

consumer_key = '9WNXStqfl3a0MLhA3YcUJpbdA'
consumer_secret = 'ihFHcWDcmKjlXFMVJswX8fr6CggTFJ4bqxVCnNcmDlefJNxacz'
access_token = '3270593396-KsUWdXzHgJwp2wKRQhET1qWu8D8ZK5KpDPSaasJ'
access_token_secret = 'UDFMyGSI618oW15kBXqSX0VCeuwfRmWXXqLNflM6Jsfnl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
me = api.me()
print(me.screen_name)

dir(api)

@app.route('/')
def hello():
    return "Hello!"


@app.route('/timeline')
def display_timeline():
    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)
        return tweet.text

@app.route('/search')
def location_search():
    public_tweets = api.search(dog)
    return "hello"

    

if __name__ == '__main__':
    app.run()