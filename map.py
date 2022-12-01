
from turtle import fillcolor
import folium
import pandas


def color_selector(el):
    return 'green' if el<=1000 else 'orange' if (el>1000 and el<=3000)  else 'red'

data= pandas.read_csv(filepath_or_buffer="Volcanoes.txt")

lat=list(data["LAT"])
lon=list(data["LON"])
ele=list(data["ELEV"])
map=folium.Map(location=[24.9061,84.1912],zoom_start=5,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes USA")

'''
for lt,ln , el in zip(lat,lon,ele) :
    fg.add_child(folium.Marker(location=[lt,ln],popup="Elevation: "+str(el)+" m",radius=10,icon=folium.Icon(color=color_selector(el))))
'''

for lt,ln , el in zip(lat,lon,ele) :
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup="Elevation: "+str(el)+" m",radius=10,fill_color=color_selector(el),fill_opacity=500))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding="utf-8-sig").read(),
style_function=lambda x : {'fillColor':"green" if x["properties"]["POP2005"]<10000000 else "yellow" if 10000000<x["properties"]["POP2005"]<50000000 else "orange" if 50000000<x["properties"]["POP2005"]<100000000 else "red"}))

map.add_child(fgv)

map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save ('map1.html')
