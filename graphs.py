import pandas as pd
import numpy as np
import plotly.express as px
from data import df3, df4
from scoring import df1
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

def clean(x):
    y=x[0:2]
    return y
def vehicle_map(mode="departements"):
    dff=df4
    dff.drop_duplicates(subset="codgeo", keep='last', inplace=True)
    dff["depart"]=dff["codgeo"]
    
    dff["depart"]=dff["depart"].apply(clean)
    dff=dff.groupby("depart").sum()

    return dff.head()
df1['names']=[
    "Ain",
    "Aisne",
    "Allier",
    "Alpes de Haute-Provence",
    "Hautes-Alpes",
    "Alpes-Maritimes",
    "Ardêche",
    "Ardennes",
    "Ariège",
    "Aube",
    "Aude",
    "Aveyron",
    "Bouches-du-Rhône",
    "Calvados",
    "Cantal",
    "Charente",
    "Charente-Maritime",
    "Cher",
    "Corrèze",
    "Corse-du-Sud & Haute-Corse",
    "Côte-d'Or",
    "Côtes d'Armor",
    "Creuse",
    "Dordogne",
    "Doubs",
    "Drôme",
    "Eure",
    "Eure-et-Loir",
    "Finistère",
    "Gard",
    "Haute-Garonne",
    "Gers",
    "Gironde",
    "Hérault",
    "Île-et-Vilaine",
    "Indre",
    "Indre-et-Loire",
    "Isère",
    "Jura",
    "Landes",
    "Loir-et-Cher",
    "Loire",
    "Haute-Loire",
    "Loire-Atlantique",
    "Loiret",
    "Lot",
    "Lot-et-Garonne",
    "Lozère",
    "Maine-et-Loire",
    "Manche",
    "Marne",
    "Haute-Marne",
    "Mayenne",
    "Meurthe-et-Moselle",
    "Meuse",
    "Morbihan",
    "Moselle",
    "Nièvre",
    "Nord",
    "Oise",
    "Orne",
    "Pas-de-Calais",
    "Puy-de-Dôme",
    "Pyrénées-Atlantiques",
    "Hautes-Pyrénées",
    "Pyrénées-Orientales",
    "Bas-Rhin",
    "Haut-Rhin",
    "Rhône",
    "Haute-Saône",
    "Saône-et-Loire",
    "Sarthe",
    "Savoie",
    "Haute-Savoie",
    "Paris",
    "Seine-Maritime",
    "Seine-et-Marne",
    "Yvelines",
    "Deux-Sèvres",
    "Somme",
    "Tarn",
    "Tarn-et-Garonne",
    "Var",
    "Vaucluse",
    "Vendée",
    "Vienne",
    "Haute-Vienne",
    "Vosges",
    "Yonne",
    "Territoire-de-Belfort",    "Essonne",    "Hauts-de-Seine",    "Seine-Saint-Denis",    "Val-de-Marne",    "Val-d'Oise",    "Guadeloupe"]
df = px.data.tips()
# Here we use a column with categorical data
fig = px.scatter(df1, x="depart", y="score", text="names")
fig.update_traces(textposition='top center')
fig.show()