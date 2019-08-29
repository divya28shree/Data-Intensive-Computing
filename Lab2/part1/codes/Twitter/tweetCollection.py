import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

# import datetime
# Twitter API credentials
consumer_key = "Bc1ZVvnYcApX3wN5oI6NRR6bq"
consumer_secret = "jBXSNViqRqWtBLLv4xn9vAeYfj3i0dDAcFkD4lAl4mjZ2jw8ns"
access_key = "1036138730627784704-xSYOA70hhv6DJfpLiiFAtakTp6b3ps"
access_secret = "1TeBt2cE2yjk933zZYaflDIFSitwUHUxH0msZaUYaOatM"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret
auth.set_access_token(access_key, access_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

tag = 'author'
class Mylistener(StreamListener):
    def on_data(self, data):
        try:
            with open('/home/divya/Desktop/DIC/Lab2/Twitter/final/'+tag+'.json', 'a', encoding='utf-8') as f:
                if 'RT' in data:
                    return True
                d = json.loads(data)
                txt = d['text']
                #print (txt)
                if tag in txt:
                    print(data)
                    f.write(data)
            return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
    def on_timeout(self):
        return True


stream = Stream(auth, Mylistener(), tweet_mode='extended')

stream.filter(track=[tag], languages=['en'], locations=[-171.791110603, 18.91619, -66.96466, 71.3577635769],
              filter_level='low')

