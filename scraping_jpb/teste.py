#ydl2.py
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import youtube_dl
import json

driver = webdriver.Chrome(executable_path=r"F:\Rick\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://g1.globo.com/busca/?q=calendario+jpb+campina+grande&page=1&order=recent&species=v%C3%ADdeos")
cont  = 0
found_noticias = driver.find_elements_by_css_selector(".results__list")
noticias = found_noticias.children

print(noticias)

'''
while (cont < 6):    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
'''

'''
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',        
    'noplaylist' : True,        
    'progress_hooks': [my_hook],  
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://globoplay.globo.com/v/7780021/'])
'''