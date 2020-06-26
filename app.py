# Hello, Flask!
from flask import Flask, render_template, request,redirect,url_for
from bokeh.embed import components
import sys
import os
sys.path.append("./utils")
from drawgraph import create_tabs
from utils.discover import discover,make_graph
import networkx as nx

app = Flask(__name__)




@app.route('/')
def plot():
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
    return render_template("input_data.html")

@app.route('/discover')
def disc():
    if len(request.args)!=0:
        queries=[]
        for i in range(6):
            if request.args[f"title{i}"] != "":
                queries.append(request.args[f"title{i}"])
        if len(queries)>0:
            G=make_graph(queries)
            if G==None:
                return redirect(url_for('disc'))
            plot=discover(G)
            nx.write_gml(G,"utils/discover.gml")
        return redirect(url_for('disc'))
    else:
        G=nx.read_gml("utils/discover.gml")
        plot=discover(G)
    script, div =components(plot)
    return render_template("discover.html", script=script, div=div)

if __name__ == '__main__':
	app.run(debug=True)
