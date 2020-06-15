import requests
import json
from recs_tmdb import get_genres
key="35538ef41d68bc78e5db88a7286d6207"
genres={}
data=open("data.txt","r")
titles=data.read().splitlines()
for title in titles:
    genres[title]=get_genres(title)
data.close()
genre_json=json.dumps(genres,indent=4)
fp=open("genres.json","w")
fp.write(genre_json)