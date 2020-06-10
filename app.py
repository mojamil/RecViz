import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from drawgraph import fig

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)