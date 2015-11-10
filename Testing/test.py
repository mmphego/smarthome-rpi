import plotly.plotly as py
from plotly.graph_objs import Scatter

trace0 = Scatter(x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

unique_url = py.plot(data, filename = 'basic-line')
