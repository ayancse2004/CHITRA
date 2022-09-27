#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:35:01 2022

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
import base64
import io
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


from dash import callback_context, no_update
from views.CumtompdfGenerator  import *


MessageLayout=html.Div([
    
    
 html.Br(),
 dbc.Col(
     
   dbc.InputGroup(
         [
             dbc.InputGroupText("Message"),
             dbc.Textarea(id="message",value=''),
         ],
         className="mb-3",
     ),
     
     ),
 
 dbc.Row(
     [
     dbc.Col(
         [
             dbc.Button(
                         "Send Mail", id="mail_send", className="fa fa-paper-plane", n_clicks=0,style={"margin-top":"0.5rem"},
                         ),
             
             
             ],xs=6,lg=1,xl=1,
         
        
         
         ),
dbc.Col([
    
    
    dbc.Button(
                "WhatsApp", id="whapp_send", className="fab fa-whatsapp", n_clicks=0,style={"margin-top":"0.5rem","background-color":'green'},

                ),
    
    ]),
    
   html.Div(id="SendStatus")
    
    
    ]
    

    )
 ])


layoutUploadFile=html.Div([
    
    
    
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ],style={"cursor":"pointer"}),
        style={
            # 'width': '',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'text-align': 'center',
            'margin': '10px',
            'color':'red',
        
        },
        # Allow multiple files to be uploaded
        multiple=False
        ),

    html.Div(id='output-file-upload',style={'overflow':"auto"}),
    
    # MessageLayout,
   

    ])





def checkInternetHttplib(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False

def parse_contents(contents, filename, date):
    global df#define data frame as global

    content_type, content_string = contents.split(',')

  
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename,style={"font-weight":"bold","text-align":"center","color":"#005e97","text-decoration":"underline"}),
        html.Hr(),
        html.H6(datetime.fromtimestamp(date)),
        dbc.Button("Select All", color="success", className="me-1",id="select-all"),
        dbc.Button("Deselect All", color="warning", className="me-1",id="deselect-all"),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
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
              

           
            # editable=True,
            # row_deletable=True,
            # row_selectable="multi",    
           
            # filter_action='native',
            
            
            # editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        # row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
            id="dynamic_table"
        ),
        MessageLayout,
        html.Hr(),
        
        
        # horizontal line

        # For debugging, display the raw contents provided by the web browser
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    ],)

  







@app.callback(Output('output-file-upload', 'children'),
          Input('upload-data', 'contents'),
          State('upload-data', 'filename'),
          State('upload-data', 'last_modified'))
def update_output(content, filename, date):
    if(content is not None):
      children=parse_contents(content, filename, date)
      print(type(df))#this will show data type as a pandas dataframe
      print(df)
      return children
    else:
        return no_update





@app.callback(
  
    Output("dynamic_table",'selected_rows'),
    
    Input('select-all', 'n_clicks'),
    Input('deselect-all', 'n_clicks'),
    
   
    State('dynamic_table','data'),
    State('dynamic_table', 'derived_virtual_data'),
     
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
        if ctx_caller == 'select-all.n_clicks':
            selected_ids = [row['key'] for row in filtered_rows]
            # print(selected_ids)
            
            return [i for i, row in enumerate(table_data) if row['key'] in selected_ids]
        if ctx_caller == 'deselect-all.n_clicks':
            return  []
        raise PreventUpdate
   else:
        raise PreventUpdate








def GenerateMessageMail(emailid,message):

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









# New Code to implement 
   
@app.callback(
    
     
    # Output("SendmailDiv", "children"),
   
    Output("SendStatus", "children"),
    Input("whapp_send","n_clicks"),
    Input('mail_send','n_clicks'),
    Input('dynamic_table', "derived_virtual_selected_rows"),
    
    Input('dynamic_table', "derived_virtual_data"),
    
    State('message', 'value'),
   
    State('dynamic_table','data')
)
def update_output_DistrictWiseDataFile(send_Wh,click_send,selected_rows,rows,message,table_data):
    ctx = dash.callback_context.triggered[0]
    ctx_caller = ctx['prop_id']
  
    # print(rows)
    # dff = df if rows is None else pd.DataFrame(rows)  
    # print("update_output_DistrictWiseDataFile",dff)
    
    selectedmailIds=[]
    # selectednames=[]
    # status=False
    
    for row in selected_rows:
        col = 'emailid'
        # print(rows[row][col])
    layout=""
    status=checkInternetHttplib()
    ctx_caller == 'select-all.n_clicks'
    if   ctx_caller == 'mail_send.n_clicks':
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
                         GenerateMessageMail(mail,message)
                         layout= dbc.Alert("SuccessFully Sent!", color="success",  is_open=True
                    ,dismissable=True,)
          else:   
                  layout= dbc.Alert("Internet Connection is Unavailable", color="danger",  is_open=True,
                              dismissable=True,)
   
        
       
    if ctx_caller == 'whapp_send.n_clicks':
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


