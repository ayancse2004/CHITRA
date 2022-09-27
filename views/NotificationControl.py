#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:00:35 2022

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
 
from views.page1 import Read_DataBase
from views.page1 import CommonCreateAndUpdate_DataBase
from views.page1 import Update_DataBaseByStatus
from views import UserMemberFormEntry
from views.StateWiseData import StateName,DistrictNameByStateName,SubDistrictNameByStateName

from views.UserMemberFormEntry import ReadMembersListfromCSV
from dash.exceptions import PreventUpdate
import smtplib

try:
    import httplib
except:
    import http.client as httplib


from datetime import datetime
from views.EmailLogin import emailLayout

from views.UploadFile import layoutUploadFile











STATENAME=StateName()



Notifications_Layout= dbc.Card(
       [
            dbc.CardHeader(
                dbc.Tabs(
                    [
                        dbc.Tab(label="All Group(सभी समूह)", tab_id="sms-N",label_style={"color": "#000f08"}),
                        dbc.Tab(label="Create Group(समूह बनाना)", tab_id="e-mailN" ,label_style={"color": "#000f08"}),
                        
                      
                        
                        # dbc.Tab(label="Not Completed Complain Page", tab_id="NotCompleted",label_style={"color": "#000f08"}),
                        
                        # dbc.Tab(label="Completed Complain Page", tab_id="Completed" ,label_style={"color": "#000f08"}),
                        # dbc.Tab(label="Overall/Details Page", tab_id="Overall" ,label_style={"color": "#000f08"}),
                        # dbc.Tab(label="Analysis View Page", tab_id="Analysis" ,label_style={"color": "#000f08"}),
                    ],
                    id="Notifications-card-tabs",
                    active_tab="sms-N",
                    style={'color':'green',"background-color": "rgb(207, 212, 242)", 'fontWeight': 'bold',}
                )
            ),
            dbc.CardBody(html.Div(id="Notifications-card-content", className="card-text")),
        ]
 )


Com_dropdown_STATE =dbc.Row(
    [
     dbc.Row([
         dbc.Col(
             
                 dbc.Label("Select Your State(अपना राज्य चुनें) ", html_for="dropdown",),md=12,sm=12,xs=12,lg=4,xl=4
                 ),
             dbc.Col(    
                 dcc.Dropdown(
                             id="Com_DROP_STATE",
                             options=[{'label':name, 'value':name} for name in STATENAME],
                             # value="",
                             clearable=False,
                             # style=StyleInput,
                             )
                 ,md=12,sm=12,xs=12,lg=8,xl=8
                 
             ),
      ],className="row justify-content-center"),
     html.Br(),
    dbc.Row(
             [
                 dbc.Col(
                     dbc.Label("Select Your District(अपने जिले का चयन करें) ", html_for="dropdown" ,),md=12,sm=12,xs=12,lg=4,xl=4
                     
                     ),
                 dbc.Col(
                     dcc.Dropdown(
                                 id="Com_DROP_DISTRICT",
                                 options=[{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],
                                 clearable=True,
                                 # style=StyleInput,
                                 ),
                         md=12,sm=12,xs=12,lg=8,xl=8
                     ),
                 ],className="row justify-content-center"),
       
     
])


def LoadStatusInfoPageLatest():
    
    import os
   
    #print("Called Status Row")   
    path='./CSV/RepairLifeCycleEntry.csv'
    if os.path.isfile(path):
        try:
            dfFile = pd.read_csv(path)
        except :
            dfFile = pd.DataFrame()
           
            
        if len(dfFile.index)>0:
                return dfFile
        else:
            dfFile.loc[0] = 'INVALID'
       
            #print(dfFile)
            return dfFile
             
    else:
        pd.DataFrame()
        
        
dfFileLatest=LoadStatusInfoPageLatest()

dfFileLatest_Completed=dfFileLatest[dfFileLatest['taskstatus']=='Completed']

dfFileLatest_InProgress=dfFileLatest[dfFileLatest['taskstatus']=='InProgress']
dfFileLatest_InProgress.insert(7, 'transferredto', '')


# Filtered Table
FilteredTable=html.Div([
    
    dbc.Button("Select All", color="success", className="me-1",id="select-all-button"),
        dbc.Button("Deselect All", color="warning", className="me-1",id="deselect-all-button"),
    dash_table.DataTable(
        id='table-dropdown-ntf',
  
        columns=[
            # {'id': 'key', 'name': 'key','editable': False},
            {'id': 'ssid', 'name': 'Member ID', 'editable': False},
            {'id': 'name', 'name': 'Name','editable': False},
            {'id': 'statename', 'name': 'State','editable': False},
            {'id': 'districtname', 'name': 'District Name','editable': False},
            {'id': 'contactno', 'name': 'Contact No', 'presentation': 'dropdown'},
            {'id': 'emailid', 'name': 'Email-ID','editable': False},
            
            # {'id': 'assignto', 'name': 'Current Assignee','editable': False},
             # {'id': 'ssid', 'name': 'Member ID', 'presentation': 'dropdown'},
            # {'id': 'taskstatus', 'name': 'Status   .','presentation': 'dropdown'},
            # {'id': 'complaintdate', 'name': 'Complaint date (dd-mm-yyyy)','editable': False},
            # {'id': 'attendeddate', 'name': 'Attended date','editable': True},
            # {'id': 'closeddate', 'name': 'Closed date','editable': True},
            
          
        ],
      
        
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
        page_current= 0,
        page_size= 10,
   
        
        style_table={
                'minHeight': '16rem',
                'overflowX': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
        
       
        css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
          

       
        editable=True,
        # row_deletable=True,
        row_selectable="multi",    
       
        filter_action='native',
     
        
        
       
            
            
        
    ),
    html.Br(),
    dbc.Col(
        
      dbc.InputGroup(
            [
                dbc.InputGroupText("Message"),
                dbc.Textarea(id="mail_message",value=''),
            ],
            className="mb-3",
        ),
        
        ),
    
    dbc.Row(
        [
        dbc.Col(
            [
                dbc.Button(
                            "Send Mail", id="send_mail", className="fa fa-paper-plane", n_clicks=0,style={"margin-top":"0.5rem"},
                            ),
                
                
                ],xs=6,lg=1,xl=1,
            
           
            
            ),
   dbc.Col([
       
       
       dbc.Button(
                   "WhatsApp", id="send_whapp", className="fab fa-whatsapp", n_clicks=0,style={"margin-top":"0.5rem","background-color":'green'},

                   ),
       
       ],xs=6,lg=1,xl=1,
       
       ),
   
   # dbc.Col([
       
       
   #     dbc.Button(
   #                 "WhatsApp Group", id="send_whGroup", className="fab fa-whatsapp", n_clicks=0,style={"margin-top":"0.5rem","background-color":'green'},

   #                 ),
       
   #     ],xs=6,lg=2,xl=2,
       
   #     )
  
   
    ],
   className="g-0",
    
    ),
  
   
   

    

    html.Br(),
    html.Div(id='WAgroupDiv'),
    html.Div(id='StatusAlert'),
])


StyleLabel={"text-align": "left","fontWeight":"bold","color":"#2b0593","margin-left":'0.6rem','font-size':'1rem',"margin-top":'0.8rem'}
StyleInput={"text-align": "left","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.5rem',}
StyleInput1={"text-align": "left","margin-left":'0.6rem','font-size':'1rem',"margin-top":'0.5rem'}



GROUPTABLE=html.Div([
    

    
    dash_table.DataTable(
        id='table-group',
  
        columns=[
            # {'id': 'key', 'name': 'key','editable': False},
            {'id': 'key', 'name': 'key', 'editable': False},
            {'id': 'name', 'name': 'Group Name','editable': False},
            {'id': 'id', 'name': 'ID','editable': False},
         
        ],
      
        
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
        page_current= 0,
        page_size= 10,
   
        
        style_table={
                'minHeight': '16rem',
                'overflowX': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
        
       
        css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
          

       
        editable=True,
        # row_deletable=True,
         
       
        filter_action='native',
     
 
        
    ),
    ])


GROUPTABLEALL=html.Div([
    
    dbc.Button("Select All", color="success", className="me-1",id="select-all-button-group"),
    dbc.Button("Deselect All", color="warning", className="me-1",id="deselect-all-button-group"),
    
    dash_table.DataTable(
        id='table-group-all',
  
        columns=[
            # {'id': 'key', 'name': 'key','editable': False},
            {'id': 'key', 'name': 'key', 'editable': False},
            {'id': 'name', 'name': 'Group Name','editable': False},
            {'id': 'id', 'name': 'ID','editable': False},
         
        ],
        data=Read_DataBase("MEMBERS_WHATSAPP_GROUP").to_dict('records')  ,
        
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
        page_current= 0,
        page_size= 10,
   
        
        style_table={
                'minHeight': '16rem',
                'overflowX': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
        
       
        css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
          

       
        editable=True,
        # row_deletable=True,
        row_selectable="multi",    
       
        filter_action='native',
     
 
        
    ),
    ])






WhatsappGrpLayout=html.Div([
    
    

    
   dbc.Row(
        [
         
         dbc.Row([
             
             dbc.Col(
                             dbc.Label("Enter Group Name(समूह का नाम दर्ज करें)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
                ),
             dbc.Col(
                 
              
                             dbc.Input(id="GROUPNAME",placeholder="Enter Group Name...",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8,
                 ),
             
             
             ],className="row justify-content-center"),
         ]),
    
   
   
     
   dbc.Row(
        [
         
         dbc.Row([
             
             dbc.Col(
                             dbc.Label("Enter Group ID(समूह आईडी दर्ज करें)", html_for="dropdown",style=StyleLabel),md=12,sm=12,xs=12,lg=4,xl=4
                ),
             dbc.Col(
                 
              
                             dbc.Input(id="GROUPID",placeholder="Enter Group ID..",style=StyleInput1),md=12,sm=12,xs=12,lg=8,xl=8,
                 ),
             
             
             ],className="row justify-content-center"),
         ]),
   
    
       
       dbc.Row(
           [
               
               
               dbc.Col(
                   [
                       dbc.Button(
                                   "Create Group", id="create_What_Group", className="fa fa-paper-plane", n_clicks=0,style={"margin-top":"0.5rem"},
                                   ),
                       
                       
                       ],xs=6,lg=2,xl=2,style={"text-align":"center"}
                   
                  
                   
                   ),
               
               
               ]
           
           
           ),
       
       
       
       
       html.Hr(),
       html.Div(id="GROUP_Info_USER"),
       html.Hr(),
       GROUPTABLE,
       html.Hr(),
       
        ],
        
        )
    



EmailNotiLayout=html.Div([
    
    dbc.Row(
        Com_dropdown_STATE
        ),
    html.Br(),
    dbc.Row(
        
        FilteredTable
        
        
        )
    
    ],
                                                                         
 )




SMSNotiLayout=html.Div("SMS Notifications Div")




MainNotificationLayout=html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Individual Notification (व्यक्तिगत अधिसूचना)", tab_id="tab-1",label_style={"color": "#000f08"}),
                dbc.Tab(label="Group Notification(समूह अधिसूचना)", tab_id="tab-2",label_style={"color": "#000f08"}),
                dbc.Tab(label="Upload Your File (अपनी फ़ाइल अपलोड करें )", tab_id="tab-3",label_style={"color": "#000f08"}),
            ],
            id="tabs",
            active_tab="tab-1",
         
            style={'color':'black',"background-color": "#8f96c2", 'fontWeight': 'bold',}
        ),
        html.Div(id="contentMain"),
    ]
)


ExistingWhatsappGroupLayout=html.Div([
    
    
    GROUPTABLEALL,
    html.Br(),
    dbc.Row(
        [
            
            
            dbc.Col(
                [
                    
                    dbc.InputGroup(
                          [
                              dbc.InputGroupText("Message"),
                              dbc.Textarea(id="Whatsapp_message",value=''),
                          ],
                          className="mb-3",
                      ),
                    
                    ]
                
                
                
                ),
            
           
       
            ]
    
        ),
    dbc.Row([
        
        dbc.Col(
            
            
            dbc.Button(
                        "Send WhatsApp Message", id="Send_grp_WhatsApp", className="fa fa-paper-plane", n_clicks=0,style={"margin-top":"0.5rem"},
                        ),
            
       
            ),
        
        
        ]),
    html.Div(id="StatusWhatsapp"),
    
    
    ]
    

    )




layout = html.Div([
    
    
     
           
        html.H4('Notifications Management (Web login required for WhatsApp)  सूचना प्रबंधन (व्हाट्सएप के लिए आवश्यक वेब लॉगिन)',style={'textAlign': 'center','color':'black',"background-color": "#f0f3f7",}),
        html.Hr(),
        # cards,
        
        # Notifications_Layout,
        # EmailNotiLayout,
        MainNotificationLayout,
        
        html.Hr(),
           

  
    
       
        ]
    
)



layoutDirect = html.Div([
    
    
       html.Div([
           
        html.H4('Notifications Management (Web login required for WhatsApp)  सूचना प्रबंधन (व्हाट्सएप के लिए आवश्यक वेब लॉगिन)',style={'textAlign': 'center','color':'black',"background-color": "#f0f3f7",}),
        html.Hr(),
        # cards,
        
        # Notifications_Layout,
        # EmailNotiLayout,
        MainNotificationLayout,
        
        html.Hr(),
           
           
           
           ],id='notification',style={'display':'none'}) ,
       
        #html.Div(id="userformentry"),

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
        
        
        ],
    
    
    
)




@app.callback(
  
    Output("table-group-all",'selected_rows'),
    
    Input('select-all-button-group', 'n_clicks'),
    Input('deselect-all-button-group', 'n_clicks'),
    
   
    State('table-group-all','data'),
    State('table-group-all', 'derived_virtual_data'),
     
    )



def sendGroupWhatsAppNotifications(select_n_clicks,deselect_n_clicks,table_data,filtered_rows):
   ctx = dash.callback_context.triggered[0]
   ctx_caller = ctx['prop_id']
   value=[]
   # if selectedRows is not None :
   #      for row in selectedRows:
          
   #              col = 'ssid'
                
                
   #              value.append(table_data[row][col])
            
   # # return value
   # print(value)
   #print(filtered_rows)  
   if filtered_rows is not None:
        if ctx_caller == 'select-all-button-group.n_clicks':
            selected_ids = [row['key'] for row in filtered_rows]
            # print(selected_ids)
            
            return [i for i, row in enumerate(table_data) if row['key'] in selected_ids]
        if ctx_caller == 'deselect-all-button-group.n_clicks':
            return  []
        raise PreventUpdate
   else:
        raise PreventUpdate


@app.callback(
    
    Output("StatusWhatsapp", "children"),
    # Input("send_whapp","n_clicks"),
    Input('Send_grp_WhatsApp','n_clicks'),
    Input('table-group-all', "derived_virtual_data"),
    State('Whatsapp_message', 'value'),
    State('table-group-all', "derived_virtual_selected_rows"),
    State('table-group-all','data')
)




def update_output_DistrictWiseData(send_Wh,rows,message,selected_rows,table_data):
    # print("rows",rows)
    ctx = dash.callback_context.triggered[0]
    ctx_caller = ctx['prop_id']
    from pywhatkit.core import core, exceptions, log
    selectedmailIds=[]
    # selectednames=[]
    # status=False
    layout=""
    status=checkInternetHttplib()
    # ctx_caller == 'select-all-button.n_clicks'
    if   ctx_caller == 'Send_grp_WhatsApp.n_clicks':
          if selected_rows is not None :
              for row in selected_rows:
   
               col = 'id'
               colN='name'
               # selectednames.append(table_data[row][colN])
               selectedmailIds.append(rows[row][col])
 
          # return selectedmailIds
          
          if status:
                for group_id in selectedmailIds:
                      if group_id is not None:
                         now = datetime.now()
                         # print(group_id)
                         #pywhatkit.sendwhatmsg_to_group_instantly(mes, message,)
                         
                         #pywhatkit.sendwhatmsg_to_group("GCrw642HFqpDzIDCLRNw8N", message,15,32)
                      
                     
                         core.send_message(message=message, receiver=group_id, wait_time=10)
                         core.close_tab(wait_time=20)
                         
                         layout= dbc.Alert("SuccessFully Sent!", color="success",  is_open=True
                    ,dismissable=True,)
          else:   
              
                  layout= dbc.Alert("Internet Connection is Unavailable", color="danger",  is_open=True,
                              dismissable=True,)
   

    return layout





@app.callback(Output("contentMain", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return EmailNotiLayout
    elif at == "tab-2":
        return Notifications_Layout
    elif at == "tab-3":
        return layoutUploadFile
    return html.P("This shouldn't ever be displayed...")




def GenerateMail(emailid,message):

    message = "Hi Member "+message
    SUBJECT = "Apna Dal-S "
    TEXT = "This message was sent by Apna Dal-S  Team \n "+ message   
    message1 = 'From: Apna Dal-S\nSubject: {}\n\n{}'.format(SUBJECT, TEXT)




    # message = "Hi Member,"+message
    # SUBJECT = "Lynx Team"
    # TEXT = "This message was sent by Lynx Team \n "+ message  
    # message1 = 'From: Lynx Team\nSubject: {}\n\n{}'.format(SUBJECT, TEXT)
        
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("ajay.cse2004@gmail.com", "whgnysbsgusdexjw")
    s.sendmail('&&&&&',emailid,message1)

# Need to seeeeeeeeee

@app.callback(
  
    Output("table-dropdown-ntf",'selected_rows'),
    
    Input('select-all-button', 'n_clicks'),
    Input('deselect-all-button', 'n_clicks'),
    
  
    State('table-dropdown-ntf','data'),
    State('table-dropdown-ntf', 'derived_virtual_data'),
     
    )



def sendGroupMailNotifications(select_n_clicks,deselect_n_clicks,table_data,filtered_rows):
   ctx = dash.callback_context.triggered[0]
   ctx_caller = ctx['prop_id']
   value=[]
   # if selectedRows is not None :
   #      for row in selectedRows:
          
   #              col = 'ssid'
                
                
   #              value.append(table_data[row][col])
            
   # # return value
   # print(value)
   #print(filtered_rows)  
   if filtered_rows is not None:
        if ctx_caller == 'select-all-button.n_clicks':
            selected_ids = [row['ssid'] for row in filtered_rows]
            # print(selected_ids)
            
            return [i for i, row in enumerate(table_data) if row['ssid'] in selected_ids]
        if ctx_caller == 'deselect-all-button.n_clicks':
            return  []
        raise PreventUpdate
   else:
        raise PreventUpdate




@app.callback(
    
     
     Output('Com_DROP_DISTRICT', 'options'),
     Output('table-dropdown-ntf', 'data'),
 
 
    Input('Com_DROP_STATE', 'value'),
    Input('Com_DROP_DISTRICT', 'value')
)
def update_output_District(state,district):
    
      DISTRICTNAME=['NULL']
      df=ReadMembersListfromCSV()
      if state is not None:
    
          DISTRICTNAME=DistrictNameByStateName(state)
        
          # print("district",district)
          # print("state",state)
         
          # df=df[df['statename']==state]z
          if district is not None:
              df=df[df['districtname']==district]
              return [{'label':name, 'value':name} for name in DISTRICTNAME],df.to_dict('records')
         
          else:
              df=df[df['statename']==state]
              return [{'label':name, 'value':name} for name in DISTRICTNAME], df.to_dict('records')
      else:
         return [{'label':name, 'value':name} for name in DISTRICTNAME],df.to_dict('records')




def checkInternetHttplib(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False
    
    
   
@app.callback(
    
     
    # Output("SendmailDiv", "children"),
    Output("StatusAlert", "children"),
    Input("send_whapp","n_clicks"),
    Input('send_mail','n_clicks'),
    Input('table-dropdown-ntf', "derived_virtual_data"),
    State('mail_message', 'value'),
    State('table-dropdown-ntf', "derived_virtual_selected_rows"),
    State('table-dropdown-ntf','data'),
    
)
def update_output_DistrictWiseData(send_Wh,click_send,rows,message,selected_rows,table_data):
    # print("Rows while",rows)
    ctx = dash.callback_context.triggered[0]
    ctx_caller = ctx['prop_id']
  
    selectedmailIds=[]
    # selectednames=[]
    # status=False
    layout=""
    status=checkInternetHttplib()
    ctx_caller == 'select-all-button.n_clicks'
    if   ctx_caller == 'send_mail.n_clicks':
          if selected_rows is not None :
              for row in selected_rows:
   
               col = 'emailid'
               colN='name'
               # selectednames.append(table_data[row][colN])
               selectedmailIds.append(rows[row][col])
 
          # return selectedmailIds
          
          if status:
                for mail in selectedmailIds:
                      if mail is not None:
                         GenerateMail(mail,message)
                         layout= dbc.Alert("SuccessFully Sent!", color="success",  is_open=True
                    ,dismissable=True,)
          else:   
                  layout= dbc.Alert("Internet Connection is Unavailable", color="danger",  is_open=True,
                              dismissable=True,)
   
        
       
    if ctx_caller == 'send_whapp.n_clicks':
        from pywhatkit.core import core
        selectedNumbers=[]
        if selected_rows is not None :
            for row in selected_rows:
 
             col = 'contactno'
             
             # selectednames.append(table_data[row][colN])
             selectedNumbers.append(rows[row][col])

        # return selectedmailIds
        
        if status:
            
              for Number in selectedNumbers:
                    if Number is not None:
                       # print(Number)
                       #GenerateMail(mail,message)
              
                    
                       now = datetime.now()
                    
                       #pywhatkit.sendwhatmsg("+91"+str(Number), message, now.hour,now.minute+1)
                     
                       
                       core.send_message(message=message, receiver="+91"+str(Number), wait_time=10)
                       core.close_tab(wait_time=20)
                                         
                                         
                       
                       layout= dbc.Alert("SuccessFully Sent!", color="success",  is_open=True,
                       dismissable=True,)
        else:   
                layout= dbc.Alert("Internet Connection is Unavailable", color="danger",  is_open=True,
                            dismissable=True,)
        

   
    return layout   

   





@app.callback(
    Output("WAgroupDiv", "children"), 
    [Input("send_whGroup", "n_clicks")]
)
def Whatsapp_grp_layout(whatsappgroup):
    if whatsappgroup >0:
        return Notifications_Layout
        


@app.callback(
    Output("Notifications-card-content", "children"), 
    [Input("Notifications-card-tabs", "active_tab")]
)
def Repair_Page_tab_content(active_tab):
    if active_tab == "e-mailN":
       return WhatsappGrpLayout
    elif active_tab == "sms-N":
       return ExistingWhatsappGroupLayout
    # elif active_tab == "NotCompleted":
    #    return HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE_NOTCOMPLETE
    
    # elif active_tab == "Completed":
    #     return HTML_SUMMARY_ITEM_COMPLETED_PAGE
    
    # elif active_tab == "Overall":
    #     return HTML_SUMMARY_ITEM_OVERALL_PAGE
   
    # elif active_tab == "Analysis":
    #     return HTML_SUMMARY_ITEM_ANALYSIS_PAGE   
   
    
    return html.Div("This shouldn't ever be displayed...")




@app.callback(
    Output("table-group-all", "data"), 
    [Input("Notifications-card-tabs", "active_tab")]
)
def UpdateTabsData(active_tab):
    if active_tab == "e-mailN":
       return Read_DataBase("MEMBERS_WHATSAPP_GROUP").to_dict('records') 
    elif active_tab == "sms-N":
       return Read_DataBase("MEMBERS_WHATSAPP_GROUP").to_dict('records') 
    # elif active_tab == "UploadFile":
    #     return UploadFile.layout
    
    # elif active_tab == "Completed":
    #     return HTML_SUMMARY_ITEM_COMPLETED_PAGE
    
    # elif active_tab == "Overall":
    #     return HTML_SUMMARY_ITEM_OVERALL_PAGE
   
    # elif active_tab == "Analysis":
    #     return HTML_SUMMARY_ITEM_ANALYSIS_PAGE   
   
    
    return html.Div("This shouldn't ever be displayed...")



@app.callback(
    [Output('GROUP_Info_USER', 'children'),
    Output('table-group', 'data')],
    
   
    [Input('create_What_Group', 'n_clicks'),
     
     
     ],
    
    
      
      State('GROUPNAME','value'),
      State('GROUPID','value'),


   
 )



def UpdateData_WhatGroup(n_clicksData,GROUPNAME,GROUPID):
    
 import os
 path='./CSV/GroupName.csv'
     
     
 if os.path.exists(path):
         
       try:
                 dfFile = pd.read_csv(path)
              
             
       except :
                 dfFile = pd.DataFrame()
 
 if n_clicksData>0:
     

    
     path='./CSV/GroupName.csv'
     
     
     if os.path.exists(path):
         
        
             
             if GROUPNAME is None:
                 return("GROUPNAME is blank!"),dfFile.to_dict('records')
                 
                 
             if GROUPID is None or len(GROUPID)<3: 
                 
                 return("GROUPID is blank!"),dfFile.to_dict('records')
             
             
             data = {'key':[GROUPNAME+"_"+GROUPID], 'name': [GROUPNAME] ,'id': [GROUPID] }
             
             # print("Data Created before saving",data)
             df = pd.DataFrame(data=data)
             
             #print("Df",df)
             
             if len(dfFile)>0:
                
            
                 mask=df['key'].values in dfFile['key'].values
                 print("Mask",mask)
          
                 if  mask:
                     return("Group already Created"),dfFile.to_dict('records')
                       
                 else:
                 
                     df.to_csv("./CSV/GroupName.csv",mode='a', header=False, index=False)    
                     updateDateBaseNewlyGroup()
                    
                     return("Group Created"),Read_DataBase("MEMBERS_WHATSAPP_GROUP").to_dict('records')
           
                     
             
             else:
                 
                 df.to_csv("./CSV/GroupName.csv",mode='a', header=False, index=False)    
                 updateDateBaseNewlyGroup()
          
                 return("Group Created"),Read_DataBase("MEMBERS_WHATSAPP_GROUP").to_dict('records')  
       
    
     else:
        
        
            
            data = {'key':[""], 'name': [""] ,'id': [""]}
                            
            df = pd.DataFrame(data=data)
            df = df.iloc[1: , :]
            
        
            df.to_csv("./CSV/GroupName.csv",index=False)
            
            return("Group Not Created"),df.to_dict('records') 
                
     # print("Read dfFile",dfFile)   
 return dash.no_update,dfFile.to_dict('records') 


def updateDateBaseNewlyGroup():
    
    
            key='key'
            CSV_FILENAME="GroupName.csv"
            TABLE_NAME="MEMBERS_WHATSAPP_GROUP"
            createTableSchema='''(key VARCHAR(255) PRIMARY KEY,name VARCHAR(255),id VARCHAR(10000));'''
            CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)
            


            pathT='./CSV/GroupName.csv'
            dfHis= Read_DataBase("MEMBERS_WHATSAPP_GROUP")
            dfHis.to_csv(pathT,index=False)
        
