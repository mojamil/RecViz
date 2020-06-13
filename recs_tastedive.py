import requests
def get_recs(title,key):
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