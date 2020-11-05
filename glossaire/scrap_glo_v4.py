from bs4 import BeautifulSoup
import urllib.request
import sys, time, threading

def scraper_glo_sculpteo(list_for_key = list, list_for_text = list, list_for_words = list):
    url = 'https://www.sculpteo.com/fr/glossaire/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find_all('div',attrs={'class':'elementor-row'})
    i = 0
    n=219
    for row in rows:
        columns = row.find_all('div', attrs={'class':'elementor-column-wrap elementor-element-populated'})
        for column in columns:
            links = column.find_all('a')
            for link in links:
                
                a = link.text.strip()
                if i < 27:
                    list_for_key.append(a)
                    i +=1
                else:
                    url = link['href']
                    p = urllib.request.urlopen(url)
                    soupe = BeautifulSoup(p, 'html.parser')
                    text = soupe.find_all('div', attrs={'class':'elementor-section-wrap'})
                    for t in text:
                        paraph = t.text.replace('\n',' ')
                        list_for_text.append(paraph)
                    dict_words = {}
                    dict_words['words'] = a
                    list_for_words.append(dict_words)
                l = len(list_for_key) + len(list_for_text) + len(list_for_words)
                animation = ["⺌.⺌","⺌,⺌","⺌:⺌","⺌'⺌","⺌°⺌"]
                sys.stdout.write('\r'+f'loading... {animation[l % len(animation)]}  process '+str(l)+'/'+str(n)+' '+ '{:.2f}'.format(l/n*100)+'%')
                sys.stdout.flush()
    sys.stdout.write('\r'+'loading... finished               \n')

