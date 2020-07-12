import csv
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
from math import sqrt
from recs_tmdb import get_genres

def find_perfect(minv):
    '''
        Finds a perfect square less than or equal to maxv

            Parameters:
                minv(int): The minimum value the squared number needs to be
            Return:
                i(int): The square root of the perfect square that is less than or equal to the maximum value
    '''
    i=1
    while (i*i)<minv:
        i+=1
    return i
def get_vertices():
    '''
        Returns a networkx graph using the titles from recs.csv as the nodes
        and the recommedations for each title are used to create the edges.
        Each node has the additonal property of genre(the primary genre of 
        the show) and position generated based on that genre

            Return:
                G (networkx graph): The graph that has been described above
                sidel (int) : The size of the grid
    '''
    genredict={}
    with open("utils/genres.json") as fp:
        genredict=json.load(fp)
    genres=set()
    for genre in genredict.keys():
        genres.add(genredict[genre][0])
    genres=list(genres)
    # This part divides the grid into an even number of squares
    # based on how many genres there are some squares are empty
    # as dividing the grid evenly requires a perfect square 
    # number of squares
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
    # This part creates the nodes and edges while adding the genres as a property
    fil=open("utils/recs.csv","r")
    data=csv.DictReader(fil)
    for row in data:
        G.add_node(row["title"],name=row["title"],genre=genredict[row["title"]][0])
        for entry in row.values():
            if entry!=None and entry!=row["title"]:
                if entry not in G.nodes:
                    G.add_node(entry,name=entry,genre=genredict[row["title"]][0])
                G.add_edge(row["title"],entry)
    # Each node is positioned randomly inside the square that
    # their genre was allocated
    for node in G.nodes:
        xran=ranges[G.nodes[node]['genre']]['x']
        yran=ranges[G.nodes[node]['genre']]['y']
        xcord=(random.random()*0.5)+xran[0]
        ycord=(random.random()*0.5)+yran[0]
        G.nodes[node]['pos']=[xcord,ycord]
    fil.close()
    return [G,sidel]
