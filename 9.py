import pandas as pd
import plotly.express as px

data = pd.DataFrame({
 'x': [1, 2, 3, 4, 5],
 'y': [5, 4, 3, 2, 1],
 'z': [2, 4, 1, 3, 5]
})

fig = px.scatter_3d(data, x='x', y='y', z='z', title="3D Scatter Plot", labels={'x': 'X-axis','y': 'Y-axis', 'z': 'Z-axis'})

fig.update_traces(marker=dict(size=10, opacity=0.8))

fig.write_html("3d_scatter_plot.html")