import requests
import os
from dotenv import load_dotenv
import html

load_dotenv()

nome = 'jennifer aniston'
autorizacao = os.getenv("tmdb_autorizacao")


def pessoa_id(nome, autorizacao):
    pessoa = html.escape(nome)
    headers = {"accept": "application/json", "Authorization": autorizacao}

    url1 = f"https://api.themoviedb.org/3/search/person?query={pessoa}"

    response1 = requests.get(url1, headers=headers)
    resposta1 = response1.json()

    if resposta1['results']:
        id_pessoa = resposta1['results'][0]['id']
    else:
        id_pessoa = 'erro'

    return id_pessoa


id_pessoa = pessoa_id(nome, autorizacao)


def filmografia_filme(autorizacao, id_pessoa):
    headers = {"accept": "application/json", "Authorization": autorizacao}

    url2 = f"https://api.themoviedb.org/3/discover/movie?with_cast={id_pessoa}"
    response2 = requests.get(url2, headers=headers)
    resposta2 = response2.json()
    pags = resposta2['total_pages']

    filmes = []

    for i in range(1, pags+1):
        url3 = f"https://api.themoviedb.org/3/discover/movie?with_cast={id_pessoa}&page={i}&include_adult=false&" \
               f"include_video=false&language=pt-BR"
        response3 = requests.get(url3, headers=headers)
        resposta3 = response3.json()

        for filme in resposta3['results']:
            filmes.append(filme['title'])

    return filmes


def filmografia_serie(autorizacao, id_pessoa):
    headers = {"accept": "application/json", "Authorization": autorizacao}

    url2 = f"https://api.themoviedb.org/3/person/{id_pessoa}/tv_credits?language=pt-BR"
    response2 = requests.get(url2, headers=headers)
    resposta2 = response2.json()

    series = []

    for serie in resposta2['cast']:
        series.append(serie['name'])

    return series


titulo = 'senhor dos anéis'
ano = '2003'


def genero(lista):
    dic_gen = {'28': 'Ação', '12': 'Aventura', '16': 'Animação', '35': 'Comédia', '80': 'Crime', '99': 'Documentário',
               '18': 'Drama', '10751': 'Família', '14': 'Fantasia', '36': 'História', '27': 'Terror',
               '10402': 'Musical', '9648': 'Mistério', '10749': 'Romance', '878': 'Ficção Científica', '53': 'Suspense',
               '10752': 'Guerra', '37': 'Faroeste'}

    gen = []

    for item in lista:
        for cod_genero in item:
            gen.append(dic_gen[str(cod_genero)])

    return gen


def info_filme(autorizacao, titulo, ano):
    # para procurar também pela pessoa, precisa verificar se os ids dos filmes achados pelo nome e estão na filmografia
    filme = html.escape(titulo)

    headers = {"accept": "application/json", "Authorization": autorizacao}

    url = f"https://api.themoviedb.org/3/search/movie?query={filme}&include_adult=false&language=pt-BR&primary_" \
          f"release_year={ano}"

    response = requests.get(url, headers=headers)
    resposta = response.json()
    titulos = resposta['results']

    lista_titulo = []
    lista_ano = []
    lista_genero = []
    lista_sinopse = []
    filmes = {}

    for filme in titulos:
        lista_titulo.append(filme['title'])
        lista_ano.append(filme['release_date'][0:4])
        lista_genero.append(filme['genre_ids'])
        lista_sinopse.append(filme['overview'])

    filmes['Título'] = lista_titulo
    filmes['Ano'] = lista_ano
    filmes['Gênero'] = genero(lista_genero)
    filmes['Sinopse'] = lista_sinopse

    return filmes


def info_serie(autorizacao, titulo, ano):
    serie = html.escape(titulo)

    headers = {"accept": "application/json", "Authorization": autorizacao}

    url = f"https://api.themoviedb.org/3/search/tv?query={serie}&include_adult=false&language=pt-BR&" \
          f"primary_release_year={ano}"

    response = requests.get(url, headers=headers)
    resposta = response.json()
    titulos = resposta['results']

    lista_titulo = []
    lista_ano = []
    lista_genero = []
    lista_sinopse = []
    filmes = {}

    for filme in titulos:
        lista_titulo.append(filme['title'])
        lista_ano.append(filme['release_date'][0:4])
        lista_genero.append(filme['genre_ids'])
        lista_sinopse.append(filme['overview'])

    filmes['Título'] = lista_titulo
    filmes['Ano'] = lista_ano
    filmes['Gênero'] = genero(lista_genero)
    filmes['Sinopse'] = lista_sinopse

    return filmes


filme = info_filme(autorizacao, titulo, ano)


def onde_assistir(id_filme, autorizacao):
    headers = {"accept": "application/json", "Authorization": autorizacao}

    url = f"https://api.themoviedb.org/3/movie/{id_filme}/watch/providers"

    response = requests.get(url, headers=headers)
    resposta = response.json()

    assista = resposta['results']['BR']

    comprar = []
    alugar = []
    assinatura = []
    assistir = {}

    for resultado in assista['flatrate']:
        assinatura.append(resultado['provider_name'])

    for resultado in onde_assistir['buy']:
        comprar.append(resultado['provider_name'])

    for resultado in onde_assistir['rent']:
        alugar.append(resultado['provider_name'])

    assistir['Compre'] = comprar
    assistir['Assine'] = assinatura
    assistir['Alugue'] = alugar

    return assistir

