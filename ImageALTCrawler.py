from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

pages = set()


def getLinks(Url):
    global pages
    exampleFile = open('imageAltdoc.csv', 'w', newline='')
    exampleReader = csv.writer(exampleFile)
    exampleReader.writerow(['image source', 'alt'])

    # Open th    e URL
    Link_one = urlopen("https://ahrefs.com" + Url)
    # Use beautifulSoup to get the HTML Code
    Cont_HTML = BeautifulSoup(Link_one)
    Images_No_ALT = Cont_HTML.findAll("img", alt=False)
    try:
        for image in Images_No_ALT:
            print(image["src"])
            image_ALT = (image["src"])
            exampleReader.writerow([image_ALT])
        exampleFile.close()
    except KeyError:
        print(" no alt but it's ok")
    # then research in the HTML Code ( tout les href qui commencent par "Wiki")
    for link in Cont_HTML.findAll("a", href=re.compile("^(/blog/)")):
        # si il y a un href dans les liens on continue à l'interieur
        if 'href' in link.attrs:
            # si link.attrs n'a pas href dans le set()
            if link.attrs['href'] not in pages:
                # alors Resultat_2 devient link.attrs(href)
                Res_two = link.attrs['href']
                # je print le résultat 2
                # j'ajoute le résultat 2 dans les set
                pages.add(Res_two)
                # et avec getlinks, je reprend le resultat2 pour le mettre comme argument
                getLinks(Res_two)


getLinks("")
