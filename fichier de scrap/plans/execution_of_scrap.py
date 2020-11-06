from bs4 import BeautifulSoup
import urllib.request
import sys, time, threading

from scrap_animate import scraper
from clean_data_for_df import clean_data_from_scrap

objets = []
the_process = threading.Thread(name='process', target=scraper(objets))

list_object = []
clean_data_from_scrap(objets, list_object)