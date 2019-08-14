from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import csv

driver = webdriver.Firefox()
driver.get("https://cep.guiamais.com.br/busca/campina+grande-pb?page=1")

nomes_ruas = []
cont_ruas = 0
cont = 0
for i in range(1, 127):
    driver.get("https://cep.guiamais.com.br/busca/campina+grande-pb?page="+str(i))
    found_ruas = driver.find_elements_by_css_selector(".table-responsive")
    ruas = found_ruas[0].find_elements_by_tag_name("tbody")
    ruas = ruas[0].find_elements_by_tag_name('tr')
    
    for j in range(len(ruas)):
        r = ruas[j].find_elements_by_tag_name('td')
        r = r[0].find_elements_by_tag_name('a')

        nomes_ruas.append(r[0].get_attribute('text'))
        nome_r = r[0].get_attribute('text').split()
        cont += len(nome_r) - 1
        cont_ruas += 1

print(cont) # 9798
print(cont_ruas) # 3150
# média de quantidade de palavras do nome das ruas de cg: 3.11
ruas1 = []
for r in nomes_ruas:
    ruas1.append(r.lower())

with open("./ruas.json", 'w') as outfile:
    json.dump(ruas1, outfile)

