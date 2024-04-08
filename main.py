import tweepy
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Função para verificar se um tweet já foi retweetado pelo bot
def check_if_retweeted(tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        return tweet.retweeted
    except tweepy.TweepError as e:
        print("Error checking if tweet already retweeted:", e)
        return False

for tweet in tweepy.Cursor(api.search_tweets, q='#example').items(5):
    try:
        if not tweet.retweeted and not check_if_retweeted(tweet.id):
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
            tweet.retweet()
            print('Retweet published successfully.')
            sleep(10)
        else:
            print("\nTweet already retweeted, skipping...")

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
