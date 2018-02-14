#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

consumer_key = 'Enter your consumer key'
consumer_secret = 'Enter your consumer secret'
access_token = 'Enter your access token'
access_token_secret = 'Enter your access token secret'


# OAuth process, using the keys and tokens
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = API(auth)

# Sample method, used to update a status
api.update_status('Hello DREAM! Welcome to Data Mining in Twitter 101.1')



