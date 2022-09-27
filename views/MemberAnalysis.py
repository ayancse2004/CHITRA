# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:45:42 2022

@author: BSTC 4
"""


import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from app import app
from views.page1 import PART_NUMBER_DATABASE_df 
from dash.dependencies import Input, Output,State
from datetime import date, datetime, timedelta
import json 
import dash
import dash_html_components as html
import dash_table
import pandas as pd
from collections import OrderedDict
import dash_pivottable
import plotly.express as px
from views.page1 import CommonCreateAndUpdate_DataBase,Read_DataBase
from views.page1 import Update_DataBaseByStatus
from views.StateWiseData import StateName,DistrictNameByStateName,SubDistrictNameByStateName
from flask_login import logout_user, current_user


Member_Header_Layout=dbc.Row([
    
    
    
    
            html.H4("Members Analysis", style={"textAlign": "center",'color':'#fff','fontSize':'30px','fontWeight':'bold',"background-color":"rgb(91, 127, 128)","font-family":"Segoe UI Semibold"}),
           
            
            ],style={"background-color":"rgb(91, 127, 128)"}
    )


AnaLysisInfo=["Normal","Advance"]

MEM_Com_dropdown_PART_MULTI_ANALYSIS=dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select Type", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_ANALYSIS-MEMBERS",
                             options=[{'label':name, 'value':name} for name in AnaLysisInfo],
                             value=AnaLysisInfo[0]
                          
                           
                             
                             ),
        ),
     html.Div(id="ANALYSIS-OUTPUT-MEMBERS",style={'margin-right':"8rem","overflow":"auto"})
     
     
    ],
    className="mb-3",
    
)

layout=html.Div([
    
    Member_Header_Layout,
    MEM_Com_dropdown_PART_MULTI_ANALYSIS
    
    ])


@app.callback(

      Output('ANALYSIS-OUTPUT-MEMBERS', 'children'),

      
      Input('Com_dropdown_MULTI_ANALYSIS-MEMBERS', 'value'),
       
  
    
   )
def Update_ANALYSIS_Page_Table(value):
   
    data=pd.DataFrame()
    data=Read_DataBase("MEMBERS_USERS_MANAGEMENT")




    if value is None or value == [''] or value ==[] or value ==["Normal"] or value=="Normal": 
         pivLayout=''
         listHeader=['districtname', 'assemblyname', 'pincode']
         
         dataNeeded=data[listHeader]
        
         DataList=dataNeeded.values.tolist()

         DataList.insert(0, listHeader)
         
         pivLayout=dash_pivottable.PivotTable(
                                    data=DataList,

                                    cols=["districtname"],
                                    rows=["assemblyname"],
                                    vals=["pincode"]
                                    )
                                    
            
         return pivLayout