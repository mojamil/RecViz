import requests
import json
from recs_tmdb import get_genres
'''
    This script gets the genres for each title in data.txt
    It think writes those genres into a json file
'''
key=""
genres={}
data=open("utils/data.txt","r")
titles=data.read().splitlines()
for title in titles:
    genres[title.replace(",","")]=get_genres(title)
data.close()
genre_json=json.dumps(genres,indent=4)
fp=open("utils/genres.json","w")
fp.write(genre_json)
