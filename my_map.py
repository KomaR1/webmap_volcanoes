import folium
import pandas

data = pandas.read_csv("volcanoes_data.txt")
lt = list(data["LAT"])
ln = list(data["LON"])
el = list(data["ELEV"])
n = list(data["NAME"])

def color(elevation):
    if elevation < 1500:
        return 'green'
    elif elevation > 1500 and elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My map")
for lat, lon, elev, name in zip(lt, ln, el, n):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=10, popup=folium.Popup(iframe), fill_color=color(elev),
                                     fill=True, color='blue', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=(open("world_data.json", 'r', encoding='utf-8-sig').read()),
                                  style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                  else 'yellow' if 10000000 <= x['properties']['POP2005'] < 50000000
                                  else 'orange' if 50000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))

map.add_child(fg)

map.save("map.html")

