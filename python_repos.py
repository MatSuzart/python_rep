import request

#Cria uma chamada de API e verifica a resposta
url = "https://api.github.com/search/repositories"
url +="?language:python+sort:stars+stars:>1000"

headers = {"Accept":"application/vnd.github.v3+json"}
r = request.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#Converte o objeto de resposat em um dicionário
response_dict = r.json()
print(f"Status code: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

#examina o primeiro repositório
repo_dicts = repo_dicts[0]
print(f"\nKeys:{len(repo_dicts)}")
for key in sorted(repo_dicts.keys()):
    print(key)
#Processa os resultados
print(response_dict.keys())
