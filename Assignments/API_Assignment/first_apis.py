import requests
import json

def search_syns(term):
   syns_list = []
   url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/'
   my_key = '?key=56d13b27-63e0-4a06-8fb6-98be586e839b'
   my_url = url + term + my_key
   response = requests.get(my_url)
   result = response.json()
   for i in range(len(result)):
       syns_list.append(result[i]['meta']['syns'])
   return syns_list

url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/'
my_key = '?key=56d13b27-63e0-4a06-8fb6-98be586e839b'
term = 'love'
my_url = url + term + my_key
response = requests.get(my_url)
result = response.json()

with open('result.json','w') as outfile:
    json.dump(result,outfile)