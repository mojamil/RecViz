import requests
from bs4 import BeautifulSoup
def get_list(id):
    link=f"https://www.imdb.com/list/{id}"
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    headers= soup.find_all('h3', class_='lister-item-header')
    titles=[]
    for header in headers:
        titles.append(header.find('a').text)
    return titles