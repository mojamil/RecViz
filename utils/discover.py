from recs_tmdb import get_rec_tv_dis,get_title
from recs_tastedive import get_recs_tv
import networkx as nx
from drawgraph import create_plot
import math
# key="373322-DiRecTre-D1E4Z4FG"
def get_titles_tastedive(queries,k):
    '''
    Returns 10 recommendations from tastedive per query and creates a 
    dicitonary linking the recommendations and queries.

        Parameters:
            queries (list of strings): Names of shows
            k (str) : API key for Tastedive
        Returns:
            titledict (dictionary of strings): The keys are the individual shows and the value is a list of recommendations for that show
    '''
    titles=set(queries)
    for query in queries:
        recs=get_recs_tv(query,k)
        titles.update(set(recs))
    titledict={}
    for title in titles:
        titledict[title]=[]
        recs=get_recs_tv(title,k)
        for rec in recs:
            if rec in titles:
                titledict[title].append(rec)
    return titledict
def get_titles_tmdb(queries):
    '''
    Returns 10 recommendations from tmdb per query and creates a 
    dicitonary linking the recommendations and queries.

        Parameters:
            queries (list of strings): Names of shows
        Returns:
            titledict (dictionary of strings): The keys are the individual shows and the value is a list of recommendations for that show
    '''
    titles=set(queries)
    for query in queries:
        titles.update(set(get_rec_tv_dis(query)))
    titledict={}
    for title in titles:
        titledict[title]=[]
        recs=get_rec_tv_dis(title)
        for rec in recs:
            if rec in titles:
                titledict[title].append(rec)
    return titledict
def make_graph(queries):
    '''
        Returns A networkx graph with postions of the query nodes positioned
        in a circle of radius 1 and the recommendations positioned in a circle
        of radius 2.
            Parameters:
                queries (list of strings): Names of shows
            Returns:
                G (networkx graph): Graph containing nodes connected by edges which represent recommendations
    '''
    queries=[get_title(x) for x in queries]
    if None in queries:
        return None
    titledict=get_titles_tmdb(queries)
    G=nx.Graph()
    for title in titledict.keys():
        if title in queries:
            G.add_node(title)
            for rec in titledict[title]:
                if rec not in G.nodes:
                    G.add_node(rec)
                G.add_edge(title,rec)
    '''
    The code below uses the number of titles to position them in a circle.
    The deltas are the angle seperation between each node 
    '''
    delta=(2*math.pi)/len(queries)
    angle1=0
    angle2=0
    delta2=(2*math.pi)/(len(titledict.keys())-len(queries))
    for query in queries:
        if len(queries)==1:
            posx=0
            posy=0
        else:
            posx=0.5*math.cos(angle1)
            posy=0.5*math.sin(angle1)
        G.nodes[query]['pos']=(posx,posy)
        angle1+=delta
        for title in titledict[query]:
            if title not in queries and 'pos' not in G.nodes[title]:
                posx=2*math.cos(angle2)
                posy=2*math.sin(angle2)
                G.nodes[title]['pos']=(posx,posy)
                angle2+=delta2
    return G