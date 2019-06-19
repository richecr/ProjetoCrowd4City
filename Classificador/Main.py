with open("../twitter_scraping/tweets_testes.csv", "r", encoding="utf-8") as file:
    texto = file.read()
    
    print(file.read().split(",")[1])