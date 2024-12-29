import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.palettes import Category20c

x = np.linspace(0, 10, 100)
y_line = np.sin(x)
categories = ['A', 'B', 'C', 'D', 'E']
x_bar = categories
y_bar = np.random.randint(1, 10, size=len(categories))
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

line_plot = figure(title="Line Plot", x_axis_label="X-axis", y_axis_label="Y-axis")
line_plot.line(x, y_line, line_width=2, legend_label="sin(x)")

source_bar = ColumnDataSource(data={'x': x_bar, 'y': y_bar})
bar_plot = figure(title="Bar Plot", x_range=x_bar, x_axis_label="Categories",y_axis_label="Values")
bar_plot.vbar(x='x', top='y', source=source_bar, width=0.5, color=factor_cmap('x',palette=Category20c[5], factors=categories))

source_scatter = ColumnDataSource(data={'x': x_scatter, 'y': y_scatter})
scatter_plot = figure(title="Scatter Plot", x_axis_label="X-axis", y_axis_label="Yaxis")
scatter_plot.circle('x', 'y', source=source_scatter, size=8, color="navy", alpha=0.5)
output_file("bokeh_plots.html")

plots = gridplot([[line_plot, bar_plot], [scatter_plot]], sizing_mode='scale_width')

show(plots)