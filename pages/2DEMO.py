import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

#Plaques data
plaques_df = gpd.read_file("plaques_commemoratives_1939-1945.geojson")
plaques = gpd.GeoDataFrame(plaques_df)
arr = [p is None for p in plaques['geometry']]
np.isfinite(arr)

plaques = plaques[~pd.isnull(plaques['geometry'])]
# Create a folium map
demo_map = folium.Map([48.8566, 2.3522], zoom_start=12)

# Create a MarkerCluster layer
plaques_mc = MarkerCluster(name='plaques', show=True)

# Add markers to the MarkerCluster layer
for idx, row in plaques.iterrows():
    coords = list(row['geometry'].coords)[0]
    marker = folium.Marker(location=[coords[1], coords[0]], icon = folium.Icon(color = 'red', icon='image', prefix = 'fa'))
    marker.add_child(folium.Popup(row['commemore']))
    marker.add_to(plaques_mc)

# Add the MarkerCluster layer to the map
plaques_mc.add_to(demo_map)

# Add layer control to the map
folium.LayerControl().add_to(demo_map)

# Show the map
st_data = st_folium(demo_map, width=725)