import csv
from bs4 import BeautifulSoup
import requests

page = requests.get('https://web.archive.org/web/20121010201041/http://www.nga.gov/collection/anZ4.htm')

soup = BeautifulSoup(page.text, 'html.parser')
# Remover links inferiores
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_ = 'BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Criar um arquivo para gravar, adicionar linha de cabeçalhos
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')


    # Adicionar em uma linha o nome de cada artista e o link associado
    f.writerow([names, links])