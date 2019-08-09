import requests
from bs4 import BeautifulSoup
import re

url = 'https://fotografiska.com/sto/en/experience/exhibitions/'
r = requests.get(url)
print(r)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text,'lxml')
for a in soup.find_all('a'):
    link = a['href']
    if (re.match(r'^(.*)/exhibition/latent', link)):
        # print(link)
        exhibition = requests.get(link)
        exhibition.encoding = 'utf-8'
        soupExhibition = BeautifulSoup(exhibition.content,'lxml')
        # print(soupExhibition.prettify())

        # print(soupExhibition.title.string)
        for hero in soupExhibition.find_all(class_ = "hero__content"):
            print(hero)
            print(hero.find_all(class_ = "container"))
            print(hero.find_all(class_ = "small"))

print()
