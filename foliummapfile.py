import folium
import pandas as pd
import numpy as np
import plotly.express as px
from data import df1, df2
import json
def foliummap():
    mode="departements"
    m = folium.Map(location=[45.5236, 2])
    m.add_child(folium.LatLngPopup())
    france_depart=json.load(open("{}.geojson".format(mode), 'r'))
    df1['id']=df1['code_insee_commune']
    def clean(x):
        x= x[0:2]
        return x
    df1['id']=df1['id'].apply(clean)
  
    dff=df1['id'].value_counts().reset_index(name='counts')
    dff['scalecount']=np.log10(dff['counts'])
    
    folium.Choropleth(
        geo_data=france_depart,
        name="choropleth",
        data=dff,
        columns=["index", "scalecount"],
        key_on="properties.code",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Unemployment Rate (%)",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m 

