import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://fotografiska.com/sto/en/experience/exhibitions/'
html = requests.get(url)
print(html)
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text,'lxml')

comments = []

links = []

for link in soup.findAll('a', attrs={'href': re.compile(r"^(.*)/exhibition/latent")}):
    links.append(link.get('href'))

# dedup the list of url containing diff. exhibitions
links = list(set(links))
# print(links)

for link in links:
    comment = {}

    # print(link)
    exhibition = requests.get(link)
    exhibition.encoding = 'utf-8'
    soupExhibition = BeautifulSoup(exhibition.content,'lxml')
    # print(soupExhibition.prettify())

    soupHead = soupExhibition.find(class_ = 'hero__content')

    comment['artist_name'] = soupHead.h2.string
    comment['exhibition_name'] = soupHead.h1.string
    comment['date'] = " ".join(soupHead.p.string.split())
    # comment['url'] = link

    # comment['exhibition_name'] = soupHead.find('i', attrs={'class': 'hero__content'}).text.strip()

    comments.append(comment)

    # print(soupExhibition.title.string)
    # for hero in soupExhibition.find_all(class_ = "hero__content"):
    #    print(hero)
    #    print(hero.find_all(class_ = "container"))
    #    print(hero.find_all(class_ = "small"))

df = pd.DataFrame(comments)
print(df)
df.to_csv('foto.csv', encoding='utf-8')
