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


# CHANGE THIS TO THE USER YOU WANT
user = 'dados'

with open('sample_api_keys.json') as f:
    keys = json.load(f)

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)
user = user.lower()
output_file = 'dados/educacao/{}.json'.format(user)
output_file_short = 'dados/educacao/{}_short.json'.format(user)
compression = zipfile.ZIP_DEFLATED

with open('all_ids.json') as f:
    ids = json.load(f)

print('total ids: {}'.format(len(ids)))

all_data = []
start = 0
end = 100
limit = len(ids)
i = math.ceil(limit / 100)

for go in range(i):
    print('currently getting {} - {}'.format(start, end))
    sleep(6)  # needed to prevent hitting API rate limit
    id_batch = ids[start:end]
    start += 100
    end += 100
    tweets = api.statuses_lookup(id_batch, tweet_mode="extended")
    for tweet in tweets:
        all_data.append(tweet)

tweets_dict = {}

#transform the tweepy tweets into a 2D array that will populate the csv	
output = [[tweet.id_str, tweet.created_at, tweet.created_at.strftime("%d-%m-%Y %H:%M:%S"), tweet.full_text] for tweet in all_data]
tweets_dict["dados"] = output

# write to csv
with open('./dados/educacao/dados.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["id_str","datetime","created_at","text"])
    writer.writerows(output)