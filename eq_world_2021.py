import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

earthquakes = 'data/eq_data_7_day_2021.json'
with open(earthquakes) as e:
    all_eq_data = json.load(e)

all_eq_dicts = all_eq_data['features']

mags, longs, lats, hover_texts = [], [], [], []
for eq_data in all_eq_dicts:
    mags.append(eq_data['properties']['mag'])
    longs.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])
    hover_texts.append(eq_data['properties']['title'])

#mapping the earthquakes
data= [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [7*mag for mag in mags],s
        'color': mags,
        'colorscale': 'sunsetdark',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },
}]
eq_title = all_eq_data['metadata']['title']
my_layout = Layout(title= eq_title)

fig= {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_2021.html')
