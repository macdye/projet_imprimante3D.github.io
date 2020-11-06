import requests
import bs4
import re
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

response = requests.get('https://www.makershop.fr/content/43-guide-achat-filament-resine-impression-3d')
soup_filament = BeautifulSoup(response.text, 'html.parser')
block = soup_filament.find('div', attrs={'class': 'rte'})
ohledico = []
for liste in block:
	datafils = {}
	base = "Rien"
################################ ICI ON RECUP LES TITRES STP
	try:
		base = liste.find('div', attrs={'class' : 'col-xs-12'})
		datafils['titre'] = base.find('h2')
	except:
		pass
################################ ICI ON RECUP LES TEXTES SI çA MARCHE
	try:
		base = liste.find('div', attrs={'class' : 'col-xs-12'})
		datafils['speech'] = base.find_all('p')
	except:
		pass
################################ ICI ON RECUP LES TEMPERATURES
	try:
		base = liste.find('ul', attrs={'list-details list-unstyled'})
		base = base(list)
		datafils['extrusion'] = base[0].text
		datafils['plateau'] = base[2].text
		datafils['vitesse'] = base[4].text
	except:
		pass
	ohledico.append(datafils)
#print(ohledico)

datatest = pd.DataFrame(ohledico)
print(datatest)

datatest.to_csv(r'scrap_filaments.csv')

#print('==============================================================================')
#print("Filament >", titre)
# print('==============================================================================')
# print("Description >", speech)
# print('==============================================================================')
# print("Data temp. extrusion >", extrusion)
# print("Data temp. plateau >", plateau)
# print("Data vitesse impr. >", vitesse)