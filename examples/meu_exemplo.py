import folium
from folium.plugins import MarkerCluster
import pandas as pd
import json
import requests
url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
)
# vis1 = json.loads(requests.get(f"{url}/vis1.json").text)
# vis2 = json.loads(requests.get(f"{url}/vis2.json").text)
# vis3 = json.loads(requests.get(f"{url}/vis3.json").text)


#Define coordinates of where we want to center our map
# boulder_coords = [40.015, -105.2705]
boulder_coords = [-5.8209,-35.2114]
boulder_coords2 = [-5.8206,-35.2122]
boulder_coords3 = [-5.8202,-35.2130]
boulder_coords4 = [-5.8197,-35.2129]
boulder_coords5 = [-5.8193,-35.2127]

trail_coordinates = [
    tuple(boulder_coords),
    tuple(boulder_coords2),
    tuple(boulder_coords3),
    tuple(boulder_coords4),
    tuple(boulder_coords5),
]

m = folium.Map(location=boulder_coords, zoom_start=22, zoom_control=False)

tooltip = "ID#5100"

# folium.Marker(boulder_coords, popup="<i>Início</i>", tooltip=tooltip).add_to(m)
# folium.Marker(boulder_coords, popup="<i>Fim</i>", tooltip=tooltip).add_to(m)

folium.Marker( location=boulder_coords, popup="<i>Início</i>", icon=folium.Icon(color="green", icon="info-sign"), ).add_to(m)
folium.Marker( location=boulder_coords5, popup="<i>Fim</i>", icon=folium.Icon(color="orange", icon="info-sign"), ).add_to(m)

# folium.Circle(
#     radius=100,
#     location=boulder_coords2,
#     popup="Possível localização",
#     color="crimson",
#     fill=True,
# ).add_to(m)

# m.add_child(folium.LatLngPopup())

# folium.Marker(
#     location=boulder_coords2,
#     popup=folium.Popup(max_width=450).add_child(
#         folium.Vega(vis2, width=450, height=250)
#     ),
# ).add_to(m)

folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)

#Create the map
# m = folium.Map(location = boulder_coords, zoom_start = 13)

#Display the map

print (vars(m))

m.save("index.html")
