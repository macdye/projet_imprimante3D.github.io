from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

urls = ['https://youtu.be/htRhj8RQIWM',
	'https://youtu.be/pu6bJwq60oc',
	'https://youtu.be/nEaD7phzoqY',
	'https://youtu.be/pGagwRiTBlo',
	'https://youtu.be/cbhbA2R9aZs',
	'https://youtu.be/6AbovudN1vc',
	'https://youtu.be/n10apuNtqR0',
	'https://youtu.be/ms4UiNGBI4o',
	'https://youtu.be/BujOFYG1VBY',
	'https://youtu.be/tNRM6URR8jI',
	'https://youtu.be/KHKdS5S6YMI',
	'https://youtu.be/Bl_10zzKB3g',
	'https://youtu.be/G8FMyk-5MWA',
	'https://youtu.be/SSBcoAa02AU',
	'https://youtu.be/18mRsGXq6hc',
	'https://youtu.be/55Sqk_tKf80',
	'https://youtu.be/GFSIS1juQlY',
	'https://youtu.be/d93bu-2rnOE',
	'https://youtu.be/NR6qbO3bFWs',
	'https://youtu.be/NsGcuY3tY2w']
session = HTMLSession()
test = []
for url in urls:
	response = session.get(url)
	response.html.render(sleep=1)
	soup = bs(response.html.html, "html.parser")
	result = {}
	try: # ON RECUPERE LE TITRE #################################
		result['titre'] = soup.title.text.replace(' - YouTube', '')
	except AttributeError:
		print('Oops I did it again')
	try: # ON RECUPERE LA DATE ##################################
		publi = soup.find("div", {"id": "date"})
		result['date'] = publi.text[1:]
	except AttributeError:
		try: # ON REESSAIE
			publi = soup.find("div", {"id": "date"})
			result['date'] = publi.text[1:]
		except AttributeError:
			result['date'] = 'NULL'
	try: # ON RECUPERE LA DURÉE #################################
		duration = soup.find("span", {"class": "ytp-time-duration"})
		result['durée'] = duration.text
	except AttributeError:
		try: # ON REESSAIE
			duration = soup.find("span", {"class": "ytp-time-duration"})
			result['durée'] = duration.text
		except AttributeError:
			result['durée'] = 'NULL'
	try: # ON RECUPERE LES TAGS #################################
		result['tags'] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])
	except AttributeError:
		print('Oops tags manquants')
	test.append(result)
#print(test)

datatest = pd.DataFrame(test)
#print(datatest)

#datatest.to_csv(r'scrap_ytbe.csv')