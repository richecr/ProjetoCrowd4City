# encode: utf-8
import tweepy
import json
import math
import glob
import csv
import zipfile
import zlib
from tweepy import TweepError
from time import sleep

with open('sample_api_keys.json') as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

output_file = './dados/educacao/dados.json'

with open('./dados/educacao/ids.json') as f:
    ids = json.load(f)

print('total ids: {}'.format(len(ids)))

all_data = []
start = 0
end = 100
limit = len(ids)
i = math.ceil(limit / 100)

while (end <= len(ids)):
    print("currently getting {} - {}".format(start, end))
    sleep(6)
    id_batch = ids[start:end]
    start += 100
    end += 100
    tweets = api.statuses_lookup(id_batch, tweet_mode="extended")
    for tweet in tweets:
        all_data.append(tweet)

tweets_dict = {}

tweets_json = [];
for t in all_data:
    tweets_json.append(dict(tweet._json));

print('metadata collection complete')
print('creating master json file')
with open(output_file, 'w') as outfile:
    json.dump(tweets_json, outfile)