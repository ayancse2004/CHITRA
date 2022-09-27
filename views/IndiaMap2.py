import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output,State
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import json

df = pd.read_csv("./CSV/members.csv")
geojsonRead=open("./json/india_states.geojson")
geojsonRead = json.load(geojsonRead)
df["density"]=round(df['members']/df['population'],4)

fig = go.Figure(data=go.Choropleth(
    geojson=geojsonRead,
    featureidkey='properties.ST_NM',
    locationmode='geojson-id',
    locations=df['state'],
    hovertext=df[['population','density']],
    z=df['members'],
    

    autocolorscale=False,
    colorscale='Reds',
    marker_line_color='peachpuff',

    colorbar=dict(
        title={'text': "Active Members"},

        thickness=10,
        len=0.7,
        bgcolor='rgba(255,255,255,0.8)',

        tick0=0,
        dtick=200000,

        xanchor='left',
        x=0.01,
        yanchor='bottom',
        y=0.05
    )
)
    
    )

fig.update_geos(
    visible=False,
    projection=dict(
        type='conic conformal',
        parallels=[12.472944444, 35.172805555556],
        rotation={'lat': 24, 'lon': 80}
    ),
    lonaxis={'range': [68, 98]},
    lataxis={'range': [6, 38]}
)

fig.update_layout(
    title=dict(
        text="Active Members in India by State as of Now",
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 100, 'l': 0, 'b': 0},
    height=800,
   
   
)



import plotly.express as px
import pandas as pd

df = pd.read_csv("./CSV/location_coordinate.csv")

figPX = px.scatter_geo(df,lat='lat',lon='long', hover_name="id")




figPX.update_layout(
    title=dict(
        text="Active Members in World by geo location",
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 100, 'l': 0, 'b': 0},
    height=800,
    )




layoutPX=dbc.Row(dcc.Graph(id="timeline", figure=figPX))



layout=dbc.Row([
    
                  dcc.Graph(id="timeline", figure=fig),
                  dcc.Graph(id="timelinePx", figure=figPX),
                  
                  
                  ]
                 
                 
                 )

                 



