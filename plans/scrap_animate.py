from bs4 import BeautifulSoup
import urllib.request
import sys, time, threading

def scraper(empty_list = list):
    time.sleep(0.1)
    base_url = 'https://www.myminifactory.com/fr/search/fetch_search/'
    i = 1
    n = 351
    while i <= n :
        page = urllib.request.urlopen(base_url + f'?page={i}&sortBy=date&featured=1&store=0')
        soup = BeautifulSoup(page, 'lxml')
        a = soup.find('p')
        a_text = a.text
        splitty = a_text.split("{")
        for split in splitty:
            if len(split) == 0 :
                pass
            else:
                sign = []
                things = split.split(',')
                for thing in things:
                    if len(thing) == 0:
                        pass
                    elif thing == """"objectResults":[""" or thing == """"objectssaved":[]""" or thing == """"idsLiked":[]""" or thing == """"objectsInCart":[]}""" or thing == """"objectResults":[]""":
                        pass
                    else:
                        thing = thing.encode('ascii', 'ignore').decode('unicode_escape')
                        thing = thing.replace('\/\/','/')
                        thing = thing.replace('\/','/')
                        sign.append(thing)
                if len(sign) > 0:
                    empty_list.append(sign)
        #Petite boucle de loading
        animation = ["⺌ ∅‿‿∅⺌","⺌∅‿‿∅ ⺌"]
        sys.stdout.write('\r'+f'loading... {animation[i % len(animation)]}  process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
        sys.stdout.flush()
        i += 1
    sys.stdout.write('\r'+'loading... finished               \n')
    sys.stdout.write('\r'+f'la liste contient {len(empty_list)} element')