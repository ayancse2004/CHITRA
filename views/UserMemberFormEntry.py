#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:53:15 2022

@author: pdm
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
import smtplib
import flask
from views.EmailLogin import emailLayout
from flask import session

from views.CumtompdfGenerator  import *

STATENAME=StateName()


FORMOK=0

sizeleft=3
sizeright=8
StyleLabel={"text-align": "left","fontWeight":"bold","color":"#2b0593","margin-left":'0.6rem','font-size':'1rem',"margin-top":'0.8rem'}
StyleInput={"text-align": "left","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.5rem',}
StyleInput1={"text-align": "left","margin-left":'0.6rem','font-size':'2min',"margin-top":'0.5rem'}




# # LoadingComp= dcc.Loading(id="loading",fullscreen=True,type='default',children=html.Div(id="loading_output")),ArithmeticError
# LoadingComp = html.Div(
#     children=[
      
#         html.Div(id="loading-input-1", ),
#         dcc.Loading(
#             id="loading-1",
#             type="default",
#             children=html.Div(id="loading-output-1")
#         ),
       
#     ],
# )


# @app.callback(
#                 Output("loading-output-1", "children"),
              
#               Input("loading-input-1", "value"))
# def input_triggers_spinner(value):
#     time.sleep(5)
#     return value


SpinnerComp=html.Div([
    
    
    dbc.Spinner(id="spinner",color='primary',)
    ],id="spinner_div",style={"display":"flex"})
    





USer_Header_Layout=dbc.Row([
    
    
 
            html.H4("Member Registration Form(सदस्य पंजीकरण फॉर्म)",
                    
                    style={"text-align": "center",'color':'#fff',
                          
                           'padding-top':'5px',
                           'fontSize':'20px','fontWeight':'bold',
                           "background-color":"rgb(91, 127, 128)",
                           "font-family":"Segoe UI Semibold"}),
           
            
            ],style={"background-color":"rgb(91, 127, 128)",}
    )




Com_dropdown_STATE =dbc.Row(
    [
     dbc.Row([
         dbc.Col(
             
                 dbc.Label("Select Your State(अपना राज्य चुनें) ", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
                 ),
             dbc.Col(    
                 dcc.Dropdown(
                             id="Part_Com_DROP_STATE",
                             options=[{'label':name, 'value':name} for name in STATENAME],
                             value="UTTAR PRADESH",
                             clearable=False,
                             style=StyleInput,
                             )
                 ,md=12,sm=12,xs=12,lg=8,xl=8
                 
             ),
      ],className="row justify-content-center"),
         
     html.Br(),
    dbc.Row(
             [
                 dbc.Col(
                     dbc.Label("Select Your District(अपने जिले का चयन करें) ", html_for="dropdown" ,style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
                     
                     ),
                 dbc.Col(
                     dcc.Dropdown(
                                 id="Part_Com_DROP_DISTRICT",
                                 options=[{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],
                                 clearable=False,
                                 style=StyleInput,
                                 ),
                         md=12,sm=12,xs=12,lg=8,xl=8
                     ),
                 ],className="row justify-content-center"),
       
       

     
     
     
     
dbc.Row([
    

     
     dbc.Col(
                     dbc.Label("Select Your Sub District(अपना उप जिला चुनें) ", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Part_Com_DROP_ASSEMBLY",
                             options=[{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],
                             clearable=False,
                             style=StyleInput,
                             ),
               md=12,sm=12,xs=12,lg=8,xl=8
        ),
    
    
    ],className="row justify-content-center"),


    ],
    # className="mb-3"
   
  
    
)








Com_dropdown_PERSONNAME =dbc.Row(
    [
     
     dbc.Row([
         dbc.Col(
                         dbc.Label("First Name of Candidate(उम्मीदवार का पहला नाम)", html_for="dropdown",style=StyleLabel), md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
                         dbc.Input(id="CAN_FIRST_NAME",placeholder="please type your name ...", type="text", style=StyleInput1,),md=12,sm=12,xs=12,lg=8,xl=8
             ),
         
         
         ],className="row justify-content-center"),
     
     dbc.Row([
         dbc.Col(
                         dbc.Label("Middle Name of Candidate(उम्मीदवार का मध्य नाम)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
                         dbc.Input(id="CAN_MIDDLE_NAME",placeholder="please type middle name ...", type="text", style=StyleInput1,),md=12,sm=12,xs=12,lg=8,xl=8
             ),
         
         ],className="row justify-content-center"),
     
     dbc.Row([
         
         dbc.Col(
                         dbc.Label("Last Name of Candidate(उम्मीदवार का अंतिम नाम)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
                         dbc.Input(id="CAN_LAST_NAME",placeholder="please type last name ...", type="text", value="",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8
             ),
         ],className="row justify-content-center"),
   

    ],
    className="mb-3",
    
)




Com_dropdown_PERSON_DETAILS =dbc.Row(
    [
     dbc.Row([
         
         dbc.Col(
                         dbc.Label("Enter Your Mobile Number(अपना मोबाइल नंबर )", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
            
                         dbc.Input(id="CAN_MOBILE",placeholder="Enter Your Mobile Number...", type="text",value="",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8
             ),
         
         
         ],className="row justify-content-center"),
     
   dbc.Row([
       
       dbc.Col(
          dbc.Label("Enter Your E-Mail id(अपना ई-मेल आईडी दर्ज करें)",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
          ),
      
       dbc.Col([
                  dbc.Input(id="email_input", placeholder="Enter Your Email-ID...",type="email", value="", style=StyleInput1,),
                  
                  dbc.FormFeedback("That looks like a email address :-)", type="valid", style=StyleInput,),
                  dbc.FormFeedback(
                      "Sorry, we only accept valid email id..",
                      type="invalid", style=StyleInput,
                         ),
       
       
       
      
        ],md=12,sm=12,xs=12,lg=8,xl=8,),
       
       
       ],className="row justify-content-center"), 
     
     dbc.Row(
         [
             
             dbc.Col(
                             dbc.Label("Enter Your Gender(अपना लिंग दर्ज करें)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
                ),
             dbc.Col(
                             dcc.Dropdown(
                                         id="Part_Com_DROP_GENDER",
                                         options=[{'label':name, 'value':name} for name in ["MALE","FEMALE","OTHERS"]],
                                         value='MALE',
                                         clearable=False,
                                         style=StyleInput,
                                         ),
                          md=12,sm=12,xs=12,lg=8,xl=8,
                 ),
             ],className="row justify-content-center")
   
     
   
     
    
     
    ],
    className="mb-3",
    
)


Com_dropdown_PERSON_ADDRESS_DETAILS=dbc.Row(
    [
     
     dbc.Row([
         
         dbc.Col(
                         dbc.Label("Enter Home Address(अपना पता दर्ज करें)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
             
          
                         dbc.Textarea(id="CAN_HOME_ADD",placeholder="Enter Home Address...",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8,
             ),
         
         
         ],className="row justify-content-center"),
     dbc.Row([
         dbc.Col(
                         dbc.Label("Enter Your Block(अपना ब्लॉक दर्ज करें)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
                         dbc.Input(id="CAN_BLOCK_ADD",placeholder="Enter Your Block ...", type="text",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8,
             ),
         
         
         ],className="row justify-content-center"),
     dbc.Row([
         
         dbc.Col(
                         dbc.Label("Enter Pin Code(पिन कोड दर्ज करें)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
            ),
         dbc.Col(
                         dbc.Input(id="CAN_PIN_ADDRESS",placeholder="Enter Your Pin Code ...", type="text",value="",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8, 
             ),
         
         ],className="row justify-content-center"),
    
     
     
   
     
    
     
    ],
    className="mb-3",
    
)

CLICK_EVENT=html.Div([
    
    
    
   # LoadingComp,
dbc.Col([dbc.Button(
                            "Register New User(सदस्य बनें)", id="USER_Update_Btn", className="me-2", n_clicks=0,
                            style={"margin-right":"0.2rem","margin-top":"2rem"},
                            ),
    
                
                           dbc.Button(
                               "Back to Main Page",
                              # dbc.NavLink(  "Back to Main Page",   href="/mainpage" ,style={"text-decoration":"none","color":"white","font-weight":"bold"}
                                href="/mainpage", 
                                style={"margin-right":"0.2rem","margin-top":"2rem"}, 
                                ),
                       # id="USER_Reset_Btn", className="me-2", n_clicks=0,
                       # style={"margin-right":"0.2rem","margin-top":"2rem"},  
                                # ),
                         
                            html.Span(id="UpdateRow_Info_USER", style={"verticalAlign": "middle","text-align":"center"}),
                         
                            
    ],
    
    # className="d-grid gap-8 d-md-flex justify-content-md-end",
    
    
  style={"text-align":"center","margin-bottom":"1rem",}
  ),
 html.Div(id="ModalAlert"),
   # LoadingComp,
 ])















USER_FORM=[
    USer_Header_Layout,
    html.Hr(),
    Com_dropdown_STATE,
    Com_dropdown_PERSONNAME,
    
    Com_dropdown_PERSON_DETAILS,
    Com_dropdown_PERSON_ADDRESS_DETAILS,
    CLICK_EVENT
    
    ]

tab_style={"color": "#fff",'background-color':'rgb(91, 127, 128)','font-weight':'bold'}
USertabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Member Registration", tab_id="tab-1",active_label_style=tab_style),
                dbc.Tab(label="Members List Info", tab_id="tab-2",active_label_style=tab_style),
                dbc.Tab(label="State Detailed Members List Info", tab_id="tab-3",active_label_style=tab_style),
            ],
            id="tabs",
            active_tab="tab-1",
          
        ),
        html.Hr(),
        
        html.Div(id="content",style={'background-color':'#fff',"margin-bottom":"10rem","overflowX":"hidden","border":"2px solid #3483d3"}),
        
        
        html.Div(id="content_details",style={"max-height":"1000vh",}),
    ],style={"overflow":"hidden",}
)



def GenerateMessage(emailid,ssid):

    message = "Welcome to ApnaDal-S as Party Member ,Your Membership number is "+ssid
    SUBJECT = "Apna Dal-S Membership number details"
    TEXT = "This message was sent by Apna Dal-S  Team \n "+ message   
    message1 = 'From: Apna Dal-S\nSubject: {}\n\n{}'.format(SUBJECT, TEXT)
    
    
    
    
    # message = "Welcome to Lynx Team ,Your Membership number is "+ssid
    # SUBJECT = "Lynx Team Membership number details"
    # TEXT = "This message was sent by Lynx Team \n "+ message   
    # message1 = 'From: Lynx\nSubject: {}\n\n{}'.format(SUBJECT, TEXT)
    
    
        
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("ajay.cse2004@gmail.com", "whgnysbsgusdexjw")
    s.sendmail('&&&&&',emailid,message1)
    



def ReadMembersListfromCSV():
    import os

    path='./CSV/NewMembersList.csv'
         
    if os.path.exists(path):
             
        try:
            dfFile = pd.read_csv(path)
            return dfFile
                 
        except :
            dfFile = pd.DataFrame()
            return dfFile
        
        
    dfFile = pd.DataFrame()
    return dfFile    
                 

PAGE_SIZE = 10

MEMBERLISTFORM = html.Div(
    
    className="row",
    children=[
        
        
        html.H4("Member's List Info", style={"textAlign": "center",'color':'#fff','fontSize':'30px','fontWeight':'bold',"background-color":"rgb(91, 127, 128)","font-family":"Segoe UI Semibold"}),
        html.Div([

               
               
               html.A('Download',
        id='download',
        href='/test_download'),
              
               ],style={"text-align":"center","margin-top":"0.5rem","margin-bottom":"0.5rem","margin-right":"1.5rem"}),
        
     
        html.Hr(),
        
        html.Div(
            dash_table.DataTable(
                id='table-paging-with-graph',
                columns=[
                    {"name": i, "id": i} for i in (ReadMembersListfromCSV().columns)
                ],
                page_current=0,
                page_size=PAGE_SIZE,
                page_action='custom',

                filter_action='custom',
                filter_query='',

                sort_action='custom',
                sort_mode='multi',
                sort_by=[],
                style_data_conditional=[
      
                        {
                            'if': {
                               
                                'column_id': 'key',
                            },
                            'backgroundColor': 'white',
                            'color': 'green',
                            
                            
            
                        },
                        ],
               
            ),
            
            
            
            style={ 'height':'450','overflowY': 'scroll'},
            className='six columns'
        ),
        
        html.Div(id="MemberInfoDisplayDialog"),
        
        html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        ),
        
    
    ]
)

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]




layout=html.Div(
    [
     USertabs
     
     ],style={"background-color":"rgb(255, 255, 255)"}
    
    )


layoutDirect=html.Div([


html.Div([
         
     USertabs
         ],id='notification',style={'display':'none'}) ,

      #html.Div(id="notification"),

      dbc.Modal(
          [
              dbc.ModalHeader(dbc.ModalTitle("Login"),close_button=False),
              dbc.ModalBody(emailLayout),
              
              dbc.ModalFooter(
                  # dbc.Button(
                  #     "Close", id="close", className="ms-auto", n_clicks=0
                  # )
              ),
          ],
          id="email_modal-ntf",
          is_open=True,
          backdrop="static",
          centered=True,
       
      ),
     
    ])
    
  


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('table-paging-with-graph', "data"),
    Input('table-paging-with-graph', "page_current"),
    Input('table-paging-with-graph', "page_size"),
    Input('table-paging-with-graph', "sort_by"),
    Input('table-paging-with-graph', "filter_query"))
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = ReadMembersListfromCSV()

    def upper_consistent(df):
        df = df.apply(lambda x: x.str.upper() if x.dtype == "object" else x) 
        return df
    
    dff=upper_consistent(dff)
    dff=dff.fillna('No Data')
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)
       
       
        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
       
        elif operator == 'contains':
           
          
           # print(type(filter_value)) 
           if type(filter_value) is int or type(filter_value) is float :
                
                filter_value=str(int(filter_value))
                
                if col_name=='contactno':
                    dff[col_name]=dff[col_name].astype(str)
                    dff = dff.loc[dff[col_name].str.contains(filter_value.upper())]
                    
                else:
                    
                    dff = dff.loc[dff[col_name].str.contains(filter_value.upper())]
               
           else:
               if col_name=='contactno':
                   dff[col_name]=dff[col_name].astype(str)
                   dff = dff.loc[dff[col_name].str.contains(filter_value.upper())]
               
               else:
                   
                       
                 dff = dff.loc[dff[col_name].str.contains(filter_value.upper())]
               
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )
      
    return dff.iloc[
        page_current*page_size: (page_current + 1)*page_size
    ].to_dict('records')


@app.callback(
    Output('table-paging-with-graph-container', "children"),
    Input('table-paging-with-graph', "data"))
def update_graph(rows):
    dff = pd.DataFrame(rows)
    
    if len(dff)>0:
        df_value_counts = dff['districtname'].value_counts().reset_index()
        df_value_counts.columns = ['districtname', 'counts']
        #print(df_value_counts)
        
        df_value_counts_Ass = dff['assemblyname'].value_counts().reset_index()
        df_value_counts_Ass.columns = ['assemblyname', 'counts']
    else:
           return "No Data"
    if len(df_value_counts)>0 and len(dff)>0:
        
        
        DISTRICT_GRAPH=dcc.Graph(
            id="counts",
            figure={
                "data": [
                    {
                        "x": df_value_counts["districtname"],
                        "y": df_value_counts["counts"] if "counts" in df_value_counts else [],
                        "type": "bar",
                        "marker": {"color": "#0074D9"},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {"automargin": True},
                    "height": 450,
                    "margin": {"t": 50, "l": 50, "r": 50},
                    'title':"Members list District Wise",
                },
            },
        )
        
    if len(df_value_counts_Ass)>0 and len(dff)>0:
        
        SUBDISTRICT_GRAPH=dcc.Graph(
            id="counts2",
            figure={
                "data": [
                    {
                        "x": df_value_counts_Ass["assemblyname"],
                        "y": df_value_counts_Ass["counts"] if "counts" in df_value_counts_Ass else [],
                        "type": "bar",
                        "marker": {"color": "#0074D9"},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {"automargin": True},
                    "height": 450,
                    "margin": {"t": 50, "l": 50, "r": 50},
                    'title':"Members list Sub District Wise",
                },
            },
        )
     

        
        return html.Div(
            [
                
                DISTRICT_GRAPH,
                SUBDISTRICT_GRAPH
                ]
                
        )
    else:
        return "No Data"







@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return USER_FORM
    elif at == "tab-2":
        if current_user.is_authenticated or session.get("login")==1:
            return MEMBERLISTFORM
        else:
            return 'No Page Found'
    
    elif at == "tab-3":
        return StateWiseDetailedLayout()
    return html.P("This shouldn't ever be displayed...")




# --- Callbacks --- #
@app.callback(
    [Output("email_input", "valid"), Output("email_input", "invalid")],
    [Input("email_input", "value")],
)
def check_validity(text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if text:
        if(re.fullmatch(regex, text)):
            return True, False
        else:
            return False, True
            
    return False, False


# --- Callbacks --- #


import re
  
def isMobileValid(s):
      
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("[6-9][0-9]{9}")
    return Pattern.match(s)
  



@app.callback(
    [Output("CAN_MOBILE", "valid"), 
     Output("CAN_MOBILE", "invalid")],
    [Input("CAN_MOBILE", "value")],
)
def check_validityMobile(text):
    if text :
       
        if isMobileValid(text) and len(text)==10:
            is_gmail=True
         
        else:
            is_gmail=False
     
        return is_gmail, not is_gmail
    return False, False




def isPinValid(s):
      
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("[1-9][0-9]{5}")
    return Pattern.match(s)
  



@app.callback(
    [Output("CAN_PIN_ADDRESS", "valid"), 
     Output("CAN_PIN_ADDRESS", "invalid")],
    [Input("CAN_PIN_ADDRESS", "value")],
)
def check_validityPin(text):
    if text :
      
        if isPinValid(text) and len(text)==6:
            is_gmail=True
         
        else:
            is_gmail=False
     
        return is_gmail, not is_gmail
    return False, False



@app.callback(
    
     
     Output('Part_Com_DROP_DISTRICT', 'options'),
 
 
    Input('Part_Com_DROP_STATE', 'value')
)
def update_output_District(value):
    
    DISTRICTNAME=['NULL']
    if value is not None:
    
        DISTRICTNAME=DistrictNameByStateName(value)
    
        #print(DISTRICTNAME)
   

    return [{'label':name, 'value':name} for name in DISTRICTNAME]
   


@app.callback(
    
     
     Output('Part_Com_DROP_ASSEMBLY', 'options'),
 
 
    Input('Part_Com_DROP_DISTRICT', 'value')
)
def update_output_SUbDistrict(value):
    
    SUBDISTRICTNAME=['NULL']
    if value is not None:
    
        SUBDISTRICTNAME=SubDistrictNameByStateName(value)
    
        #print(SUBDISTRICTNAME)
   

    return [{'label':name, 'value':name} for name in SUBDISTRICTNAME]




@app.callback(
    Output("modal", "is_open"),
    [ Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n2, is_open):
    if n2:
        return not is_open
    return is_open


@app.callback(
    Output('UpdateRow_Info_USER', 'children'),
    
    # Output('ModalAlert','children'),
   
    [Input('USER_Update_Btn', 'n_clicks'),
     
     ],
    
    
      
      State('Part_Com_DROP_STATE','value'),
      State('Part_Com_DROP_DISTRICT','value'),
      State('Part_Com_DROP_ASSEMBLY','value'),
      
      State('CAN_FIRST_NAME','value'),
      State('CAN_MIDDLE_NAME','value'),
      
      
      
      State('CAN_LAST_NAME','value'),
      State('CAN_MOBILE','value'),
      State('email_input','value'),
      State('Part_Com_DROP_GENDER','value'),
      State('CAN_HOME_ADD','value'),
      State('CAN_BLOCK_ADD','value'),
      State('CAN_PIN_ADDRESS','value'),
    
    
   
     
   
 )



def UpdateData_row(n_clicksData,StateName,DistrictName,
                   AssemblyName,FirstName,MiddleName,
                   LastName,MobileNo,EmailID,Gender,
                   HomeAddress,Block,PinCode):
    
 import os
 import numpy as np

 
 if n_clicksData>0:
     

    
     path='./CSV/NewMembersList.csv'
     
     
     if os.path.exists(path):
         
             try:
                 dfFile = pd.read_csv(path)
                 #print("Read dfFile",dfFile)
             
             except :
                 dfFile = pd.DataFrame()
                 

             
             if StateName is None:
                 return("StateName is blank!"),html.Div()
                 
                 
             if DistrictName is None or len(DistrictName)<3: 
                 
                 return("DistrictName is blank!"),html.Div()
             
             if AssemblyName is None or len(AssemblyName)<3:
                    
                    return("AssemblyName is Blank!"),html.Div() 
                
             if FirstName is None or len(FirstName.strip())<3:
                       
                    return("FirstName is Blank!"),html.Div()   
                
                                
             if MiddleName is None  or len(MiddleName.strip())<0:
                       
                    MiddleName=""
              
             if LastName is None or len(LastName.strip())<1:
                              
                    return("LastName is Blank!"),html.Div()  
             if MobileNo is None or len(MobileNo)!=10:
                 
                     
                                    
                    return("MobileNo is Blank!  or not proper Mobile Number typed"),html.Div()
                
             if Gender is None or len(Gender)<1:
                                          
                    return("Gender is Blank!"),html.Div()   
               
             if HomeAddress is None or len(HomeAddress.strip())<10:
                                          
                    return("HomeAddress is Blank or not proper address typed!"),html.Div() 
            
             if Block is None or len(Block.strip())<3:
                                         
                   return("Block is Blank!  or not proper block typed"),html.Div()  
            
             if PinCode is None or len(PinCode)!=6:
                 
                  return("PinCode is Blank!  or not proper pin code typed"),html.Div()  
            
                
             if isMobileValid(MobileNo):
                 print('ok mobile')
                 
             else:
                 return("MobileNo is Blank!  or not proper Mobile Number typed"),html.Div()
                 
             if isPinValid(PinCode):
                 print('ok pin')
                 
             
             else:
                 return("PinCode is Blank!  or not proper pin code typed"),html.Div()  
                 
            
             from datetime import datetime
             import random 
             
             print("HomeAddress",HomeAddress)
             
             HomeAddress=HomeAddress.replace(","," ")
             HomeAddress=HomeAddress.replace('\n', ' ')
             
             Block=Block.replace(","," ")
             Block=Block.replace("\n"," ")
             random_number = random.randint(10000000000, 999999999999)

             SSID="ADS"+"_"+str(random_number)
           
             now = datetime.now()
             # print("Now Time",now)
             dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                 
             # print("dt_string",dt_string)
             
             data = {'key':[StateName+"_"+MobileNo], 'name': [FirstName+" "+ MiddleName + " "+ LastName] ,'gender': [Gender] ,'address': [HomeAddress],'block': [Block] ,'pincode': [PinCode] 
                         
                         ,'statename': [StateName] ,'districtname': [DistrictName] ,'assemblyname': [AssemblyName],'contactno':[MobileNo],'emailid':[EmailID],'date':[dt_string],'ssid':[SSID]  
                         
                         }
             
             # print("Data Created before saving",data)
             df = pd.DataFrame(data=data)
             
             print("Df",df['address'],df['block'])
             textStatus="Some Error Occurred {}".format(MobileNo)
             if len(dfFile)>0:
                
                 df['contactno'] = df['contactno'].astype('int64')
                 #print("  df['contactno'] ",  df['contactno'] )
                 dfFile['contactno'] = dfFile['contactno'].astype('int64')
                 
                 #print(" dfFile['contactno'] ", dfFile['contactno'] )
                 mask=df['contactno'].values in dfFile['contactno'].values
                 #print("Mask",mask)
          
                 if  mask:
                     #CustompdfGeneratorpdf(df)
                     return("User already Registered with following Number {}".format(df['contactno'])),modaloutput(("User already Registered with following Number {}".format(df['contactno'])))
                       
                 else:
                 
                     df.to_csv("./CSV/NewMembersList.csv",mode='a', header=False, index=False)    
                     sendStatus=updateDateBaseNewlyAddedMemeber()
                     if sendStatus:
                         if len(EmailID)>5:
                           GenerateMessage(EmailID,SSID)   
                           CustompdfGeneratorpdf(df)
                         textStatus="User Registered with following Number is {}  user Party Number is {} and Details is sent to Your mail if any ".format(MobileNo,SSID)
                           
                     # return modaloutput
                     # return"User Registered with following Number is {}  user Party Number is {} and Details is sent to Your mail if any ".format(MobileNo,SSID),modaloutput("User Registered with following Number is {}  user Party Number is {} and Details is sent to Your mail if any ".format(MobileNo,SSID))
                     return textStatus,modaloutput(textStatus)
                     
             
             else:
                 
                 df.to_csv("./CSV/NewMembersList.csv",mode='a', header=False, index=False)    
                 updateDateBaseNewlyAddedMemeber()
                 dcc.Loading(id="loading",fullscreen=True,type='default')
                 return("User Registered with following Number is {} and user Party Number is {} ".format(MobileNo,SSID)),modaloutput("User Registered with following Number is {} and user Party Number is {} ")  
       
    
     else:
        
        
            
            data = {'key':[""], 'name': [""] ,'gender': [""] ,'address': [""],'block': [""] ,'pincode': [""] 
                            
                            ,'statename': [""] ,'districtname': [""] ,'assemblyname': [""],'contactno':[""],'emailid':[""],'date':[""],'ssid':[""]  
                            
                            }
            df = pd.DataFrame(data=data)
            df = df.iloc[1: , :]
            
        
            df.to_csv("./CSV/NewMembersList.csv",index=False)
            
            return("User Not Registered with US Please Try Again"),modaloutput("User Not Registered with US Please Try Again")
                
 
            






def modaloutput(message):
    # from fpdf import FPDF
        
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_xy(0, 0)
    # pdf.set_font('arial', 'B', 13.0)
    # pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Hello", border=0)
    # pdf.output('test.pdf', 'F')
    modaloutput= html.Div(
        [
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Confirmation")),
                    dbc.ModalBody(message,style={"font-weight":"bold"}),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                id="modal",
                is_open=True,
                backdrop="static",
                centered=True
            ),
            
        ]
    )
    return modaloutput







              
            
def updateDateBaseNewlyAddedMemeber():
    
            print("updateDateBaseNewlyAddedMemeber")
            key='key'
            CSV_FILENAME="NewMembersList.csv"
            TABLE_NAME="MEMBERS_USERS_MANAGEMENT"
            createTableSchema='''(key VARCHAR(255) PRIMARY KEY,name VARCHAR(255),gender VARCHAR(255),address VARCHAR(1000),block VARCHAR(255),
                 pincode VARCHAR(255),statename VARCHAR(255),districtname VARCHAR(255),
                 assemblyname VARCHAR(255),contactno VARCHAR(255),emailid VARCHAR(500),date VARCHAR(255),ssid VARCHAR(10000));'''
            getVal=CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)
            print("################################",getVal)
            
            print("updateDateBaseNewlyAddedMemeber2")

            pathT='./CSV/NewMembersList.csv'
            dfHis= Read_DataBase("MEMBERS_USERS_MANAGEMENT")
            dfHis.to_csv(pathT,index=False)
            return(getVal)
        
                     
                         

def StateWiseDetailedLayout():

    import datetime
    
    
    todaysDate=datetime.date.today().strftime('%Y-%m-%d')
    # todaysDate=datetime.date.today().strftime('%d/%m/%Y')
   
    # print(todaysDate)
    



    HTML_SUMMARY_STATE=[]
    HTML_SUMMARY_INDIA=[]
    
    df=ReadMembersListfromCSV()
    
    STATENAME=df['statename'].unique()
 
    
    for k in STATENAME:
        
        dfff=df[df['statename']==k]
        
        statecount=len(dfff)
   
        
        dfff['dateonlyIndia'] = (pd.to_datetime(dfff['date'],format=('%d/%m/%Y %H:%M:%S')).dt.date).astype(str)
        
   
        # print( dfff['dateonlyIndia'] )
        
        TotalcountDfDailyIndia=dfff[dfff['dateonlyIndia']==todaysDate]
        
        # print( TotalcountDfDailyIndia)
        
        
        #print(k)
        
        State_card = dbc.Card([
            
            
            dbc.Row([
                dbc.Col([
                   dbc.CardHeader(k,style={'textAlign': 'center',"color":"white",
                                           "font-size": "25px",
                                           "font-weight":"bold",
                                           "padding": "0.1rem 0.1rem",
                                                                      
                                           "font-family": "Segoe UI Semibold",
                                           "background-color": "#5b7f80"}),
                   ],width=12),
                   
                   dbc.Col([
                       dbc.Label("Total Members",style={"font-size": "17px"}),
                       html.H1(statecount,id="First",),
                       
                       ],width=6,style={"font-size": "15px","color":"green","font-weight":"bold","text-align":"center"}
                       ),
                
                       dbc.Col([
                           dbc.Label("Today's Members",style={"font-size": "17px"}),
                           html.H1(len(TotalcountDfDailyIndia),id="First"),
                           
                           ],width=6,style={"font-size": "15px","color":"green","font-weight":"bold","text-align":"center"}
                           ),
                     
                   ]),
            
            ],)
        HTML_SUMMARY_STATE.append(dbc.Row(dbc.Col(State_card)))
        
        
        DISTRICTNAME=dfff['districtname'].unique()
        
        HTML_SUMMARY_LIST_VIEW_PARAMETER=[]
        for y in DISTRICTNAME:
            #print(k,y,DISTRICTNAME)
            
            TotalcountDf=df[df['districtname']==y]
            
            TotalcountDf['dateonly'] = (pd.to_datetime(TotalcountDf['date'],format=('%d/%m/%Y %H:%M:%S')).dt.date).astype(str)
            
            TotalcountDfDaily=TotalcountDf[TotalcountDf['dateonly']==todaysDate]
            #print(todaysDate)
            #print("TotalcountDfDaily",TotalcountDfDaily,TotalcountDf['dateonly'])
         
         
            Totalcount=len(TotalcountDf)
            TotalcountDaily=len(TotalcountDfDaily)
            
            complex_card = dbc.Card(
                     [
      
                         dbc.CardBody(
                              [
                                 
                                  html.H6(y,id="First",className="card-title",style={"margin-top":"-1.1rem","font-size": "14px","color":"#a00","font-weight":"bold","textAlign":"center"}),
                                  
                                  #html.Div(className="fa fa-users",),
                                 
                                  dbc.Row([
                                      
                                      dbc.Col([
                                          html.Label("Total ",style={'color':'green',"font-weight":"bold",}),
                                  
                                        
                                          ],width=4
                                                   
                                        ),
                                      
                                    dbc.Col(
                                                  html.Label(className="fa fa-users",style={'color':'green',"font-weight":"bold",}),width=4
                                      ),
                          
                                    dbc.Col(
                                                  html.Label(Totalcount,id="TotalMembers",className="card-title",style={"margin-top":"-0.9rem",
                                                                                                         "font-size": "12px","color":"black","font-weight":"bold",}),width=4
                                       ),]
                                   ),
                                      
                             
                                  
                                  dbc.Row([
                                      
                                      dbc.Col([
                                          html.Label("Today's"),
                                  
                                        
                                          ],width=4
                                                   
                                        ),
                                      
                                    dbc.Col(
                                                  html.Label(className="fa fa-users"),width=4
                                      ),
                                 
                                    
                                    dbc.Col(
                                                  html.Label(TotalcountDaily,id="TodayMembers",className="card-title",style={"margin-top":"-0.9rem",
                                                                                                         "font-size": "12px","color":"black"}),width=4
                                       ),]
                                   ),
                                      
                                  
                                  dbc.Row([
                                   
                                      
                                    dbc.Col(
                                                  html.Label(" ",id=y,n_clicks=0, className="fas fa-info-circle",style={"font-size":"25px"}) ,width=12
                                      ),
                                 
                                  
                                   ],style={"text-align":'right'}),
                                      
                                  
                                  dbc.Row([
                                      
                                      
                                      dbc.Col(
                                                    html.Div(" ",id='outputDiv'+y,n_clicks=0) , align="center",width=12
                                        ),
                                      
                                      ]
                                      
                                      
                                      ),
                                 # html.Hr(style={"margin-top":"-0.3rem","font-size": "12px"}),
                                  
                                  #html.H6(count,id="Last",className="card-title",style={"margin-top":"-0.9rem",
                                                                                         #"font-size": "12px","color":"black"}),
                                  
                              ],style={
                                     "color":"blue","margin-left": "1rem","margin-right":"0.5rem",
                                     "margin-bottom":"0.5rem","margin-top":"0.1rem",
                                     "height":"0.5rem"}
                              
                          ),
                          
                      ],id='card'+y,style={"width":'18rem',"height":"8.2rem","margin-bottom":"0.5rem","margin-left":"0.5rem","margin-right":"0.5rem","margin-top":"0.5rem"},color="primary", outline=True
                    )
            HTML_SUMMARY_LIST_VIEW_PARAMETER.append(dbc.Col((complex_card)))
            
        HTML_SUMMARY_STATE.append(dbc.Row(HTML_SUMMARY_LIST_VIEW_PARAMETER))          


    return  html.Div(HTML_SUMMARY_STATE,)            
  




# @app.callback(
    
     
#      Output('content_details', 'children'),
 
 
#     Input('CHITRAKOOT', 'n_clicks')
# )
# def update_output_DISTRICT_DETAILS(value):
    
#     print("update_output_DISTRICT_DETAILS",value)
#     if value is not None:
    
#         return value
    
#         #print(SUBDISTRICTNAME)
   

#     return "No Valid Input"


# def generate_control_id(value):
#     return 'Control {}'.format(value)



    




# create a callback for all possible combinations of dynamic controls
# each unique dynamic control pairing is linked to a dynamic output component









df=ReadMembersListfromCSV()
for value in df['districtname'].unique():
    @app.callback(
                    [Output('outputDiv'+value, 'children'),
                     Output('card'+value, 'style'),
                     ],
                    [Input(value, 'n_clicks'),
                    Input(value, 'id')],
                    )
                        
            
    def generate_output_callback(value,idvalue):
        
        #print("update_output_DISTRICT_DETAILS",value,idvalue)
        DISTRICT_GRAPH=[]
        STATE_GRAPH=[]
        style={"width":"18rem","height":"8.2rem","margin-bottom":"0.5rem","margin-left":"0.5rem","margin-top":"0.5rem"}
        styleNew={"width":"64vw","height":"70vh","margin-bottom":"0.5rem","margin-left":"0.5rem","margin-top":"0.5rem","margin-right":"0.5rem","overflowY":"auto"}
        if value is not None and value>=0:
            
            if  value%2!=0:
       
                
                dff = ReadMembersListfromCSV()
                
                if len(dff)>0:
                    
                    
                    
                    
                    dff['date'] = (pd.to_datetime(dff['date'],format=('%d/%m/%Y %H:%M:%S')).dt.date).astype(str)
                    Dfsum=dff[dff['districtname']==idvalue]

                    Dfsum=Dfsum.groupby('date').count()
                    
                    Dfsum['date'] = Dfsum.index
                    
                    Dfsum=Dfsum.reset_index(drop=True)
                    
                    #print(Dfsum[['date','districtname']])
                    
    
                 
                    #print(df_value_counts)
                    
                else:
                       return "No Data",styleNew
                if len(Dfsum)>0 and len(dff)>0:
                    
                    
                    DISTRICT_GRAPH=dcc.Graph(
                        id="counts",
                        figure={
                            "data": [
                                {
                                    "x": Dfsum["date"],
                                    "y": Dfsum["districtname"] if "districtname" in Dfsum else [],
                                    "type": "bar",
                                    "marker": {"color": "#0074D9"},
                                }
                            ],
                            "layout": {
                                "xaxis": {"automargin": True},
                                "yaxis": {"automargin": True},
                                "height": 400,
                              
                                "margin": {"t": 150, "l": 50, "r": 50,"b":50},
                                'title':"   District:Members",
                            },
                        },
                    )
                    
                
                
      
        
                dfnew=dff[dff['districtname']==idvalue]
                dfnew=dfnew.reset_index()
                
                STATENAME=dfnew['statename'][0]
                # print(STATENAME)
                
                dfnew=dff[dff['statename']==STATENAME]
                
                Dfsum=dfnew.groupby('date').count() 
                
                Dfsum['date'] = Dfsum.index
                
                Dfsum=Dfsum.reset_index(drop=True)
          
                if len(Dfsum)>0 and len(dff)>0:
                    
                   
                    STATE_GRAPH=dcc.Graph(
                        id="counts2",
                        figure={
                            "data": [
                                {
                                    "x": Dfsum["date"],
                                    "y": Dfsum["statename"] if "statename" in Dfsum else [],
                                    "type": "bar",
                                    "marker": {"color": "#0074D9"},
                                }
                            ],
                            "layout": {
                                "xaxis": {"automargin": True},
                                "yaxis": {"automargin": True},
                                "height": 400,
                               
                                "margin": {"t": 150, "l": 50, "r": 50,"b":50},
                                'title':"   State:Members",
                            },
                        },
                    )    
                        

                  

                    
                return [DISTRICT_GRAPH,STATE_GRAPH],styleNew
            else:
                return '',style
            #print(SUBDISTRICTNAME)
      

        return "",style




    
    
    


# @app.server.route('/test_download')
# def download_excel():
    
#     if current_user.is_authenticated:
#         import flask
#         import io
#         param = flask.request.args
#         print(param)
    
#         df=Read_DataBase("MEMBERS_USERS_MANAGEMENT")
    
#         #Convert DF
#         str_io = io.StringIO()
#         df.to_csv(str_io, sep=",")
    
#         mem = io.BytesIO()
#         mem.write(str_io.getvalue().encode('utf-8'))
#         mem.seek(0)
#         str_io.close()
    
#         return flask.send_file(mem,
#                            mimetype='text/csv',
#                            attachment_filename='downloadFile.csv',
#                            cache_timeout=1000,
#                            as_attachment=True)    
#     else:
#         return ("You are not Authorized")
  
        
  
@app.server.route('/test_download')
def download_excel():
    
    if current_user.is_authenticated or session.get("login")==1:
       

        df=Read_DataBase("MEMBERS_USERS_MANAGEMENT")
    
        file_name = 'ApnaDalMembersList.xlsx'
        df.to_excel(file_name)
    
        return flask.send_file(file_name,
                          
                            attachment_filename='ApnaDalMembersList.xlsx',
                            cache_timeout=1000,
                            as_attachment=True)    
    else:
        return ("You are not Authorized")
    
    
    
 
    
 
    
def LoadStatusInfoPageHistoryM():
    
    import os
   
    #print("Called Status Row")   
    import os

    path='./CSV/RepairLifeCycleEntry.csv'
         
    if os.path.exists(path):
             
        try:
            dfFile = pd.read_csv(path)
            return dfFile
                 
        except :
            dfFile = pd.DataFrame()
            return dfFile
        
        
    dfFile = pd.DataFrame()
    return dfFile    
        
        
        
       
# @app.callback(
#     Output('MemberInfoDisplayDialog', "children"),
#     Input('table-paging-with-graph', "active_cell"),    
#     State('table-paging-with-graph', 'data'))

# def getMemberInfoDialog(active_cell,table_data):

#     if active_cell:
#         cell = json.dumps(active_cell, indent=2)    
#         row = active_cell['row']
#         col = active_cell['column_id']
        
#         print("getMemberInfoDialog",col)
#         # row=row+page_current*page_size
#         value = table_data[row][col]
#         out = '%s\n%s' % (cell, value)
       
       
#         df=ReadMembersListfromCSV()

#         df['key']=df['key'].str.upper()
        
#         dfFiltered=df[df['key']==str(value).upper()]
        
#         if len(dfFiltered)>0 and col=='key':
        
#             # probValue=table_data[row]
#             #print("dfFiltered1",dfFiltered['gender'])
            
#             print(table_data[row])
    
    
#             rows=[]
#             for x in dfFiltered.columns:
#                 if x!="key":
#                   row= html.Tr([html.Th(x.upper()), html.Th(dfFiltered[x])])
#                   rows.append(row)
               
    
#             table_body = [html.Tbody(rows)]
#             table = dbc.Table(table_body, bordered=True)
            
            
            
#             return dbc.Modal(
#                         [
#                             dbc.ModalHeader(dbc.Row
                                            
#                                             ([
                                
#                                                     dbc.Label(dfFiltered['name'].str.upper()+" "+"Details",
                                                              
                                                              
#                                                             style={"font-weight":"bold","color":"green",
                                                                   
#                                                                    # "text-align":"center",
#                                                                    "font-size":"20px"
                                                                   
#                                                                    }),
                                                    
                                                    
#                                                     # dbc.Label("सदस्य विवरण'",
#                                                     #           style={"font-weight":"bold","color":"blue",
                                                                     
#                                                     #                  "text-align":"center",
#                                                     #                  "font-size":"15px"
                                                                     
#                                                     #                  },
                                                              
#                                                     #           ),
                            
                                
#                                                 ],
                      
#                                                     ),style={"border":"2px solid green","text-align":"center"}
#                                             ),
                            
                            
                            
#                             dbc.ModalBody(
                                
                                
#                                 [
                                   
                                    
    
                                        
#                                     table,
                                    
                                 
                                 
                                 
#                                  ]),
                            
#                             dbc.ModalFooter(  
#                                 [
                               
#                                 ]
#                                 ),
                            
                           
                           
#                         ],
#                         id="modal-body-scroll",
#                         scrollable=True,
#                         is_open=True,
#                         centered=True,
#                         keyboard =False,
#                         backdrop="static",
#                         style={"z-index":"555555555555"}
#                     ),

#         else:
#             return ""
        
        
        
        
        
@app.callback(
    Output('MemberInfoDisplayDialog', "children"),
    Input('table-paging-with-graph', "active_cell"),    
    State('table-paging-with-graph', 'data'))

def getMemberInfoDialogfromTable(active_cell,table_data):

    if active_cell:
        cell = json.dumps(active_cell, indent=2)    
        row = active_cell['row']
        col = active_cell['column_id']
        
      
       
        dfFiltered=pd.DataFrame.from_dict(table_data)
        dfFiltered['key']=dfFiltered['key'].str.upper()
        
        value = table_data[row][col]
        dfFiltered=dfFiltered[dfFiltered['key']==str(value).upper()]
        # dfFiltered.columns=['ssid','key','name','gender','statename','districtname','assemblyname','block','pincode','contactno','emailid','address','date']
        

      
        # print(dfFiltered)
        columns=['ssid','key','name','gender','statename','districtname','assemblyname','block','pincode','contactno','emailid','address','date']
        # print(dfFiltered['gender'])
        if len(dfFiltered)>0 and col=='key':
        

    
    
            rows=[]
            for x in columns:
                # print("dfFiltered[x]",dfFiltered[x],x)
                if x!="key":
                  row= html.Tr([html.Th(str(x).upper()), html.Th(dfFiltered[x])])
                  rows.append(row)
               
    
            table_body = [html.Tbody(rows)]
            table = dbc.Table(table_body, bordered=True)
            
            
            
            return dbc.Modal(
                        [
                            dbc.ModalHeader(dbc.Row
                                            
                                            ([
                                
                                                    dbc.Label(dfFiltered['name'].str.upper()+" "+" Details",
                                                              
                                                              
                                                            style={"font-weight":"bold","color":"green",
                                                                   
                                                                    "text-align":"center",
                                                                   "font-size":"20px"
                                                                   
                                                                   }),
                                                    
                                                    
                                                    # dbc.Label("सदस्य विवरण'",
                                                    #           style={"font-weight":"bold","color":"blue",
                                                                     
                                                    #                  "text-align":"center",
                                                    #                  "font-size":"15px"
                                                                     
                                                    #                  },
                                                              
                                                    #           ),
                            
                                                   
                                                ],style={"text-align":"center",}, 
                      
                                                    ),style={"border":"2px solid green","text-align":"center"}
                                            ),
                            
                            
                            
                            dbc.ModalBody(
                                
                                
                                [
                                   
                                    
    
                                        
                                    table,
                                    
                                 
                                 
                                 
                                 ]),
                            
                            dbc.ModalFooter(  
                                [
                               
                                ]
                                ),
                            
                           
                           
                        ],
                        id="modal-body-scroll",
                        scrollable=True,
                        is_open=True,
                        centered=True,
                        keyboard =False,
                        backdrop="static",
                        style={"z-index":"555555555555"}
                    ),

        else:
            return ""        