import csv
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
from math import sqrt
from recs_tmdb import get_genres

def find_perfect(minv):
    i=1
    while (i*i)<minv:
        i+=1
    return i
def get_vertices():
    genredict={}
    with open("utils/genres.json") as fp:
        genredict=json.load(fp)
    genres=set()
    for genre in genredict.keys():
        genres.add(genredict[genre][0])
    genres=list(genres)
    sidel=find_perfect(len(genres))
    sumarr=[-sidel/2]
    for i in range(1,1+sidel):
        sumarr.append(sumarr[i-1]+1)
    ranges={}
    i=0
    for y in range(len(sumarr)-1):
        for x in range(len(sumarr)-1):
            if i<len(genres):
                ranges[genres[i]]={}
                ranges[genres[i]]['x']=[sumarr[x],sumarr[x+1]]
                ranges[genres[i]]['y']=[sumarr[y],sumarr[y+1]]
                i+=1
    G=nx.Graph()
    fil=open("utils/recs.csv","r")
    data=csv.DictReader(fil)
    for row in data:
        G.add_node(row["title"],name=row["title"],genre=genredict[row["title"]][0])
        for entry in row.values():
            if entry!=None and entry!=row["title"]:
                if entry not in G.nodes:
                    G.add_node(entry,name=entry,genre=genredict[row["title"]][0])
                G.add_edge(row["title"],entry)
    for node in G.nodes:
        xran=ranges[G.nodes[node]['genre']]['x']
        yran=ranges[G.nodes[node]['genre']]['y']
        xcord=(random.random()*0.5)+xran[0]
        ycord=(random.random()*0.5)+yran[0]
        G.nodes[node]['pos']=[xcord,ycord]
    fil.close()
    return [G,sidel]
