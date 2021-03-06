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


print('metadata collection complete')
print('creating master json file')
with open(output_file, 'w') as outfile:
    json.dump(all_data, outfile)

print('creating ziped master json file')
zf = zipfile.ZipFile('dados/educacao/{}.zip'.format(user), mode='w')
zf.write(output_file, compress_type=compression)
zf.close()

results = []

def is_retweet(entry):
    return 'retweeted_status' in entry.keys()

def get_source(entry):
    if '<' in entry["source"]:
        return entry["source"].split('>')[1].split('<')[0]
    else:
        return entry["source"]

with open(output_file) as json_data:
    data = json.load(json_data)
    for entry in data:
        t = {
            "created_at": entry["created_at"],
            "full_text": entry["full_text"],
            "in_reply_to_screen_name": entry["in_reply_to_screen_name"],
            "retweet_count": entry["retweet_count"],
            "favorite_count": entry["favorite_count"],
            "source": get_source(entry),
            "id_str": entry["id_str"],
            "is_retweet": is_retweet(entry),
            "coordinates": entry["coordinates"]
        }
        results.append(t)

print('creating minimized json master file')
with open(output_file_short, 'w') as outfile:
    json.dump(results, outfile)

with open(output_file_short, encoding="utf-8") as master_file:
    data = json.load(master_file)
    fields = ["favorite_count", "source", "full_text", "in_reply_to_screen_name", "is_retweet", "created_at", "retweet_count", "id_str", "coordinates"]
    print('creating CSV version of minimized json master file')
    f = csv.writer(open('dados/educacao/{}.csv'.format(user), 'w'))
    f.writerow(fields)
    for x in data:
        f.writerow([x["favorite_count"], x["source"], x["full_text"].encode("utf-8"), x["in_reply_to_screen_name"], x["is_retweet"], x["created_at"], x["retweet_count"], x["id_str"], x["coordinates"]])