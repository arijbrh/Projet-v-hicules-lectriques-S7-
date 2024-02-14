from flask import Flask
import pandas as pd
import numpy as np
from data import  df3, df4, df5
from scoring import df1
import json
import folium
app = Flask(__name__)
data_path_raw = "./TMJA2019.shp"
data_path_trd = "./TMJA2019.geojson"
with open(data_path_trd) as f:
    data = json.load(f)["features"]
for flux_ in data:
    flux_["geometry"]["coordinates_corr"] = []
    for coordinates_ in flux_["geometry"]["coordinates"]:
        if isinstance(coordinates_[0], list):
            for coord_ in coordinates_:
                flux_["geometry"]["coordinates_corr"].append([coordinates_[1], coordinates_[0]])
        else:
            flux_["geometry"]["coordinates_corr"].append([coordinates_[1], coordinates_[0]])
@app.route('/')
def index():
    start_coords = (42, 2)
    mode="departements"
    m = folium.Map(location=[45.5236, 2], zoom_start=6)
    m.add_child(folium.LatLngPopup())
    france_depart=json.load(open("{}.geojson".format(mode), 'r'))
    
    
    folium.Choropleth(
        geo_data=france_depart,
        name="bornes de recharge",
        data=df1,
        columns=["depart", "nbre_pdc"],
        key_on="properties.code",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="nombre de stations de recharge",
        show=False
    ).add_to(m)

    c1=folium.Choropleth(
    geo_data=france_depart,
    name="population ",
    data= df3,
    columns=["depart", "PTOT"],
    key_on="properties.code",
    fill_color="OrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="population ",show=False)
    for key in c1._children:
        if key.startswith('color_map'):
            del(c1._children[key])
    c1.add_to(m)


    c2=folium.Choropleth(
    geo_data=france_depart,
    name="vehicules ",
    data=df4 ,
    columns=["depart", "nb_vp"],
    key_on="properties.code",
    fill_color="Oranges",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="vehicules ",show=False)
    for key in c2._children:
        if key.startswith('color_map'):
            del(c2._children[key])
    c2.add_to(m)


    folium.Choropleth(
    geo_data=france_depart,
    name="vehicules_elec",
    data=df4,
    columns=["depart", "nb_vp_rechargeables_el"],
    key_on="properties.code",
    fill_color="Reds",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="vehicules electriques",show=False).add_to(m)


    c3=folium.Choropleth(
    geo_data=france_depart,
    name="traffic ",
    data=df5 ,
    columns=["depart", "TMJA"],
    key_on="properties.code",
    fill_color="OrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="traffic ",show=False)
    for key in c3._children:
        if key.startswith('color_map'):
            del(c3._children[key])
    c3.add_to(m)


    c4=folium.Choropleth(
    geo_data=france_depart,
    name="nombre de stations par traffic ",
    data=df5 ,
    columns=["depart", "metric"],
    key_on="properties.code",
    fill_color="Blues",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="charging stations/traffic ",show=False)
    for key in c4._children:
        if key.startswith('color_map'):
            del(c4._children[key])
    c4.add_to(m)


    folium.Choropleth(
        geo_data=france_depart,
        name="scoring",
        data=df1,
        columns=["depart", "score"],
        key_on="properties.code",
        fill_color="RdPu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="scoring",show=False
    ).add_to(m)

    c=folium.Choropleth(
    geo_data=france_depart,
    name="gdp",
    data=df1,
    columns=["depart", "gdp"],
    key_on="properties.code",
    fill_color="OrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="gdp",show=False)
    for key in c._children:
        if key.startswith('color_map'):
            del(c._children[key])
    c.add_to(m)

    

    #first method
    #folium.GeoJson("TMJA2019.geojson", name="trafficlines").add_to(m) 
    
    route_layer= folium.FeatureGroup(name="route layer")

    for flux_ in data:
        tooltip = f"""Route {flux_["properties"]["route"]} <br> TMJA: {flux_["properties"]["TMJA"]} """
        folium.PolyLine(locations=flux_["geometry"]["coordinates_corr"],
        tooltip=tooltip,
        weight=2, color='blue').add_to(route_layer)
    
    route_layer.add_to(m)


    folium.LayerControl().add_to(m)
    return m._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)

    """ci=folium.Choropleth(
    geo_data=france_depart,
    name=" ",
    data= ,
    columns=["depart", " "],
    key_on="properties.code",
    fill_color="OrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=" ",show=False)
    for key in ci._children:
        if key.startswith('color_map'):
            del(ci._children[key])
    ci.add_to(m)"""