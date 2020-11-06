from bs4 import BeautifulSoup
import urllib.request
from scrap_glo_v4 import scraper_glo_sculpteo

keys =[]
definitions=[]
words=[]
scraper_glo_sculpteo(keys, definitions, words)

print(keys)
print(len(definitions))
print(len(words))