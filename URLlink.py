#extract Links

import requests, bs4, re

def extract_Links (link):
    
  res = requests.get(link)
  Cont_HTML = bs4.BeautifulSoup(res.text)
  linkRegex = "^" + link
  for link in Cont_HTML.findAll('a', attrs={'href': re.compile(linkRegex)}):
    print (link.get("href"))

extract_Links ("http://www.example.com/")
	
