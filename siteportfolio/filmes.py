import requests
from imdb import Cinemagoer
import os
from dotenv import load_dotenv

load_dotenv()

ia = Cinemagoer()

campo_pessoa = 'brad pitt'
pessoa = campo_pessoa.replace(' ', '%20')

url = f"https://api.themoviedb.org/3/search/person?query={pessoa}"

autorizacao = os.getenv("tmdb_autorizacao")

headers = {"accept": "application/json", "Authorization": autorizacao}

response = requests.get(url, headers=headers)
resposta_pessoa = response.json()

id_pessoa = resposta_pessoa['results'][0]['id']

# filmes_gen = {'Action': 28, 'Adventure': 12, 'Animation': 16, 'Comedy': 35, 'Crime': 80, 'Documentary': 99,
#               'Drama': 18, 'Family': 10751, 'Fantasy': 14, 'History': 36, 'Horror': 27, 'Music': 10402,
#               'Mystery':9648, 'Romance': 10749, 'Science Fiction': 878, 'Thriller': 53, 'War': 10752, 'Western': 37}

ano = 2008
id_genero = 28

url = f"https://api.themoviedb.org/3/discover/movie?with_cast={id_pessoa}&year={ano}&with_genres={id_genero}"

headers = {"accept": "application/json", "Authorization": autorizacao}

res = requests.get(url, headers=headers)
resposta_final = res.json()

print(resposta_final)






def filmografia(nome):
    pessoa = ia.search_person(nome)
    id_pessoa = pessoa[0].personID
    person_id = ia.get_person(id_pessoa)
    filmes = person_id['filmography']['actor']  # lista de filmes
    return filmes
