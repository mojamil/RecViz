import csv
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
def get_vertices():
    G=nx.Graph()
    fil=open("recs.csv","r")
    data=csv.DictReader(fil)
    for row in data:
        posx=random.random()
        posy=random.random()
        G.add_node(row["title"],pos=[posx,posy])
        
        for entry in row.values():
            if entry!=None and entry!=row["title"]:
                if entry not in G.nodes:
                    posx=random.random()
                    posy=random.random()
                    G.add_node(entry,pos=[posx,posy])
                G.add_edge(row["title"],entry)
    fil.close()
    return G