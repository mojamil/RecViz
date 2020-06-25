import networkx as nx

from bokeh.io import output_file, show, curdoc
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,
                          EdgesAndLinkedNodes,NodesAndLinkedEdges, TapTool,
                          BoxSelectTool, ColumnDataSource,CustomJSTransform, LabelSet,
                          WheelZoomTool,Select)
from bokeh.models.widgets import Panel, Tabs
from bokeh.palettes import Spectral4,inferno,viridis,Plasma11
from bokeh.plotting import from_networkx
from bokeh.transform import transform  
from makegraph import get_vertices

def create_plot(G,layout):
    
    # data={"names":[]}
    # for node in G.nodes:
    #     data["names"].append(G.nodes[node]['name'])
    # source = ColumnDataSource(data=data)
    if layout=="grouped" :
        G,sidel=get_vertices()
        hsidel=sidel/2
        plot = Plot(plot_width=1200, plot_height=600,
                    x_range=Range1d(-(hsidel+.1), hsidel+.1), y_range=Range1d(-(hsidel+.1), hsidel+.1),align='center')
    else:
        plot = Plot(plot_width=1200, plot_height=600,
                    x_range=Range1d(-2.1, 2.1), y_range=Range1d(-2.1,2.1),align='center')
    plot.title.text = "TV Shows Connected By Recommendation"
    plot.background_fill_color="black"
    plot.background_fill_alpha=0.1


    if layout=="grouped":
        pos_dict={}
        for node in G.nodes:
            pos_dict[node]=G.nodes[node]["pos"]
        graph_renderer = from_networkx(G, pos_dict, scale=hsidel, center=(0, 0))
    elif layout=="discover":
        pos_dict={}
        for node in G.nodes:
            pos_dict[node]=G.nodes[node]["pos"]
        graph_renderer = from_networkx(G, pos_dict, scale=2, center=(0, 0))
    else:
        graph_renderer = from_networkx(G, layout, scale=2, center=(0, 0))
    if len(G.nodes)>256:
        Inferno=[Spectral4[1]]*len(G.nodes)-256
        Inferno.extend(viridis(len(G.nodes)))
    else:
        Inferno=list(viridis(len(G.nodes)))
    source = graph_renderer.node_renderer.data_source
    nodes=graph_renderer.node_renderer
    edges=graph_renderer.edge_renderer
    source.data['name'] = [x for x in source.data['index']]
    source.data['colors']=Inferno
    nodes.glyph = Circle(size=15, fill_color='colors', fill_alpha=0.9,line_color='colors')
    nodes.selection_glyph = Circle(size=15, fill_color=Plasma11[10], fill_alpha=0.8)
    nodes.hover_glyph = Circle(size=15, fill_color=Plasma11[9])
    nodes.glyph.properties_with_values()

    edges.glyph = MultiLine(line_color="black", line_alpha=0.1, line_width=2)
    edges.selection_glyph = MultiLine(line_color=Plasma11[10], line_width=2)
    edges.hover_glyph = MultiLine(line_color=Plasma11[9], line_width=2)

    graph_renderer.selection_policy = NodesAndLinkedEdges()
    graph_renderer.inspection_policy = NodesAndLinkedEdges()
    #graph_renderer.selection_policy = EdgesAndLinkedNodes()


    # e_source=graph_renderer.edge_renderer.data_source
    # e_source.data["name"]=[]
    # for i in range(len(e_source.data["start"])):
    #     start=e_source.data['start'][i]
    #     end=e_source.data['end'][i]
    #     string=f"{start} to {end}"
    #     e_source.data["name"].append(string)
    if layout=="grouped":
        node_hover_tool = HoverTool(tooltips=[ ("", "@name") , ("","@genre")])
    else:
        node_hover_tool = HoverTool(tooltips=[ ("", "@name")])
    plot.add_tools(node_hover_tool, WheelZoomTool(),TapTool(), BoxSelectTool())

    plot.renderers.append(graph_renderer)
    return plot

def create_tabs():
    plot1=create_plot(get_vertices()[0],layout="grouped")
    tab1 = Panel(child=plot1, title="Grouped by Category")
    plot2=create_plot(get_vertices()[0],nx.kamada_kawai_layout)
    tab2 = Panel(child=plot2, title="Kamada Kawai Layout")
    plot3=create_plot(get_vertices()[0],nx.circular_layout)
    tab3 = Panel(child=plot3, title="Circular Layout")
    plot2=create_plot(get_vertices()[0],nx.spiral_layout)
    tab4 = Panel(child=plot2, title="Spiral Layout")
    tabs= Tabs(tabs=[ tab1, tab2, tab3, tab4 ])
    return tabs