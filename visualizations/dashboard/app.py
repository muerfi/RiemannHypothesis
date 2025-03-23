# visualizations/dashboard/app.py
# Author: Murphy
# Date: March 2025
# Description: Interactive dashboard to explore the Riemann zeta function along the critical line.

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
from mpmath import zeta

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Riemann Zeta Function Explorer"),
    html.Label("Select range for t (imaginary part):"),
    dcc.Slider(
        id='t-range-slider',
        min=0,
        max=100,
        step=1,
        value=50,
        marks={i: str(i) for i in range(0, 101, 10)},
    ),
    dcc.Graph(id='zeta-plot'),
])

# Callback to update the plot based on the slider
@app.callback(
    Output('zeta-plot', 'figure'),
    [Input('t-range-slider', 'value')]
)
def update_plot(t_max):
    # Compute zeta(1/2 + it) for t in [0, t_max]
    t_values = np.linspace(0, t_max, 1000)
    zeta_values = [abs(zeta(0.5 + 1j * t)) for t in t_values]

    # Create the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=t_values,
        y=zeta_values,
        mode='lines',
        name='|ζ(1/2 + it)|'
    ))
    fig.update_layout(
        title='Magnitude of ζ(s) on the Critical Line',
        xaxis_title='Imaginary Part (t)',
        yaxis_title='|ζ(1/2 + it)|',
        template='plotly_dark'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
  
