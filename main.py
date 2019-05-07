from TwitterAPI import TwitterAPI

api = TwitterAPI("rrUDLNZVqv8DaWX6fkmNrB5V9", "R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7",
               "2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK", "AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW")

r = api.request('statuses/show/:%d' % 1125743655078322176)
t = r.json()

print(t['text'])