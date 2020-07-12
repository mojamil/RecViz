# Hello, Flask!
from flask import Flask, render_template, request,redirect,url_for
from bokeh.embed import components
import sys
import os
sys.path.append("./utils")
from drawgraph import create_tabs,create_plot
from utils.discover import make_graph
import networkx as nx

app = Flask(__name__)




@app.route('/')
def plot():
    '''
        This route shows various network plots of the given or default
        list of titles. Upon getting a new list it will run the required
        scripts to create the plots 
    '''
    if len(request.args)!=0:
        listid=request.args.get('imdbl')
        os.system(f'python3 utils/genlist.py {listid}')
        os.system('python3 utils/genre_list.py')
        os.system('python3 utils/findrecs.py')
        return redirect(url_for('plot'))
    plot=create_tabs()
    script, div =components(plot)
    return render_template("network.html", script=script, div=div)
@app.route('/input')
def inp():
    '''
        This route has input for the list id in order to create
        a new network plot
    '''
    return render_template("input_data.html")

@app.route('/discover')
def disc():
    '''
        The discover route contains an input to find titles recommended
        for titles given by the user the titles are shown via a network
        graph. It stores this network graph in a gml file in order to 
        not have load times when refreshing. 
    '''
    if len(request.args)!=0:
        queries=[]
        for i in range(6):
            if request.args[f"title{i}"] != "":
                queries.append(request.args[f"title{i}"])
        if len(queries)>0:
            G=make_graph(queries)
            if G==None:
                return redirect(url_for('disc'))
            plot=create_plot(G,"discover")
            nx.write_gml(G,"utils/discover.gml")
        return redirect(url_for('disc'))
    else:
        G=nx.read_gml("utils/discover.gml")
        plot=create_plot(G,"discover")
    script, div =components(plot)
    return render_template("discover.html", script=script, div=div)

if __name__ == '__main__':
	app.run(debug=True)
