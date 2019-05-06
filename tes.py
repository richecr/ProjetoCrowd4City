from biblioteca_twitter import Twitter

t = Twitter('rrUDLNZVqv8DaWX6fkmNrB5V9', 'R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7', '2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK', 'AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW')

# Melhor busca para testar a api do twiiter para o projeto no LSI
# b = t.search('lixo rua calçada', 'pt')

b = t.search('lixo na calçada', 'pt')

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

for r in b:
    u = r['text']
    print(r['user']['geo_enable'])
    print("----> ")
    print(u.translate(non_bmp_map))

    print('-------\n\n')