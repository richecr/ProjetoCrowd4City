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
links_falharam = []

def escreve():
    with open("../links_falharam.json", 'w') as outfile:
        json.dump(links_falharam, outfile)

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

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://globoplay.globo.com/v/4310516", "https://globoplay.globo.com/v/5486784", "https://globoplay.globo.com/v/5886436", "https://globoplay.globo.com/v/4761695", "https://globoplay.globo.com/v/5466567", "https://globoplay.globo.com/v/7834197"])

'''
for link in links:
    link = link.split("%2F")
    link = "https://globoplay.globo.com/v/" + link[4]
    print(link)
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except:
        links_falharam.append(link)
        if (len(links_falharam) == 10):
            escreve()
        continue
'''