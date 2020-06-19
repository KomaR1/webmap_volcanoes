import folium
import pandas

data = pandas.read_csv("volcanoes_data.txt")
lt = list(data["LAT"])
ln = list(data["LON"])
el = list(data["ELEV"])
n = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")
for lat, lon, elev, name in zip(lt, ln, el, n):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("map.html")

