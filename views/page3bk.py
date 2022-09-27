# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 09:05:54 2022

@author: BSTC 4
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:26:37 2022

@author: pdm
"""

import dash_trich_components as dtc
from dash.dependencies import Input, Output,State
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from app import app, server
import dash_bootstrap_components as dbc

from views import login, error, page1, page2, profile, user_admin,page3,IndiaMap2
from views import UserMemberFormEntry,MemberAnalysis






content_1 = html.Div(['content 1'],style={"height": "42rem",})
content_2 = html.Div(['content 1'],style={"height": "42rem",})
content_3 = html.Div(['content 1'],style={"height": "42rem",})
content_4 =html.Div(['content 1'],style={"height": "42rem",})
content_5 = html.Div(['content 1'],style={"height": "42rem",})

layout_dtc = dbc.Col([
    dtc.SideBar([
        
        dtc.SideBarItem(id='id_4', label="Total Members(India)", icon="fas fa-info-circle"),
        
      
        
        dtc.SideBarItem(id='id_3', label="Member Registration", icon="far fa-list-alt"),
        
        dtc.SideBarItem(id='id_5', label="Active Members Analysis", icon="fas fa-cog"),
      
        dtc.SideBarItem(id='id_1', label="Visitor Mgmt", icon="fas fa-home"),
        
        dtc.SideBarItem(id='id_2', label="Complain Mgmt", icon="fas fa-chart-line"),
        
        
       
        
     

     
    ]),
    
    html.H4("", style={"textAlign": "center","margin-top": "20px",'color':'#fff','height':'50px','fontWeight':'bold',"background-color":"rgb(91, 127, 128)","font-family":"Segoe UI Semibold",'width':'48px'}),
    
  
],)






placement_selector = html.Div(
    [
        dbc.Label("Placement:"),
        dbc.RadioItems(
            id="offcanvas-placement-selector",
            options=[
                {"label": "start (Default)", "value": "start"},
                {"label": "end", "value": "end"},
                {"label": "top", "value": "top"},
                {"label": "bottom", "value": "bottom"},
            ],
            value="start",
            inline=True,
        ),
    ],
    className="mb-2",
)

offcanvas = html.Div(
    [
       
        dbc.Button(
            "Open Offcanvas", id="open-offcanvas-placement", n_clicks=0
        ),
        dbc.Offcanvas([
           dbc.Col([
               
               dtc.SideBarItem(id='id_4', label="Total Members(India)", icon="fas fa-info-circle"),
               
             
               
               dtc.SideBarItem(id='id_3', label="Member Registration", icon="far fa-list-alt"),
               
               dtc.SideBarItem(id='id_5', label="Active Members Analysis", icon="fas fa-cog"),
             
               dtc.SideBarItem(id='id_1', label="Visitor Mgmt", icon="fas fa-home"),
               
               dtc.SideBarItem(id='id_2', label="Complain Mgmt", icon="fas fa-chart-line"),
               
               
              
               
            

            
           ]),
            
       
            ],
            id="offcanvas-placement",
            title="Menu",
            is_open=True,
            style={'background-color':'red'}
        ),
    ]
)

Page3navbar=html.Div([
    
    dbc.NavbarSimple(
       children=[
          
        offcanvas
          
       ],
       brand="NavbarSimple",
     
       color="primary",
       dark=True,
       expand =True,
   ),
    
    html.Div([
    ], id="page_content",style={"margin-bottom": "6rem","max-height":'100%',}),

    
    ])

 

layout=html.Div([Page3navbar])




@app.callback(
    Output("page_content", "children"),
    [
        Input("id_1", "n_clicks_timestamp"),
        Input("id_2", "n_clicks_timestamp"),
        Input("id_3", "n_clicks_timestamp"),
        Input("id_4", "n_clicks_timestamp"),
        Input("id_5", "n_clicks_timestamp")
    ]
)

def toggle_collapse(input1, input2, input3, input4, input5):
    
    
    
    btn_df = pd.DataFrame({"Party Workers": [input4], 
                           "Visitor Mgmt": [input1], 
                           "Complain Mgmt": [input2],
                           "Member Registration": [input3], 
                           "Active Members Analysis": [input5]
                           })
    
   
    
    btn_df = btn_df.fillna(0)
    # print("btn_df&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7",btn_df)

    if btn_df.idxmax(axis=1).values == "Party Workers":
        return IndiaMap2.layout

    if btn_df.idxmax(axis=1).values == "Visitor Mgmt":
        return page1.layout
    if btn_df.idxmax(axis=1).values == "Complain Mgmt":
        return page2.layout
    if btn_df.idxmax(axis=1).values == "Member Registration":
        return UserMemberFormEntry.layout

    if btn_df.idxmax(axis=1).values == "Active Members Analysis":
        return MemberAnalysis.layout
    
    else:
        return IndiaMap2.layout
        
    
    
    
    
    
    
@app.callback(
    Output("offcanvas-placement", "is_open"),
    Input("open-offcanvas-placement", "n_clicks"),
    [State("offcanvas-placement", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    Output("offcanvas-placement", "placement"),
    Input("offcanvas-placement-selector", "value"),
)
def toggle_placement(placement):
    return placement


  