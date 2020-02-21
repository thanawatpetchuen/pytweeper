import json
import itertools
import requests
import shutil
import os

def make_dir(path):
  if not os.path.exists(path):
      os.makedirs(path)

def download_image(url, image_path):
  response = requests.get(url, stream=True)
  print("Downloading... (%s)" % url)
  with open('./images/'+image_path, 'wb+') as out_file:
      shutil.copyfileobj(response.raw, out_file)
  del response


def mapper(d):
  try:
    print(len(d['entities']['media']))
    image = list(map(lambda x: x['media_url_https'], d['entities']['media']))
    return image
  except KeyError:
    return ''

with open('data.json', 'r') as f:
  data = json.load(f)

mapped = list(map(mapper, data))
merged = list(itertools.chain(*mapped))

print(merged)

for image in merged:
  download_image(image, image.split('/')[-1])