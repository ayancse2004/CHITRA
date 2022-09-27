#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:29:58 2022

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
from flask import Flask
from views.UserMemberFormEntry import Com_dropdown_STATE,Com_dropdown_PERSONNAME,Com_dropdown_PERSON_ADDRESS_DETAILS
from views.UserMemberFormEntry import USER_FORM
from dash import Input, Output, html, no_update
from views.page2 import Com_dropdown_problem,updateDateBaseLatest,updateDateBaseHistory
from views.UserMemberFormEntry import Com_dropdown_STATE


StyleInput={"text-align": "left","margin-left":'0rem','font-size':'1rem',"margin-top":'0.5rem',}
def ReadPortfolioListfromCSV(path):
    import os
    if os.path.exists(path):
             
        try:
            dfFile = pd.read_csv(path)
            return dfFile
                 
        except :
            dfFile = pd.DataFrame()
            return dfFile
        
        
    dfFile = pd.DataFrame()
    return dfFile    




def CreateADSLIST():
   dfAds=ReadPortfolioListfromCSV('./CSV/NewMembersList.csv')
   arr=[]
   
   for num in (dfAds['ssid']):
      #print("num",num)
      arr.append(num)
    

   return arr



def CreateRoleLIST():
   path='./CSV/portfolio.csv'
   dfAds=ReadPortfolioListfromCSV(path)
   arr=[]
   
   for num in (dfAds['postrole'].unique()):
      #print("num",num)
      arr.append(num)
    
   # print("arr",arr) 
   return arr


def CreateRoleLISTforDropdown(level):
   path='./CSV/portfolio.csv'
   dfAds=ReadPortfolioListfromCSV(path)
   arr=[]
   
   dfAds=dfAds.loc[dfAds['name']==level]
   # print('dfAds',dfAds)
   
   for num in (dfAds['postrole'].unique()):
       arr.append(num)
    
   # print("arr",arr) 
   return arr




def CreateContactNoLIST():
   path='./CSV/NewMembersList.csv'
   dfAds=ReadPortfolioListfromCSV(path)
   arr=[]
   
   for num in (dfAds['contactno']):
      #print("num",num)
      arr.append(num)
    

   return arr

ADS_NUBERLIST=CreateADSLIST()

ROLEList=CreateRoleLIST()

# print(ROLEList)

MobileNumberList=CreateContactNoLIST()




Postinglayout= dbc.Card(
       [
            dbc.CardHeader(id="NewContent"
               
                ),
            
            dbc.CardBody(html.Div(id="NewContent1", className="card-text")
                         
                         
                         ),
        ]
       )


portfolioLayout=html.Div([
    
    html.Div(
    [
    
    
       html.Div("Portfolio Management",style={"font-weight":"bold","text-align":"center","color":"blue","font-size":"3.0vmin"}),
       # html.Marquee("NOTE: File headers must be the following and in the same order: [name gender	address	block pincode statename	 districtname assemblyname	contactno emailid]",style={"font-weight":"bold","background-color":"yellow","color":"red"}),

       dbc.Tabs(
           [
               dbc.Tab(label="Existing Designation", tab_id="tab-first",label_style={"color": "#000f08"}),
               dbc.Tab(label="Create Designation", tab_id="tab-second",label_style={"color": "#000f08"}),
               # dbc.Tab(label="Delete the Records", tab_id="tab-third",label_style={"color": "#000f08"}),
           ],
           id="tabs_portfolio",
           active_tab="tab-first",
        
           style={'color':'black',"background-color": "rgb(215, 225, 219)", 'fontWeight': 'bold',}
       ),
       
      
       
       
       
    
    
    ],
    ),
    # html.Div(id="tabContent" ,)
    Postinglayout,
    
    ],
    
    )

StyleLabel={"textAlign": "left","fontWeight":"bold","color":"#2b0593","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.8rem'}
StyleInput1={"textAlign": "left","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.5rem'}





CreatePostLayout=html.Div([
        
    
        
    dbc.Row([
        
        
        dbc.Col(
                        dbc.Label("Enter Post Level(Ex-National,State..etc)", html_for="dropdown",style=StyleLabel), md=3,sm=12,xs=12,style={"text-align":"left"}
           ),
        dbc.Col(
           
                        dbc.Input(id="Level",placeholder="Enter Level Name...", type="text",value="",style=StyleInput1),md=3,sm=12,xs=12
            ),
        
        
        ]),
    dbc.Row([
    
        
        dbc.Col(
                        dbc.Label("Enter New Post Name(Ex-President,Cheif Minister... etc)", html_for="dropdown",style=StyleLabel), md=3,sm=12,xs=12,style={"text-align":"left"}
           ),
        dbc.Col(
           
                        dbc.Input(id="AddPost",placeholder="Enter Designation Name...", type="text",value="",style=StyleInput1),md=3,sm=12,xs=12
            ),
        ],style={"text-align":"left","font-weight":"bold",}),
        
        dbc.Row(
            
          dbc.Col(  dbc.Button("Add New Post",id="Add_design",n_clicks=0),md=4,sm=6,xl=6,style={"textAlign": "left","margin-top":'0.5rem'})
            
            ),
         
       
      
    html.Br(),
    # dbc.Row(
    #     [
            
    #         dbc.Button("Add",id="Add_design",n_clicks=0)
            
            
    #         ]),
    
    html.Div(id="Add_Status")
    
    ])



# CommonPostLayout= dbc.Card(
#        [
#             dbc.CardHeader(
#                 dbc.Tabs(
#                     [
#                         dbc.Tab(label="Existing", tab_id="existing",label_style={"color": "#000f08"}),
#                         dbc.Tab(label="Create", tab_id="create" ,label_style={"color": "#000f08"}),
                        
#                     ],
#                     id="Portfolio-card-tabs",
#                     active_tab="existing",
#                     style={'color':'green',"background-color": "rgb(207, 212, 242)", 'fontWeight': 'bold',}
#                 )
#             ),
            
#         ]
#  )



ADSFilterLayout=html.Div([
    
        
  dbc.Row([
      
    
   
     
         
         dbc.Col(
                         dbc.Label("Enter Membership Number(अपनी सदस्यता संख्या दर्ज करें)", html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left",}
            ),
         dbc.Col(
                     dcc.Dropdown(
                                 id="SSID_Port",
                                 options=[{'label':name, 'value':name} for name in ADS_NUBERLIST],
                                 clearable=False,
                                 style=StyleInput1,
                                 ),md=4,sm=12,xs=12,
            ),
        
     
     
          
        

        
         ],style={"text-align":"center","font-weight":"bold",}
      ),
    
  
  
    html.Div(id="afterselectSSID",style={"border":"2px solid blue"}),
    
    html.Div(id="afteraddedmemeber")
    
    ])




MobileNumberFilterLayout=html.Div([
    
        
  dbc.Row([
      
    
   
     
         
         dbc.Col(
                         dbc.Label("Enter Mobile Number(अपनी सदस्यता संख्या दर्ज करें)", html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left",}
            ),
         dbc.Col(
                     dcc.Dropdown(
                                 id="Contact_port",
                                 options=[{'label':name, 'value':name} for name in MobileNumberList],
                                 clearable=False,
                                 style=StyleInput1,
                                 ),md=4,sm=12,xs=12,
            ),
        
     
     
          
        

        
         ],style={"text-align":"center","font-weight":"bold",}
      ),
    
  
  
  
    
    html.Div(id="afterSelectContact",style={"border":"2px solid blue"}),
    html.Div(id="afterContactmemeber")
    
    ])



CommonCreateLayout=html.Div([
    dbc.Row([
        
          dbc.Col(MobileNumberFilterLayout ,md=6,xs=12,sm=12,),
          dbc.Col(ADSFilterLayout ,md=6,xs=12,sm=12,)
        
        
        ]
        
        )
    
    
    
    ])


layout=portfolioLayout













@app.callback(Output("NewContent1", "children"),
              [Input("tabs_portfolio", "active_tab")],
              
              
              )
def switch_tab(at
               
               
               
               ):
    if at == "tab-first":
        path='./CSV/portfolio.csv'
        dfFile=ReadPortfolioListfromCSV(path)
        # print("portfolio dfile",dfFile['name'])
        tabs=[]
        for num in (dfFile['name'].unique()):
              #print('num',num)
              idtext="portfolio"+num
              tabs.append(
                 dbc.Tab(
                     label=num,
                     # value=num,
                     tab_id=num,
                     children=[
                         html.Div([
                             
                             dbc.Tabs(
                                 [
                                     dbc.Tab(label="Existing", tab_id="existing",label_style={"color": "#000f08"}),
                                     dbc.Tab(label="Create", tab_id="create" ,label_style={"color": "#000f08"}),
                                     
                                 ],
                                 id="Portfolio-card-tabs"+num,
                                 active_tab="existing",
                                 style={'color':'green',"background-color": "rgb(207, 212, 242)", 'fontWeight': 'bold',}
                             )
                             
                             
                             ],id=idtext),
                         
                         dbc.CardBody(html.Div(id=idtext, className="card-text")),
                         
                         ]
                     ))
              

        
        # return Notifications_Layout1
        return   (dbc.Tabs(
                      id="tabs_port",
                       # value="tab-1",
                        children=tabs,
                        active_tab="NATIONAL",
                    
                       style={'color':'black',"background-color": "rgb(213, 231, 247)", 'fontWeight': 'bold',}
                   
                   ))
    
    elif at == "tab-second":
        return CreatePostLayout
  
    return html.P("This shouldn't ever be displayed...")




# df=ReadMembersListfromCSV()
# for value in df['districtname'].unique():
#     @app.callback(
#                     [Output('outputDiv'+value, 'children'),
#                      Output('card'+value, 'style'),
#                      ],
#                     [Input(value, 'n_clicks'),
#                     Input(value, 'id')],
#                     )
                        
            
#     def generate_output_callback(value,idvalue):





path='./CSV/portfolio.csv'
dfFile=ReadPortfolioListfromCSV(path)

for value in dfFile['name'].unique():
    @app.callback(
        Output("portfolio"+value, "children"), 
        [
         Input("tabs_port", "active_tab"),
         Input("Portfolio-card-tabs"+value, "active_tab"),
         
        ]
         
         
        
    )
    def PostingTabs(active_tabParent,active_Child):
        
        
      
        print("active_tabParent",active_tabParent)
        print("active_Child",active_Child)
        
        
        
        
        path='./CSV/portfoliomembers.csv'
        dfFile=ReadPortfolioListfromCSV(path)
     
        if active_Child == "existing":
            
            data=dfFile[dfFile['postlevel']==active_tabParent]
            #print(data)
            
            tablelayout=dash_table.DataTable(
              id='overall'+active_tabParent+active_Child,
              data=data.to_dict('records'),
              columns=[{"name": i, "id": i} for i in data.columns],
              
              style_table={
                      'minHeight': '16rem',
                      'overflowX': 'scroll',
                      'width': '100%',
                      'minWidth': '100%',
                  },
              style_cell = {
                      'font-family': 'arial',
                      'font-size': '15px',
                      'text-align': 'center'
                  },
              style_header={
              'backgroundColor': '#c9c9c9',
              'color': 'black',
              'fontWeight': 'bold',
              'textAlign': 'center',
              #'border': '1px solid pink',
              },
             
             filter_action="native",
             sort_action="native",
             sort_mode="multi",
             column_selectable="single",
             #row_selectable="multi",
            
             page_action="native",
             page_current= 0,
             page_size= 10,
             

           
            ),
     
    
            # print("PostingTabs\n") 
            return tablelayout
        elif active_Child == "create":
           # print("PostingTabs Created\n")
           return CommonCreateLayout
      
       
        
        return html.Div("This shouldnmm't ever be displayed...")
    




@app.callback(
    Output("Add_Status", "children"), 
    [
     
     Input("Add_design", "n_clicks"),
     State("AddPost", "value"),
     State("Level","value"),
    ]
     
     
    
)
def AddDesignationtoCSV(n_clicks,value,level):
    
  if n_clicks:
      if len(value)>0:
          path='./CSV/portfolio.csv'
          dfFile=ReadPortfolioListfromCSV(path)
          
    
          data = {'id':[len(dfFile)+1], 'name':[level.upper()],'postrole':[value.upper()]}
          df = pd.DataFrame(data=data)
          if len(dfFile)>0:
              mask=df['name'].values in dfFile['name'].values
              if mask:
                  mask2=df['postrole'].values in dfFile['postrole'].values
                  if mask2:
                    return("Designation already Exist {}".format(df['name'].values))
                  else:
                      df.to_csv(path,mode='a', header=False, index=False)
                      
                      return("Added Succesfully {}".format(df['name']))
                  
              else:
                  df.to_csv(path,mode='a', header=False, index=False)
                  
                  return("Added Succesfully {}".format(df['name']))
                  
    
    
             
             
          
      else:
              layout2="Mobile Entery is not Ok(मोबाइल ठीक नहीं है) "
      # print("n_clicks")





@app.callback(
    
     
    Output('afterselectSSID', 'children'),
    

    Input('SSID_Port','value')  ,  
   
    Input("tabs_port", "active_tab"),
    Input("Portfolio-card-tabs"+value, "active_tab"),
 
 
    
 
    

    
    
)
def FilterWithSSID(ssid,parent,child):
    
    data=ReadPortfolioListfromCSV("./CSV/NewMembersList.csv")
    fildata=data[data['ssid']==ssid]
    style={"text-align":"center",'display':'block',"background-color":"white","border":"none",
           "color":"blue","text-decoration":"underline","font-weight":"bold",'cursor':'grab','padding-top':'0.2rem'}
    styleDisable={"text-align":"center",'display':'none'}
    PROBLEM_LIST=["Appointment Related","Job-Related",'Land Related','Problem']
 
    
    # print("FilterwithSSID",parent,child)

    ROLEList=CreateRoleLISTforDropdown(parent)
     
    if len(fildata)==1:
        if len(ssid)>0:
            # print(fildata['contactno'])
            fildataM=fildata[fildata['ssid']==(ssid)]
           
       
            if len(fildataM)==1:
                
                MEMBERINFOOVERALL=dbc.Row([
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your State(आपका राज्य)", html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_STATE_P",placeholder=" Your state..", type="text",disabled =True,
                                      
                                      value=fildataM['statename'],style=StyleInput1),md=4,sm=12,xs=12,
                            ),
                        
                        ]),
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your District(आपका जिला)" , html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_DISTRICT_P",placeholder=" Your district..", type="text",disabled =True,
                                      
                                      value=fildataM['districtname'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Sub-District(आपका उप-जिला)" , html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_SUB_DISTRICT",placeholder=" Your Sub-district..", type="text",disabled =True,
                                      
                                      value=fildataM['assemblyname'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                    
                    
                    
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Name(आपका  नाम)" , html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_NAME",placeholder=" Your Name..", type="text",disabled =True,
                                      
                                      value=fildataM['name'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                    
                    dbc.Row([
                        
                        dbc.Col(
                                 dbc.Label("Mobile Number", html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="Mobile_no",placeholder=" Your Number..", type="text",disabled =True,
                                      
                                      value=fildataM['contactno'],style=StyleInput1),md=4,sm=12,xs=12,
                            ),
                        
                        ]),
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Gender(आपका लिंग )"  , html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_GENDER",placeholder=" Your Gender..", type="text",disabled =True,
                                      
                                      value=fildataM['gender'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                 
                    
                    # html.Hr(),    
                 
                    
                 
                    dbc.Col(
                             dbc.Label("Assign Role for State/District/Sub District",id="assignedrole" ,html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,style={"text-align":"center"}
                       ),
             
                
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Assign Role",id="assignedrole" ,html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4,style={"text-align":"left"}
                           ),
                       
                        dbc.Col(
                            
                                dcc.Dropdown(
                                            id="Assigned_Role",
                                            options=[{'label':name, 'value':name} for name in ROLEList],
                                            clearable=False,
                                            style=StyleInput,
                                            ),md=12,sm=12,xs=12,lg=8,xl=8
                                
                                ),
                    
                                             
                        
                        
                        ],style={"text-align":"center"}),
                    
                    # html.Hr(),
                    
                    Com_dropdown_STATE,
                    
                    dbc.Row([
                        dbc.Col(
                            
                                dbc.Button("Update", size="sm", className="me-1",id='updateRole',n_clicks=0,style={"text-align":"center","margin-top":"2rem","background-color":"green"}),
                              md=12,
                                
                                ),
                    
                                             
                        
                        
                        ],style={"text-align":"center"}),

                       ],style={"text-align":"left","font-weight":"bold",}),
                   
                return MEMBERINFOOVERALL

                



@app.callback(
    Output("afteraddedmemeber", "children"), 
    [
     
     Input("updateRole", "n_clicks"),
     State("Assigned_Role", "value"),
     State("SSID_Port", "value"),
     State('Part_Com_DROP_STATE','value'),
     State('Part_Com_DROP_DISTRICT','value'),
     State("tabs_port", "active_tab"),
     
    ]
     
     
    
)

def AddUpdatedMemberToCSVSSID(n_clicks,value,ssid,state,district,parent_tab):
    
  if n_clicks:
      if value:
          path='./CSV/portfoliomembers.csv'
          dfFile=ReadPortfolioListfromCSV(path)
          
          start_date_object = datetime.today().strftime('%d-%m-%Y')
          end_date_object=datetime.now()
          
        
          data = {'id':[len(dfFile)+1],'postname':[value.upper()],'ssid':ssid,'stateincharge':state,'districtincharge':district,'postlevel':parent_tab,'fromdate':[start_date_object],'todate':['']}
          
          # print("data",data)
          df = pd.DataFrame(data=data)
          if len(dfFile)>=0:
              mask=df['ssid'].values in dfFile['ssid'].values
              if mask:
                  mask2=df['postname'].values in dfFile['postname'].values
                  if mask2:
                     
                     return("Designation already Assigned for the above member{}".format(df['postname'].values))
                  
                  else:
                     df.to_csv(path,mode='a', header=False, index=False)
                  
                     return("Updated Succesfully {}".format(df['ssid']))
                  
    
    
             
             
          
              else:
                 df.to_csv(path,mode='a', header=False, index=False)
          
                 return("Updated Succesfully {}".format(df['ssid']))
              
      else:
         return("Assign The Role before Update")
      




@app.callback(
    
     
    Output('afterSelectContact', 'children'),
    

    Input('Contact_port','value')  ,  
    Input("tabs_port", "active_tab"),
    Input("Portfolio-card-tabs"+value, "active_tab"),
    # Input('','value'), 
    
)
def FilterWithMobileNo(contactno,parent,child):
    
    data=ReadPortfolioListfromCSV("./CSV/NewMembersList.csv")
   
    
    fildata=data[data['contactno']==contactno]
  
    ROLEList=CreateRoleLISTforDropdown(parent)

     
    if len(fildata)==1:
       
           
        # if len(str(contactno))==10:
        #     # print(fildata['contactno'])
        #     fildataM=fildata[fildata['contactno']==int(contactno)]
           
       
        #     if len(fildataM)==1:
                
                MEMBERINFOOVERALL=dbc.Row([
                    dbc.Row([
                        
                        dbc.Col(
                                 dbc.Label("SSID Number(एसएसआईडी नंबर)", html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="SSID_M",placeholder=" Your state..", type="text",disabled =True,
                                      
                                      value=fildata['ssid'],style=StyleInput1),md=4,sm=12,xs=12,
                            ),
                        
                        ]),
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your State(आपका राज्य)", html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_STATE_M",placeholder=" Your state..", type="text",disabled =True,
                                      
                                      value=fildata['statename'],style=StyleInput1),md=4,sm=12,xs=12,
                            ),
                        
                        ]),
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your District(आपका जिला)" , html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_DISTRICT_M",placeholder=" Your district..", type="text",disabled =True,
                                      
                                      value=fildata['districtname'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Sub-District(आपका उप-जिला)" , html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_SUB_DISTRICT_M",placeholder=" Your Sub-district..", type="text",disabled =True,
                                      
                                      value=fildata['assemblyname'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                    
                    
                    
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Name(आपका  नाम)" , html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_NAME_M",placeholder=" Your Name..", type="text",disabled =True,
                                      
                                      value=fildata['name'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                    
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Gender(आपका लिंग )"  , html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_GENDER_M",placeholder=" Your Gender..", type="text",disabled =True,
                                      
                                      value=fildata['gender'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                 
                    
                    # html.Hr(),   
   
                 
                               
                    dbc.Col(
                             dbc.Label("Assign Role for State/District/Sub District",id="assignedrole" ,html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,style={"text-align":"center"}
                       ),
             
                
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Assign Role",id="assignedrole" ,html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4,style={"text-align":"left"}
                           ),
                       
                        dbc.Col(
                            
                                dcc.Dropdown(
                                            id="Assigned_RoleMobile",
                                            options=[{'label':name, 'value':name} for name in ROLEList],
                                            clearable=False,
                                            style=StyleInput,
                                            ),md=12,sm=12,xs=12,lg=8,xl=8
                                
                                ),
                    
                                             
                        
                        
                        ],style={"text-align":"center"}),
                    
                    
                    
                    
                    # html.Hr(),
          
                    Com_dropdown_STATE,
                    
                    
                    
                    dbc.Row([
                        dbc.Col(
                            
                                dbc.Button("Update", size="sm", className="me-1",id='updateRoleC',n_clicks=0,style={"text-align":"center","margin-top":"2rem","background-color":"green"}),
                              md=12,
                                
                                ),
                    
                                             
                        
                        
                        ],style={"text-align":"center"}),

                       ],style={"text-align":"left","font-weight":"bold",}),
                   
                return MEMBERINFOOVERALL

    else:
        return ""


@app.callback(
    Output("afterContactmemeber", "children"), 
    [
     
      Input("updateRoleC", "n_clicks"),
      State("Assigned_RoleMobile", "value"),
      State("SSID_M", "value"),
      
      
      State('Part_Com_DROP_STATE','value'),
      State('Part_Com_DROP_DISTRICT','value'),
      State("tabs_port", "active_tab"),
    ]
     
     
    
)

def AddUpdatedMemberToCSV(n_clicks,value,ssid,state,district,parent_tab):
    
  if n_clicks:
      if value:
          path='./CSV/portfoliomembers.csv'
          dfFile=ReadPortfolioListfromCSV(path)
          
          start_date_object = datetime.today().strftime('%d-%m-%Y')
          end_date_object=datetime.now()
          
          data = {'id':[len(dfFile)+1],'postname':[value.upper()],'ssid':ssid,'stateincharge':state,'districtincharge':district,'postlevel':parent_tab,'fromdate':[start_date_object],'todate':['']}
          
          #print("data",data)
          df = pd.DataFrame(data=data)
          if len(dfFile)>=0:
              mask=df['ssid'].values in dfFile['ssid'].values
              if mask:
                  mask2=df['postname'].values in dfFile['postname'].values
                  if mask2:
                     
                      return("Designation already Assigned for the above member{}".format(df['postname'].values))
                  
                  else:
                      df.to_csv(path,mode='a', header=False, index=False)
                  
                      return("Updated Succesfully {}".format(df['ssid']))
                  
    
    
             
             
          
              else:
                  df.to_csv(path,mode='a', header=False, index=False)
          
                  return("Updated Succesfully {}".format(df['ssid']))
              
      else:
          return("Assign The Role before Update")
      
  else:
      return ""