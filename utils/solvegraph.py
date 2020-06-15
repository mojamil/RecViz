import networkx as nx
from makegraph import get_vertices
G=get_vertices()

visited=[]
for i in range(len(G.nodes)):
    visited.append(0)

for node in G.nodes():
    order=[]
    #find_path(order,node)

def find_path(l,n):
    visited[visited.index(n)]=1
    edges=G.edges(n)
    return None