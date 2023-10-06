import requests

api_key = 'd17bf137-48db-4cce-9b51-3868ba539e15'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiatze/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)