import requests

api_key = 'ed9f20c1-0072-4e0a-ba4d-84d35c961e10'
word = 'voluminous'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)