import requests as rq
from bs4 import BeautifulSoup

def downloaddlinks():
    link = input("input link")
    if 'http' or 'https' in link:
        data = rq.get(link)
    else:
        data= rq.get('https' + link)

        soup = BeautifulSoup(data.text, 'html.perser')
        links = []
        for lnk in soup.get_all('a'):
            links.append(lnk.get('href'))

        with open('links.text', 'a') as  tobesaved:
            print(links[0:10], file = tobesaved)

downloaddlinks()
