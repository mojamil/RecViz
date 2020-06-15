# Hello, Flask!
from flask import Flask, render_template, request
from bokeh.embed import components
import sys
sys.path.append("./utils")
from drawgraph import create_plot
app = Flask(__name__)


@app.route('/')
def plot():
    plot=create_plot()
    script, div =components(plot)
    return render_template("network.html", script=script, div=div)


if __name__ == '__main__':
	app.run(debug=True)
