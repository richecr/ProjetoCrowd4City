from __future__ import unicode_literals
import json
import youtube_dl

with open('links.json') as f:
    links = json.load(f)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'noplaylist' : True,
    'progress_hooks': [my_hook],
}

for link in links:
    link = link.split("%2F")
    link = "https://globoplay.globo.com/v/" + link[4]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
