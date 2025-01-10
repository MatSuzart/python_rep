import request
import plotly.express as px
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
repo_links, stars,houver_texts = [],[],[]
print(f"Repositories returned:{len(repo_dicts)}")
print("\nSelected information about first repository:")

repo_names,stars,hover_texts = [],[]

for repo_dict in repo_dicts:
    #Transforma os nomes dos repositórios em links ativos
    repo_name=repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_links)


    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    #Cria textos flutuantes
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_texts = f"{owner}<br/>{description}"
    hover_texts.append(hover_texts)
    #Cria a visualização
    title = "Most-Starred Python Projects on GitHub"
    labels = {'x':'Repository', 'y':'Stars'}
    fig = px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)
    #fig = px.bar(x=repo_names,y=stars, title= title, labels=labels,haver_name=hover_texts)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20,yaxis_title_font_size=20)
    fig.update_traces(maker_color='SteelBlue',maker_opacity=0.6)
    fig.show()

    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Description:{repo_dict['description']}")
#examina o primeiro repositório
repo_dicts = repo_dicts[0]
print(f"\nKeys:{len(repo_dicts)}")
for key in sorted(repo_dicts.keys()):
    print(key)
#Processa os resultados
print(response_dict.keys())
