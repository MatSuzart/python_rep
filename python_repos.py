import request

#Cria uma chamada de API e verifica a resposta
url = "https://api.github.com/search/repositories"
url +="?language:python+sort:stars+stars:>1000"

headers = {"Accept":"application/vnd.github.v3+json"}
r = request.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#Converte o objeto de resposat em um dicionário
response_dict = r.json()

#Processa os resultados
print(response_dict.keys())
