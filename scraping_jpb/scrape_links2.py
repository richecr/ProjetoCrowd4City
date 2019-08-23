#ydl2.py
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import csv

driver = webdriver.Firefox()
driver.get("https://globoplay.globo.com/busca/?q=calend%C3%A1rio+jpb")
cont  = 0
found_noticias = driver.find_elements_by_css_selector(".tiled-grid-widget")
n = found_noticias[0].find_elements_by_tag_name("li")
quantidade = 800

if (len(n) > quantidade):
    novo_n = []
    for i in range(0, quantidade):
        novo_n.append(n[i])
    
    n = novo_n

while (len(n) < quantidade):
    sleep(2)
    try:
        next_page = driver.find_elements_by_css_selector(".action-button__button")
        found_noticias = driver.find_elements_by_css_selector(".tiled-grid-widget")
        n = found_noticias[0].find_elements_by_tag_name("li")
        next_page[0].click()
    except:
        break
    

links = []
for noticia in n:
    div = noticia.find_elements_by_css_selector(".search-results-videos__video")
    div1 = div[0].find_elements_by_css_selector('.final-content')
    a = div1[0].find_elements_by_tag_name('a')

    links.append(a[0].get_attribute("href"))

print("Quantidade de noticias: ", len(links))
# write to json
with open("./links1.json", 'w') as outfile:
    json.dump(links, outfile)

driver.close()