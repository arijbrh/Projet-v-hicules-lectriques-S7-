import pandas as pd
import numpy as np
import plotly.express as px
from main import df1, df2, df3
import json
# import plotly.io as pio
# pio.renderers.default = 'chrome'
def graph_nbre_pdc():
    dff=pd.DataFrame(df1.groupby(['nbre_pdc']).size())
    dff=dff.drop(dff.index[20:])
    #print(dff)
    fig=px.bar(dff, x=dff.index, y=dff.columns)
    fig.show()
    return fig

#graph_nbre_pdc()

def map_stations(mode="departements"):
    france_depart=json.load(open("{}.geojson".format(mode), 'r'))
    df1['id']=df1['code_insee_commune']
    def clean(x):
        x= x[0:2]
        return x
    df1['id']=df1['id'].apply(clean)
  
    dff=df1['id'].value_counts().reset_index(name='counts')
    dff['scalecount']=np.log10(dff['counts'])
    print(dff)

    print(france_depart['features'][0]['properties'])
    fig=px.choropleth(dff, locations='index', featureidkey='properties.code', geojson=france_depart, color='scalecount', scope='europe', color_continuous_scale="Viridis",labels={'scalecount': 'log of the number of charging stations'})
    fig.show()
    return fig 

#map_stations()

def map_population(mode="departements"):
    france_depart=json.load(open("{}.geojson".format(mode), 'r'))
    

    print(france_depart['features'][0]['properties'])
    fig=px.choropleth(df3, locations='CODDEP', featureidkey='properties.code', geojson=france_depart, color='PTOT', scope='europe',labels={'PTOT': 'Population'})
    fig.show()
    return fig 
map_population()
