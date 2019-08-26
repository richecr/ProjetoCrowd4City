from __future__ import unicode_literals
import json
import youtube_dl
import os


# Testar esse código em casa.
'''
def get_videos():
    urls = open('./links.json', 'r')
    urls.read()
    urls.close()
    get_vids = os.system("youtube-dl --verbose -o '/audios/%(title)s.%(ext)s' https://globoplay.globo.com/v/7843006/ ")

get_videos()
'''

with open('../links1.json') as f:
    links1 = json.load(f)

with open('../links.json') as f:
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

videos_falharam = []
comeca = 27
cont = 0
link_ = "2597930"
baixar = False

for link in links1:
    if (link_ in link):
        baixar = True
    if (baixar):
        baixado = False
        for l in links:
            l = l.split("%2F")
            l = "https://globoplay.globo.com/v/" + l[4] + "/"
            if (l == link):
                baixado = True
        if (not baixado):
            print(link)
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
            except:
                videos_falharam.append(link)
                with open("../videos_falharam.json", 'w', encoding="utf-8") as vf:
                    json.dumps(videos_falharam)
                continue