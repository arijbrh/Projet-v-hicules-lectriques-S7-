import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import graphs as g

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2('electrical charging stations in France dashboard'),
    dcc.RadioItems(id='regions',options=['departements','communes'],value='departements',inline=True),
    dcc.Graph(id='map',figure=g.map())
]) 


@app.callback(
    Output(component_id='map', component_property='figure'),
    Input(component_id='regions',component_property='value')
)

if __name__=='__main__':
    app.run_server(debug=True)