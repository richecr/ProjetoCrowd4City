from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import datetime

#start = datetime.datetime(2016,10,1) #year, month, day

try:
    f = open('dia', 'r')
    dados = f.read()
    start = datetime.datetime.strptime(dados, '%m/%d/%Y')
    print(start)
except FileNotFoundError:
    start = datetime.datetime(2016,10,1)

# Para Lixo: lixo na rua
# Para Segurança: falta de segurança na rua
# Para saúde: 
# Para Educação: 

# edit these three variables
user = 'falta de segurança na rua'

end = datetime.datetime(2019, 6, 4)  # year, month, day
print(start)
print(end)
# only edit these if you're having problems
delay = 1  # time to wait on each page load before reading the page
driver = webdriver.Firefox()  # options are Chrome() Firefox() Safari()

'''
["1093673934187315200", "1101443847681384448", "1120977738737815552", "1101195226755026945", "1126806623027179522", "1118093056635486209", "1103115430577799169", "1115725094779748352", "1099345913397604353", "1086001567634018309", "1093222233735118849", "1100820543241101312", "1133571494552973315", "1128631342294605827", 
'''

# don't mess with this stuff
twitter_ids_filename = 'all_ids.json'
days = (end - start).days + 1
id_selector = '.time a.tweet-timestamp'
tweet_selector = 'li.js-stream-item'
user = user.lower()
ids = []

def escrever_dia(date):
    dia = date.strftime('%m/%d/%Y')
    arquivo = open('dia', 'w+')
    arquivo.write(dia)
    arquivo.close()

def format_day(date):
    day = '0' + str(date.day) if len(str(date.day)) == 1 else str(date.day)
    month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
    year = str(date.year)
    return '-'.join([year, month, day])

def form_url(since, until):
    p1 = 'https://twitter.com/search?f=tweets&vertical=default&q='
    p2 =  user + '%20since%3A' + since + '%20until%3A' + until + 'include%3Aretweets&src=typd'
    return p1 + p2

def increment_day(date, i):
    return date + datetime.timedelta(days=i)

for day in range(days):
    d1 = format_day(increment_day(start, 0))
    d2 = format_day(increment_day(start, 1))
    url = form_url(d1, d2)
    print(url)
    print(d1)
    driver.get(url)
    sleep(delay)

    try:
        found_tweets = driver.find_elements_by_css_selector(tweet_selector)
        increment = 10

        while len(found_tweets) >= increment:
            print('scrolling down to load more tweets')
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(delay)
            found_tweets = driver.find_elements_by_css_selector(tweet_selector)
            increment += 10

        print('{} tweets found, {} total'.format(len(found_tweets), len(ids)))

        for tweet in found_tweets:
            try:
                id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
                ids.append(id)
            except StaleElementReferenceException as e:
                print('lost element reference', tweet)

    except NoSuchElementException:
        print('no tweets on this day')

    try:
        with open(twitter_ids_filename) as f:
            all_ids = ids + json.load(f)
            data_to_write = list(set(all_ids))
            print('tweets found on this scrape: ', len(ids))
            print('total tweet count: ', len(data_to_write))
    except FileNotFoundError:
        with open(twitter_ids_filename, 'w') as f:
            all_ids = ids
            data_to_write = list(set(all_ids))
            print('tweets found on this scrape: ', len(ids))
            print('total tweet count: ', len(data_to_write))

    with open(twitter_ids_filename, 'w') as outfile:
        json.dump(data_to_write, outfile)
    ids = []
    start = increment_day(start, 1)
    escrever_dia(start)


print('all done here')
driver.close()
