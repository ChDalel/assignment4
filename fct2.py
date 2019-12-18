import requests
url = ('https://newsapi.org/v2/everything?'
       'q=health&'
       'from_param=2019-12-01&'
       'to=2019-12-18&'
       'apiKey=b4e1a3f84d634379b8b781fbeb1a17e6')
response = requests.get(url)
res=response.json()
for i in res['articles']:
    print ((i['title'])+':')
    print(i['description'])
    print('')
