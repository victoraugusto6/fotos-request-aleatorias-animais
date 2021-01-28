import requests


def busca_cachorro():
    """
    Busca a foto de um cachorro utilizando a API 'Dog API'
    :return: Link com foto de algum cachorro
    """

    link = 'https://dog.ceo/api/breeds/image/random'
    foto = requests.get(link)
    return foto.json()['message']


def busca_gato():
    """
    Busca a foto de um gato utilizando a API 'TheCatApi'
    :return: Link com foto de algum gato
    """
    link = 'https://api.thecatapi.com/v1/images/search'
    foto = requests.get(link)
    return foto.json()[0]['url']


if __name__ == '__main__':
    print(busca_cachorro())
    print(busca_gato())
