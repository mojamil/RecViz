import requests
def get_recs_tv(title,key):
    '''
        Returns a list of 10 recommendations for a tv show using the TasteDive API (https://tastedive.com/read/api)

            Parameters:
                title(string): The name of the show
                key(string): The API key for Tastedive (use the link above to acquire one)
            Return:
                recs(list of strings): A list of the recommedations for the show given
    '''
    r=requests.get(f"https://tastedive.com/api/similar?q=show:{title}&k={key}")
    results=r.json()["Similar"]["Results"]
    recs=[]
    maxl=10
    if(len(results)<10):
        maxl=len(results)
    for i in range(0,maxl):
        name=results[i]['Name']
        recs.append(name)
    return recs