
# import os
#
#
# def create_file():
#     f = open("guru99.txt", "w+")
#     os.mkdir('pizza_pictures')
#     f.close()
#
#
# create_file()


import requests
import bs4
import os


def pobieracz_obrazow(adres):
    strona = requests.get(adres)
    parser = bs4.BeautifulSoup(strona.text, 'html.parser')
    return parser.find_all('img')


def zapisywacz_obrazow(adres):
    try:
        os.mkdir('obrazki')
    except:
        pass
    strona = requests.get(adres)
    parser = bs4.BeautifulSoup(strona.text, 'html.parser')
    obrazki = parser.find_all('img')

    for obrazek in obrazki:
       adres_obrazka = obrazek.get('src')
       nazwa_obrazka = obrazek.get('alt')
       if nazwa_obrazka is not None:
            nazwa_obrazka = nazwa_obrazka.replace(' ', '-').replace('/', '')
            with open(f'obrazki/{nazwa_obrazka}.jpg', 'wb') as jpg:
                dane_obrazka = requests.get(adres_obrazka).content
                jpg.write(dane_obrazka)


