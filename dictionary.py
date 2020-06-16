import requests

r = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/attention?key=fcab0a95-26ee-4436-8e9a-953d07dcdee7')
# r = requests.get('https://imgs.xkcd.com/comics/python.png')
r_dist = r.json()

print(r_dist)
# with open('comic.png', 'wb') as f:
 # 	f.write(r.content) 

# print(r.headers)


# payload = {'page' : 2, 'count' : 25}
# r = requests.get('https://httpbin.org/get', params=payload)

# print(r.url)