import requests

key="35538ef41d68bc78e5db88a7286d6207" # Fill this in with your API key for tmdb (https://developers.themoviedb.org/3)
def get_show_id(name):
    '''
        The tmdb api requires an id to get more information about shows
        this function gets the id by using the title fo the show

            Parameters:
                name(string): name of the show
            Return:
                results(string): The id of the show if found
    '''
    r=requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={key}&language=en-US&page=1&query={name}&include_adult=false")
    if len(r.json()['results'])==0:
        return None
    results=r.json()["results"][0]['id']
    return results
def get_title(name):
    '''
        Gets the name for the show on tmdb as to avoid duplicates when getting recommendations

            Parameters:
                name(string): name of the show
            Return:
                t_name(string): The title of the show on tmdb
    '''
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}?api_key={key}&language=en-US")
    if not idno:
        return None
    t_name=r.json()['name']
    return t_name
def get_rec_tv(name):
    '''
        Returns a list of 5 recommendations for a tv show using the TMDb API (https://developers.themoviedb.org/3)

            Parameters:
                title(string): The name of the show
            Return:
                recs(list of strings): A list of the recommedations for the show given
    '''
    idno=get_show_id(name)
    if not idno:
        return None
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}/recommendations?api_key={key}&language=en-US&page=1")
    results=[x["name"] for x in r.json()["results"]]
    return results[:5]

def get_rec_tv_dis(name):
    '''
        Returns a list of 10 recommendations for a tv show using the TMDb API (https://developers.themoviedb.org/3)

            Parameters:
                title(string): The name of the show
            Return:
                recs(list of strings): A list of the recommedations for the show given
    '''
    idno=get_show_id(name)
    if not idno:
        return None
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}/recommendations?api_key={key}&language=en-US&page=1")
    results=[x["name"] for x in r.json()["results"]]
    return results[:20]

def get_genres(name):
    '''
        Gets the genres for the show as listed on tmdb

            Parameters:
                name(string): name of the show
            Return:
                results(string): The list of genres associated with that show according to tmdb
    '''
    idno=get_show_id(name)
    r=requests.get(f"https://api.themoviedb.org/3/tv/{idno}?api_key={key}&language=en-US")
    if 'genres' not in r.json().keys():
        return ["none"]
    results=r.json()['genres']
    results=[x["name"] for x in results]
    return results

