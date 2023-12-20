import simplejson
import requests

response = requests.get(
    'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
my_heroes = ['Hulk', 'Captain America', 'Thanos']
for hero in response.json():
    if hero.get('name', '') in my_heroes:
        print(hero.get('name', ''), hero.get('powerstat', {}).get('combat'))
