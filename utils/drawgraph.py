import networkx as nx

from bokeh.io import output_file, show, curdoc
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,
                          EdgesAndLinkedNodes,NodesAndLinkedEdges, TapTool,
                          BoxSelectTool, ColumnDataSource,CustomJSTransform, LabelSet,
                          WheelZoomTool)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx
from bokeh.transform import transform  
from makegraph import get_vertices

def create_plot():
    G=get_vertices()
    # data={"names":[]}
    # for node in G.nodes:
    #     data["names"].append(G.nodes[node]['name'])
    # source = ColumnDataSource(data=data)

    plot = Plot(plot_width=1200, plot_height=600,
                x_range=Range1d(-2.1, 2.1), y_range=Range1d(-2.1, 2.1))
    plot.title.text = "TV Shows Connected By Recommendation"

    pos_dict={}
    for node in G.nodes:
        pos_dict[node]=G.nodes[node]["pos"]

    graph_renderer = from_networkx(G, nx.kamada_kawai_layout, scale=2, center=(0, 0))

    graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
    graph_renderer.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[3])
    graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[2])
    graph_renderer.node_renderer.glyph.properties_with_values()

    graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.9, line_width=2)
    graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[3], line_width=2)
    graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[2], line_width=2)

    graph_renderer.selection_policy = NodesAndLinkedEdges()
    graph_renderer.inspection_policy = NodesAndLinkedEdges()
    source = graph_renderer.node_renderer.data_source
    source.data['name'] = [x for x in source.data['index']]

    # e_source=graph_renderer.edge_renderer.data_source
    # e_source.data["name"]=[]
    # for i in range(len(e_source.data["start"])):
    #     start=e_source.data['start'][i]
    #     end=e_source.data['end'][i]
    #     string=f"{start} to {end}"
    #     e_source.data["name"].append(string)

    node_hover_tool = HoverTool(tooltips=[ ("", "@name") , ("","@genre")])
    plot.add_tools(node_hover_tool, WheelZoomTool(),TapTool(), BoxSelectTool())

    plot.renderers.append(graph_renderer)
    return plot
