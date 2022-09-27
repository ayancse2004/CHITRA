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
from views import ReachUS
from views import NotificationControl
from views import MemberDetailsMngmnt
from views import page3
from views import PortfolioMngmnt


# layout_dtc = dbc.Col([
#     dtc.SideBar([
        
#         dtc.SideBarItem(id='id_4', label="Total Members(India)", icon="fas fa-info-circle"),
        
      
        
#         dtc.SideBarItem(id='id_3', label="Member Registration", icon="far fa-list-alt"),
        
        
#         dtc.SideBarItem(id='id_6', label="Reach US", icon="fas fa-chart-line"),
        
#         dtc.SideBarItem(id='id_5', label="Active Members Analysis", icon="fas fa-cog"),
      
#         dtc.SideBarItem(id='id_1', label="Visitor Mgmt", icon="fas fa-home"),
        
#         dtc.SideBarItem(id='id_2', label="Complain Mgmt", icon="fas fa-chart-line"),
        
        
       
        
     

     
#     ]),
    
   
  
# ],style={"z-index":"1090","position":"static",})




# layout_dtc = dbc.Col([
#     dtc.SideBar([
        
#         dtc.SideBarItem(id='id_4', label="Total Members(India)", icon="fas fa-info-circle"),
        
      
        
#         dtc.SideBarItem(id='id_3', label="Member Registration", icon="far fa-list-alt"),
        
        
#         dtc.SideBarItem(id='id_6', label="Reach US", icon="fas fa-chart-line"),
        
#         dtc.SideBarItem(id='id_5', label="Active Members Analysis", icon="fas fa-cog"),
      
#         dtc.SideBarItem(id='id_1', label="Visitor Mgmt", icon="fas fa-home"),
        
#         dtc.SideBarItem(id='id_2', label="Complain Mgmt", icon="fas fa-chart-line"),
        
        
       
        
     

     
#     ]),
    
#     # html.H4("", style={"textAlign": "center","margin-top": "20px",'color':'#fff','height':'50px','fontWeight':'bold',"background-color":"rgb(91, 127, 128)","font-family":"Segoe UI Semibold",'width':'48px'}),
    
    
#     html.Div([
#     ], id="page_content",style={"margin-bottom": "6rem","max-height":'100%',"margin-top":"4.2rem","position":"static",}),

    
  
# ],style={"margin-top":"-3.8rem","z-index":"1090","position":"static",})




 

# Page3Layot=html.Div([
    
#     dbc.Row([
        
#         dbc.Col( layout_dtc,),
           
#         dbc.Col(dbc.Button("Click")),
#         ],style={"margin-top":"-3.8rem","z-index":"1090","position":"static"})
    
#     ],style={"position":"static"})




# layout=html.Div([layout_dtc])




# @app.callback(
#     Output("page_content", "children"),
#     [
#         Input("id_1", "n_clicks_timestamp"),
#         Input("id_2", "n_clicks_timestamp"),
#         Input("id_3", "n_clicks_timestamp"),
#         Input("id_4", "n_clicks_timestamp"),
#         Input("id_5", "n_clicks_timestamp"),
#         Input("id_6", "n_clicks_timestamp")
#     ]
# )

# def toggle_collapse(input1, input2, input3, input4, input5,input6):
    
    
    
#     btn_df = pd.DataFrame({"Party Workers": [input4], 
#                            "Visitor Mgmt": [input1], 
#                            "Complain Mgmt": [input2],
#                            "Member Registration": [input3], 
#                            "Active Members Analysis": [input5],
#                            "Reach US": [input6]
#                            })
    
   
    
#     btn_df = btn_df.fillna(0)
#     # print("btn_df&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7",btn_df)

#     if btn_df.idxmax(axis=1).values == "Party Workers":
#         return IndiaMap2.layout

#     if btn_df.idxmax(axis=1).values == "Visitor Mgmt":
#         return page1.layout
#     if btn_df.idxmax(axis=1).values == "Complain Mgmt":
#         return page2.layout
#     if btn_df.idxmax(axis=1).values == "Member Registration":
#         return UserMemberFormEntry.layout

#     if btn_df.idxmax(axis=1).values == "Active Members Analysis":
#         return MemberAnalysis.layout
    
#     if btn_df.idxmax(axis=1).values == "Reach US":
#         return ReachUS.layout
    
#     else:
#         return IndiaMap2.layout
        




    
navlayout=html.Div([

    
  
   dbc.Row(
       
       dbc.NavLink(
           
           dbc.Button("Admin", outline=False, n_clicks=0,color="primary", id="btn_sidebar", className="fa fa-list-alt")
           
           ),
       
  
      id="Row_lg"),
   dbc.Row(
       [
         
        
        dbc.NavLink(
                dbc.Button("", outline=False, n_clicks=0,color="primary", id="btn_sidebar1", className="fa fa-list-alt",)),
          dbc.Tooltip(
   
             "Admin Control",
               target="btn_sidebar1",
               placement="top"
                      ),
    
      
      
      ],  id="Row_sm"
      ),
    
    
    
    dbc.Offcanvas(
        [
       
        
        dbc.Row([
            dbc.Col([
            
            html.I( className="fa fa-info-circle fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Total Members(India)",id='id_4',style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},),
            ],xs=11,sm=11,md=11,),
            
            ],id="row1"),
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-list-alt fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Member Registration",id='id_3', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row2"),
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-info-circle fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Reach US",id='id_6', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row3"),
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-cog fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Active Members Analysis",id='id_5',style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row4"),
        dbc.Row([
            dbc.Col([
              
            html.I( className="fa fa-home fa-2x"),], xs=1,sm=1,md=1,id="col1" ),
            dbc.Col([ dbc.NavLink("Visitor Management",id='id_1',style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
                ],xs=11,sm=11,md=11,),
              
            
            ],id="row5"),
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-chart-line fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Complain Management",id='id_2', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row6"),
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-chart-line fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Notification Management",id='id_7', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row7"),
        
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-chart-line fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Member Details Management",id='id_8', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row8"),
        
        
        
        dbc.Row([
            dbc.Col([
            html.I( className="fa fa-chart-line fa-2x"),],xs=1,sm=1,md=1,id="col1"),
            dbc.Col([
            dbc.NavLink("Portfolio Management",id='id_9', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
            ],xs=11,sm=11,md=11,),
            
            ],id="row9"),
        
        
        
        ], className="g-12",
        
      
        
        
        id="offcanvas",
        title="Admin Control",
        is_open=False,
        
        style={"color":"white","background-color":"rgb(70, 161, 164)","font-weight":"bold",}
    ),
    
    
    ],)

layout=html.Div(
   id="page_content",)






@app.callback(
    Output('offcanvas', 'is_open'),
    [
     Input('btn_sidebar', 'n_clicks'),
     Input('btn_sidebar1', 'n_clicks')],
    [State("offcanvas", "is_open")],)

def ShowOffCanvas(n1,n2,is_open):
    print("It is coming in the callback function",n1,is_open)
    
    if n1>0 or n2>0:
      return not is_open
     
    return is_open 
        
 

    

@app.callback(
    Output("page_content", "children"),
    [
        Input("id_1", "n_clicks_timestamp"),
        Input("id_2", "n_clicks_timestamp"),
        Input("id_3", "n_clicks_timestamp"),
        Input("id_4", "n_clicks_timestamp"),
        Input("id_5", "n_clicks_timestamp"),
        Input("id_6", "n_clicks_timestamp"),
        Input("id_7", "n_clicks_timestamp"),
        Input("id_8", "n_clicks_timestamp"),
        Input("id_9", "n_clicks_timestamp"),
    ]
)

def toggle_collapse(input1, input2, input3, input4, input5,input6,input7,input8,input9):
    
    
    
    btn_df = pd.DataFrame({
        "Member Registration": [input3], 
        
        "Party Workers": [input4], 
                           "Visitor Management": [input1], 
                           "Complain Management": [input2],
                          
                           "Active Members Analysis": [input5],
                           "Reach US": [input6],
                           "Notification Management":[input7],
                           "Member Details Management":[input8],
                           "Portfolio Management":[input9],
                           })
    
   
    
    btn_df = btn_df.fillna(0)
    # print("btn_df&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7",btn_df)

    if btn_df.idxmax(axis=1).values == "Party Workers":
        return IndiaMap2.layout

    if btn_df.idxmax(axis=1).values == "Visitor Management":
        return page1.layout
    if btn_df.idxmax(axis=1).values == "Complain Management":
        return page2.layout
    if btn_df.idxmax(axis=1).values == "Member Registration":
        return UserMemberFormEntry.layout

    if btn_df.idxmax(axis=1).values == "Active Members Analysis":
        return MemberAnalysis.layout
    
    if btn_df.idxmax(axis=1).values == "Reach US":
        return ReachUS.layout
    if btn_df.idxmax(axis=1).values == "Notification Management":
        return NotificationControl.layout
   
    if btn_df.idxmax(axis=1).values == "Member Details Management":
        return MemberDetailsMngmnt.Mnglayout
    
    if btn_df.idxmax(axis=1).values == "Portfolio Management":
        return PortfolioMngmnt.layout  
    
    else:
        return IndiaMap2.layout
        
  
        

# @app.callback(
#     Output("page_content", "children"),
#     [
#         Input("id_11", "n_clicks_timestamp"),
#         Input("id_12", "n_clicks_timestamp"),
#         Input("id_13", "n_clicks_timestamp"),
#         Input("id_14", "n_clicks_timestamp"),
#         Input("id_15", "n_clicks_timestamp"),
#         Input("id_16", "n_clicks_timestamp"),
#     ]
# )

# def toggle_collapseDTC(input1, input2, input3, input4, input5,input6):
    
    
    
#     btn_df = pd.DataFrame({"Party Workers": [input4], 
#                            "Visitor Management": [input1], 
#                            "Complain Management": [input2],
#                            "Member Registration": [input3], 
#                            "Active Members Analysis": [input5],
#                            "Reach US": [input6]
#                            })
    
   
    
#     btn_df = btn_df.fillna(0)
#     # print("btn_df&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7",btn_df)

#     if btn_df.idxmax(axis=1).values == "Party Workers":
#         return IndiaMap2.layout

#     if btn_df.idxmax(axis=1).values == "Visitor Management":
#         return page1.layout
#     if btn_df.idxmax(axis=1).values == "Complain Management":
#         return page2.layout
#     if btn_df.idxmax(axis=1).values == "Member Registration":
#         return UserMemberFormEntry.layout

#     if btn_df.idxmax(axis=1).values == "Active Members Analysis":
#         return MemberAnalysis.layout
    
#     if btn_df.idxmax(axis=1).values == "Reach US":
#         return ReachUS.layout
    
#     else:
#         return IndiaMap2.layout
          
  