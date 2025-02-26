import pandas as pd

# Load the CSV file
df = pd.read_csv('Three Candidate Data.csv')

# Extract the relevant columns
data = df.iloc[:, 1:4]

# Extract the labels from column 1
labels = df.iloc[:, 0]

# Extract the color values from column 5
Third_Party = df.iloc[:, 4]

# Extract the symbol values from column 6
Winning_Party = df.iloc[:, 5]

import plotly.express as px
import plotly.graph_objects as go

# Create a ternary plot with labels

fig = px.scatter_ternary(data, a=data.columns[0], b=data.columns[2], c=data.columns[1] ,
                         hover_name=labels, color=Third_Party, 
                         symbol=Winning_Party,
                         color_discrete_map = {"IND": "blue", "GRN": "green", "JLN":"red", "UAP":"yellow", "ON":"orange", "KAP":"gray", "XEN":"black"},
                         symbol_map= {"ALP": "star-square", "LNP":"circle", "GRN":"x", "IND":"x", "KAP":"x", "XEN":"x" },
                         #title="Ternary Plot of Three Candidate Percentage",
                         labels={"color": "3rd party", "symbol": "Winning Party"})

# Customize the plot
# Customize the plot with axis titles
fig.update_layout(
    #title="Vote percentage at the 2nd last count of the 2022 Election",
    ternary=dict(
        sum=100, 
        aaxis=dict(title=dict(text="ALP vote %", font=dict(size=18)),tickmode='linear', dtick=10),
        caxis=dict(title=dict(text="LNP Vote %", font=dict(size=18)),tickmode='linear', dtick=10),
        baxis=dict(title=dict(text="3rd Party %", font=dict(size=18)),tickmode='linear', dtick=10),
        ),
        legend=dict(
            font=dict(size=18)
        )
)
# Add lines from corners to the center

# Add lines from corners to the center
lines = go.Scatterternary({
    'mode': 'lines',
    'a': [100, 0, 33.33, None, 0, 100, 33.33, None, 0, 0, 33.33],
    'b': [0, 100, 33.33, None, 100, 0, 33.33, None, 100, 0, 33.33],
    'c': [0, 0, 33.33, None, 0, 0, 33.33, None, 100, 100, 33.33],
    'line': {'color': 'black', 'width': 1, 'dash': 'dash'},
    'showlegend': False
})

fig.add_trace(lines)
# Add annotations with arrows
annotations = [
    dict(
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=0,
        x=0.23,
        y=0.5,
        text='ALP vote %',
        font=dict(size=18)
    ),
    dict(
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=0,
        x=0.78,
        y=0.5,
        text='LNP Vote %',
        font=dict(size=18)
    ),
    dict(
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=0,
        x=0.5,
        y=-0.1,
        text='3rd Party %',
        font=dict(size=18)
    )
]

fig.update_layout(annotations=annotations)

# Drawing the Arrows
fig.add_shape(type='line',
              x0=0.27, y0=0.4, x1=0.33, y1=0.6,
              line=dict(color='Red', width=2))

fig.add_shape(type='line',
              x0=0.327, y0=0.55, x1=0.33, y1=0.6,
              line=dict(color='Red', width=2))

fig.add_shape(type='line',
              x0=0.31, y0=0.57, x1=0.33, y1=0.6,
              line=dict(color='Red', width=2))

fig.add_shape(type='line',
              x0=0.67, y0=0.6, x1=0.735, y1=0.4,
              line=dict(color='Blue', width=2))

fig.add_shape(type='line',
           x0=0.735, y0=0.45, x1=0.735, y1=0.4,
            line=dict(color='Blue', width=2))

fig.add_shape(type='line',
            x0=0.71, y0=0.43, x1=0.735, y1=0.4,
            line=dict(color='blue', width=2))

fig.add_shape(type='line',
              x0=0.57, y0=-0.068, x1=0.43, y1=-0.068,
              line=dict(color='Black', width=2))
fig.add_shape(type='line',
              x0=0.45, y0=-0.053, x1=0.43, y1=-0.068,
              line=dict(color='Black', width=2))
fig.add_shape(type='line',
              x0=0.45, y0=-0.083, x1=0.43, y1=-0.068,
              line=dict(color='Black', width=2))

# Show the plot
fig.show()


