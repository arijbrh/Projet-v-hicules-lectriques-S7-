from flask import Flask
import pandas as pd
import numpy as np
from main import df1, df2, df3
import json
import folium
app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (42, 2)
    mode="departements"
    m = folium.Map(location=[45.5236, 2], zoom_start=6)
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
        name="bornes de recharge",
        data=dff,
        columns=["index", "counts"],
        key_on="properties.code",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="nombre de stations de recharge",
    ).add_to(m)

    folium.Choropleth(
    geo_data=france_depart,
    name="population",
    data=df3,
    columns=["CODDEP", "PTOT"],
    key_on="properties.code",
    fill_color="PuRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population",).add_to(m)

    folium.LayerControl().add_to(m)
    return m._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)