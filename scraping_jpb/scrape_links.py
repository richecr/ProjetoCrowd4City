#ydl2.py
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import csv

driver = webdriver.Firefox()
driver.get("http://g1.globo.com/busca/?q=calendario+jpb&page=1&order=recent&species=v%C3%ADdeos")
cont  = 0
found_noticias = driver.find_elements_by_css_selector(".results__list")
n = found_noticias[0].find_elements_by_tag_name("li")
quantidade = 5
if (len(n) > quantidade):
    novo_n = []
    for i in range(0, quantidade):
        novo_n.append(n[i])
    
    n = novo_n

while (len(n) < quantidade):
    sleep(1)
    div_next_page = driver.find_elements_by_css_selector(".pagination")
    next_page = div_next_page[0].find_elements_by_tag_name("a")
    found_noticias = driver.find_elements_by_css_selector(".results__list")
    n = found_noticias[0].find_elements_by_tag_name("li")
    next_page[0].click()

links = []
for noticia in n:
    div = noticia.find_elements_by_css_selector(".widget--info__text-container")
    a = div[0].find_elements_by_tag_name("a")

    links.append(a[0].get_attribute("href"))

print("Quantidade de noticias: ", len(links))
# write to json
with open("./links.json", 'w') as outfile:
    json.dump(links, outfile)

driver.close()