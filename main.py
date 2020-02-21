from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

def print_json(json_object):
  print(json.dumps(json_object, indent=1))

def write_json(dict):
  with open('data2.json', 'w+', encoding="utf8") as f:
    json.dump([status._json for status in dict], f, indent=2)

class Tweeper:
  def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
    self.initialize_api(consumer_key, consumer_secret, access_token, access_secret)

  def initialize_api(self, consumer_key, consumer_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    self.api = tweepy.API(auth, wait_on_rate_limit=True)
  
  def get_me(self):
    return self.api.me()
  
  def get_home_timeline(self, end_page=1):
    timeline = []
    for page in range(1, end_page+1):
      percent = (page/end_page) * 100
      print("Percent:  %.2f" % percent)
      timeline += self.api.home_timeline(page=page, count=200)
    return timeline

if __name__ == "__main__":
  name = '@BTS_SkyTrain'
  consumer_key = 'Uu3FZb0UV4f86NOrcRXKoDWd6'
  consumer_secret = 'iD3J7RF5I6h4zjNy6sy610g4WwbxHW9iGfgyAQxETYSszuYoB5'
  access_token = '1052536547784847360-ebYM0ISRr59gcdW2Su7pfG4kOQlAsX'
  access_secret = 'xvlCEUUZok0jbwGyLJoeBk4mQBXb8cCE76TDkz4dRcjfE'
  client = Tweeper(consumer_key, consumer_secret, access_token, access_secret)
  write_json(client.get_home_timeline(1))