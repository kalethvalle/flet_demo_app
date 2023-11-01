import requests

def loadAnimes():
    url = 'https://kitsu.io/api/edge/anime?page[limit]=20&page[offset]=0'

    response = requests.get(url)
    return response.json()['data']

