import requests
import json

#Cria uma chamada de API e armazena a reposta
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code:{r.status_code}")

#Processa as informações sobre cada contribuição de aritog
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:
    #Cria uma nova chamada API para cada contribuição de artigo
    url = f"https://hacker-news.firebaseio.com/v0/item{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

#Cria um dicionário para cada artigo
submission_dict = {
    'title':response_dict['title'],
    'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",'comments':response_dict['descendants'],

}
submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts,key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")

#Explora a estrutura dos dados
response_dict = r.json()
response_string = json.dumps(response_dict,indent=4)
print(response_string)
