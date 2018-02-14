#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

consumer_key = 'Enter your consumer key'
consumer_secret = 'Enter your consumer secret'
access_token = 'Enter your access token'
access_token_secret = 'Enter your access token secret'
file = "Twitter_data_final.csv"
f = open(file, "w")
f.write("Created at" + " , " + "ID" + " , " + "Friends_count" + " , " + "Time Zone" + " , " + "Verified" + "\n")

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    # we are going to filter the results. So, we modify on_status

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            return

        f.write(str(status.user.created_at) + " , " + str(status.user.id_str) + " , "
                #cannot encode characters which is causing a problem right now.
                #+ status.text.encode('utf-8') + " , "
                + str(status.user.friends_count) + " , " + str(status.user.time_zone) + " , " + str(status.user.verified)
                + "\n")

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API

    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    #This line filter Twitter Streams to capture data by the keywords: 'Winter Olympics', 'Olympics'

    stream.filter(track=['Winter Olympics', 'Olympics'])

