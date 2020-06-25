import requests
key="35538ef41d68bc78e5db88a7286d6207"
def get_show_id(name):
    r=requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={key}&language=en-US&page=1&query={name}&include_adult=false")
    if len(r.json()['results'])==0:
        return None
    results=r.json()["results"][0]['id']
    return results
def get_title(name):
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}?api_key={key}&language=en-US")
    return r.json()['name']
def get_rec_tv(name):
    idno=get_show_id(name)
    if not idno:
        return None
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}/recommendations?api_key={key}&language=en-US&page=1")
    results=[x["name"] for x in r.json()["results"]]
    return results[:5]

def get_rec_tv_dis(name):
    idno=get_show_id(name)
    if not idno:
        return None
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}/recommendations?api_key={key}&language=en-US&page=1")
    results=[x["name"] for x in r.json()["results"]]
    return results[:10]

def get_rec_movies(name):
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/movie/{idno}/recommendations?api_key={key}&language=en-US&page=1")
    if 'status_code' in r.json().keys() and r.json()['status_code']==34:
        return []
    results=[x["title"] for x in r.json()["results"]]
    
    return results[:5]
def get_genres(name):
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}?api_key={key}&language=en-US")
    if 'genres' not in r.json().keys():
        return ["none"]
    results=r.json()['genres']
    results=[x["name"] for x in results]
    return results

def get_genres_movie(name):
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/movie/{idno}?api_key={key}&language=en-US")
    results=r.json()['genres']
    results=[x["name"] for x in results]
    return results
