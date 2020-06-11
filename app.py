import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from dash.dependencies import Input, Output
from drawgraph import fig

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(id='basic-interactions',figure=fig),
    html.Div([
            dcc.Markdown("""
                **Hover Data**

                Mouse over values in the graph.
            """),
            html.Pre(id='hover-data')
        ], className='three columns')
],)

@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_click_data(hoverData):
    return json.dumps(hoverData, indent=2)
if __name__ == '__main__':
    app.run_server(debug=True)