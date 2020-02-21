from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import pickle
import operation

def print_json(json_object):
  print(json.dumps(json_object, indent=1))

def write_json(dict):
  with open('data2.json', 'w+', encoding="utf8") as f:
    json.dump([status._json for status in dict], f, indent=2)

def pickle_dump(x, name):
  with open(name, 'wb') as f:
    pickle.dump([status._json for status in x], f)

class Tweeper:
  def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
    self.files = {
      'timeline': 'timeline.pkl'
    }
    self.initialize_api(consumer_key, consumer_secret, access_token, access_secret)

  def initialize_api(self, consumer_key, consumer_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    self.api = tweepy.API(auth, wait_on_rate_limit=True)
  
  def set_file(self, name, file):
    self.files[name] = file
  
  def get_me(self):
    return self.api.me()
  
  def get_home_timeline(self, end_page=1):
    timeline = []
    for page in range(1, end_page+1):
      percent = (page/end_page) * 100
      print("Percent:  %.2f" % percent)
      timeline += self.api.home_timeline(page=page, count=200)
      pickle_dump(timeline, self.files['timeline'])
    return timeline

def main():
  import argparse
  parser = argparse.ArgumentParser(description='PyTweeper (Twitter crawler)')
  parser.add_argument('-p', type=int, help='page count for crawler')
  parser.add_argument('-o', type=str, help='output destination', required=True)

  args = vars(parser.parse_args())
  page = args['p'] or 10
  output = args['o']
  
  consumer_key = 'Uu3FZb0UV4f86NOrcRXKoDWd6'
  consumer_secret = 'iD3J7RF5I6h4zjNy6sy610g4WwbxHW9iGfgyAQxETYSszuYoB5'
  access_token = '1052536547784847360-ebYM0ISRr59gcdW2Su7pfG4kOQlAsX'
  access_secret = 'xvlCEUUZok0jbwGyLJoeBk4mQBXb8cCE76TDkz4dRcjfE'
  client = Tweeper(consumer_key, consumer_secret, access_token, access_secret)
  client.set_file('timeline', 'timeline3.pkl')
  client.get_home_timeline(page)
  operation.read_and_download('timeline3.pkl', output)


if __name__ == "__main__":
  main()
  pass
