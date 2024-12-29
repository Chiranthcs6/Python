import plotly.graph_objs as go
import pandas as pd

data = [
 {"City": "New York", "Latitude": 40.7128, "Longitude": -74.0060, "Population": 8398748},
 {"City": "Los Angeles", "Latitude": 34.0522, "Longitude": -118.2437, "Population":
3990456},
 {"City": "Chicago", "Latitude": 41.8781, "Longitude": -87.6298, "Population": 2705994},
 {"City": "Houston", "Latitude": 29.7604, "Longitude": -95.3698, "Population": 2320268},
 {"City": "Phoenix", "Latitude": 33.4484, "Longitude": -112.0740, "Population": 1680992},
]

df = pd.DataFrame(data)

fig = go.Figure(data=go.Scattergeo(
    lon=df['Longitude'],
    lat=df['Latitude'],
    text=df['City'],
    mode='markers',
    marker=dict(
    size=df['Population'] / 100000, 
    opacity=0.7,
    colorscale='Viridis', 
    color=df['Population'],
    colorbar=dict(title='Population'),
    )
))

fig.update_geos(
 center=dict(lon=-95, lat=30),
 scope="usa", 
 showland=True, 
 landcolor="rgb(229, 229, 229)", 
)

fig.update_layout(
 title="US Cities Population Map",
)

fig.write_html("interactive_map.html")
