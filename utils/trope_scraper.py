import requests
from bs4 import BeautifulSoup
def get_show(name):
    link=f"https://tvtropes.org/pmwiki/pmwiki.php/Series/{name}".replace(" ","")
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    tropes= soup.find_all('a',class_="twikilink")
    tropelist=[]
    for trope in tropes:
        if "Main" in trope["href"]:
            tropelist.append(trope["href"].split("/")[-1])
    return set(tropelist)
def trope_compare(name1,name2):
    match_count=0
    tropes_1=get_show(name1)
    tropes_2=get_show(name2)
    larger=tropes_1
    smaller=tropes_2
    if len(tropes_1)<len(tropes_2):
        larger=tropes_2
        smaller=tropes_1
    for trope in larger:
        if trope in smaller:
            match_count+=1
    return match_count


