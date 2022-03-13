import csv
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.americanas.com.br/categoria/automotivo/moto/pecas-para-motos')

soup = BeautifulSoup(page.text, 'html.parser')
# Remover links inferiores
lista_produtos = soup.find().all_all(p)
for produto in lista_produtos:
  print(produto)