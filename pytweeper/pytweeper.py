from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from progress.bar import ChargingBar
import tweepy
import pickle
import os
from .twitter import *
from .operation import *

def pickle_dump(x, name):
  with open(name, 'wb') as f:
    pickle.dump([status._json for status in x], f)

def save_key(key):
  with open('key.pkl', 'wb') as f:
    pickle.dump(key, f)

def load_key():
  try:
    with open('key.pkl', 'rb') as f:
      return pickle.load(f)
  except FileNotFoundError:
    return None

def delete_key():
  try:
    os.remove('key.pkl')
    return True
  except FileNotFoundError:
    return False

class Tweeper:
  def __init__(self):
    self.files = {
      'timeline': 'timeline.pkl'
    }
    self.authorize = False
  
  def logout(self):
    if delete_key():
      self.authorize = False

  def initialize_api(self):
    twitter_auth = TwitterAuth()
    key = load_key() or twitter_auth.auth()
    if (not key['error']):
      self.authorize = True
      save_key(key)
      auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
      auth.set_access_token(key['access_token'], key['access_secret'])
      self.api = tweepy.API(auth, wait_on_rate_limit=True)
    else:
      print("Unauthorize")
  
  def set_file(self, name, file):
    self.files[name] = file
  
  def get_me(self):
    return self.api.me()
  
  def get_home_timeline(self, end_page=1):
    timeline = []
    bar = ChargingBar('Crawling', max=end_page)
    for page in range(1, end_page+1):
      timeline += self.api.home_timeline(page=page, count=200)
      pickle_dump(timeline, self.files['timeline'])
      bar.next()
    bar.finish()
    return timeline

def main():
  import argparse
  parser = argparse.ArgumentParser(description='PyTweeper (Twitter crawler)')
  parser.add_argument('-p', type=int, help='page count for crawler')
  parser.add_argument('-o', type=str, help='output destination')
  parser.add_argument('--logout', action='store_true', help='output destination')

  args = vars(parser.parse_args())
  page = args['p'] or 10
  output = args['o'] or os.path.join(os.getcwd(), 'pytweeper','images')
  logout = args['logout']
  
  client = Tweeper()
  if logout:
    client.logout()
  client.initialize_api()
  if client.authorize:
    client.set_file('timeline', 'timeline3.pkl')
    client.get_home_timeline(page)
    read_and_download('timeline3.pkl', output)


if __name__ == "__main__":
  pass
