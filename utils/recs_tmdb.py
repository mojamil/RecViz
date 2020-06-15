import requests
key="35538ef41d68bc78e5db88a7286d6207"
def get_show_id(name):
    r=requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={key}&language=en-US&page=1&query={name}&include_adult=false")
    results=r.json()["results"][0]['id']
    return results

def get_rec(name):
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}/recommendations?api_key={key}&language=en-US&page=1")
    results=[x["name"] for x in r.json()["results"]]
    return results[:5]
def get_genres(name):
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}?api_key={key}&language=en-US")
    results=r.json()['genres']
    results=[x["name"] for x in results]
    return results
