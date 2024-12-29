import plotly.express as px
import pandas as pd

data = {
 'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
 'Value': [10, 15, 12, 20, 25, 18, 30, 22, 28, 35]
}

df = pd.DataFrame(data)

fig = px.line(df, x='Date', y='Value', title='Time Series Plot')

fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Value')

fig.show()