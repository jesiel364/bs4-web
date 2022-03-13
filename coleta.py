import csv
from bs4 import BeautifulSoup
import requests


print('Loading...')
try:
	page = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
except:
	print('Erro ao carregar a página.')
	exit()


soup = BeautifulSoup(page.text, 'html.parser')



refs = soup.find(_class='reference internal')
refs = refs.decompose()

print(refs)
exit()

title = soup.title
print(title) # Recuperando title
	# Remover links inferiores	
lista = soup.find('p')

for item in lista:
	print(item)