#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:05:54 2022

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

from dash import callback_context, no_update
import flask
from flask import session

from flask_login import logout_user, current_user
from views.CumtompdfGenerator  import *

DISPLAYPROP="none"


UploadFile=html.Div([
    
    
    
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

    html.Div(id='file_upload',style={'overflow':"auto"}),
    
    # MessageLayout,
   

    ])



CustomUpoadLayout=html.Div(
    [
     UploadFile,
     
     
     
     ]
    )

UpdateRecords=html.Div(
    [
     
     html.Div(id="editable_table")
     
     
     
     
     
     
     ]
    
    
    
    )





Mnglayout=html.Div(
 [
  html.Div("Member Details Management",style={"font-weight":"bold","text-align":"center","color":"blue","font-size":"3.0vmin"}),
  html.Marquee("NOTE: File headers must be the following and in the same order: [name gender	address	block pincode statename	 districtname assemblyname	contactno emailid]",style={"font-weight":"bold","background-color":"yellow","color":"red"}),

  dbc.Tabs(
      [
          dbc.Tab(label="Custom Upload", tab_id="tab-first",label_style={"color": "#000f08"}),
          dbc.Tab(label="Update The Records", tab_id="tab-second",label_style={"color": "#000f08"}),
          dbc.Tab(label="Delete the Records", tab_id="tab-third",label_style={"color": "#000f08"}),
      ],
      id="tabs",
      active_tab="tab-first",
   
      style={'color':'black',"background-color": "rgb(215, 225, 219)", 'fontWeight': 'bold',}
  ),
  html.Div(id="customcontent"),
  
  
  ]
    
    
    )






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

    columnsCustom=[]
    columnsCustom.append('status')
    #columnsCustom.append('ssid')
    for i in df.columns:
        columnsCustom.append(i)
    #columnsCustom.append('date')
    
    
    # print(df.columns)
    # print(columnsCustom)
    df.insert(0, 'status',"Newly")
    return html.Div([
        html.H5(filename,style={"font-weight":"bold","text-align":"center","color":"#005e97","text-decoration":"underline"}),
        html.Hr(),
        html.H6(datetime.fromtimestamp(date)),
        # dbc.Button("Select All", color="success", className="me-1",id="select-all"),
        # dbc.Button("Deselect All", color="warning", className="me-1",id="deselect-all"),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in columnsCustom],
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
            
            # style_data_conditional={},
            css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
            
            
              style_data_conditional=[
                     {
                         'if': {
                             'filter_query': '{{status}} = {}'.format(0),
                         },
                         'backgroundColor': '#FF4136',
                         'color': 'white'
                     },
                    
                     {
                         'if': {
                             'filter_query': '{{status}} = {}'.format(1),
                         },
                         'backgroundColor': 'green',
                         'color': 'white'
                     },
                 ],


#         style_data_conditional=[
#     {
#         'if': {
#             'filter_query': '{status} <= 0',
#             'column_id': 'status'
#         },
#         'backgroundColor': '#B10DC9',
#         'color': 'white'
#     },
    
#     {
#         'if': {
#             'filter_query': '{status} >= 1',
#             'column_id': 'status'
#         },
#         'backgroundColor': 'green',
#         'color': 'white'
#     }
# ],


      
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        # row_selectable="multi",
        # row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
            id="custom_table"
        ),
        # MessageLayout,
        html.Hr(),
        
        html.Button("Update",id="update_database",n_clicks=0,className='btn btn-primary btn-lg'),
        html.Div(id="updateDiv")
        
    
    ],)









@app.callback(Output('file_upload', 'children'),
          Input('upload-data', 'contents'),
          State('upload-data', 'filename'),
          State('upload-data', 'last_modified'),
          )
def update_output(content, filename, date):
    if(content is not None):
      children=parse_contents(content, filename, date)
      print(type(df))#this will show data type as a pandas dataframe
      # print(df)
      return children
    else:
        return no_update







@app.callback(Output("customcontent", "children"), [Input("tabs", "active_tab")])
def switchTabs(at):
    if at == "tab-first":
        return CustomUpoadLayout
    elif at == "tab-second":
        return "UpdateRecord"
    elif at == "tab-third":
        return "DeleteRecords"
    return html.P("This shouldn't ever be displayed...")


      
    SpinnerComp=html.Div([
        
        
        dbc.Spinner(id="spinner",color='primary',)
        ],id="spinner_div",style={"display":DISPLAYPROP}) 



@app.callback(Output("updateDiv", "children"), 
               Output("custom_table","data"),
              
              [Input("update_database", "n_clicks"),
               # Input("style_data_conditional","style")
               
               
               ],
              State('custom_table', "derived_virtual_data"),
              State('custom_table', "data"),
              )
def updateDatabase(n_clicks,rows,tabledata):
    
    # dfreturn=pd.DataFrame.from_dict(rows)
    df=pd.DataFrame()
    dfFile = pd.DataFrame()
    dfMain=pd.DataFrame.from_dict(rows)
    
    dfReturn=pd.DataFrame.from_dict(tabledata)
    #print("dfReturn",dfReturn)
    
    columnsCustom=[]
    columnsCustom.append('key')
    columnsCustom.append('ssid')
    for i in dfMain.columns:
        columnsCustom.append(i)
    columnsCustom.append('date')
    
    if n_clicks >0:
        
        import os
        import random 
        
        path='./CSV/NewMembersList.csv'
        

    
        
        for row,i in zip(rows,  range(0,len(rows))    ):
            if os.path.exists(path):
                
                    try:
                        dfFile = pd.read_csv(path)
                        #print("Read dfFile",dfFile)
                    
                    except :
                        dfFile = pd.DataFrame()
            random_number = random.randint(10000000000, 999999999999)
    
            SSID="ADS"+"_"+str(random_number)
          
            now = datetime.now()
            # print("Now Time",now)
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                
            # print("dt_string",dt_string)
            
            data = {'key':row['statename']+"_"+ str(row['contactno']), 'name': row['name'],'gender': row['gender'] ,'address': row['address'],'block': row['block'] ,'pincode': row['pincode'] 
                        
                        ,'statename': row['statename'] ,'districtname': row['districtname'] ,'assemblyname': row['assemblyname'],'contactno':row['contactno'],'emailid':row['emailid'],'date':[dt_string],'ssid':[SSID]
                        
                        }
            

            
            
            #print("Data Created before saving",dfMain)
            
            
            df = pd.DataFrame(data=data)
            #print(df)
            
            #print("Df",df)
            
            if len(dfFile)>0:
               
                df['contactno'] = df['contactno'].astype('int64')
                #print("  df['contactno'] ",  df['contactno'] )
                dfFile['contactno'] = dfFile['contactno'].astype('int64')
                
                #print(" dfFile['contactno'] ", dfFile['contactno'] )
                mask=df['contactno'].values in dfFile['contactno'].values
                #print("Mask",mask)
                
                SSIDFILE=dfFile[dfFile['contactno']== row['contactno']]
                #print(SSIDFILE)
                
                SSIDFILE=dfFile[dfFile['contactno']== row['contactno']]
            
                #print("SSIDFILE 9",SSIDFILE['ssid'])
                
                if len(SSIDFILE)>0:
                    print(SSIDFILE['ssid'].values)
                    
         
                if  mask:
                    print(i)  
                    if 'key' not in dfMain.columns:
                            dfMain.insert(0, 'key',"Already Registered")
                            dfReturn.at[i,'status']=0
                          
                    else:
                        dfMain.at[i,'key']="Already Registered!"
                        dfReturn.at[i,'status']=0
                    
                    
                       
                        
                    if 'ssid' not in dfMain.columns:
                       # print(dfMain.columns,i) 
                        dfMain.insert(1, 'ssid',SSIDFILE['ssid'][:1])
                        dfMain.at[i,'ssid']=SSIDFILE['ssid'][:1]
                       # print(dfMain['ssid'],SSIDFILE['ssid'].values) 
                    else:
                         #print(dfMain.columns,i) 
                         dfMain.at[i,'ssid']=SSIDFILE['ssid'][:1]
                        # print(dfMain.columns,i) 
                        
                    if 'date' not in dfMain.columns:
                            dfMain.insert(12, 'date',SSIDFILE['date'][:1])
                            dfMain.at[i,'date']=SSIDFILE['date'][:1] 
                    else:
                            dfMain.at[i,'date']=SSIDFILE['date'][:1]   
                            
                             
                            # dfreturn['upload status']=dfMain['key']
                   
                    print("Already Exist")
                    #print("new Code by Ria",dfReturn)
                    
                    
                    pass
                      
                else:
                    if 'key' not in dfMain.columns:
                            dfMain.insert(0, 'key', row['statename']+"_"+ str(row['contactno']))
                            
                            dfReturn.at[i,'status']=1
                    else:
                        dfMain.at[i,'key']=row['statename']+"_"+ str(row['contactno'])
                        dfReturn.at[i,'status']=1
                        
                        
                    if 'ssid' not in dfMain.columns:
                               dfMain.insert(1, 'ssid',SSID)
                               dfMain.at[i,'ssid']=SSID 
                    else:
                           dfMain.at[i,'ssid']=SSID    
                           
                    if 'date' not in dfMain.columns:
                        dfMain.insert(12, 'date',dt_string)
                        dfMain.at[i,'date']=dt_string 
                    else:
                          dfMain.at[i,'date']=dt_string   
                                  
                
                    df.to_csv("./CSV/NewMembersList.csv",mode='a', header=False, index=False)    
                    updateDateBaseNewlyAddedMemeberCustom()
                    
                
                    
                    
                    
                    
                
                    
                    #if len(EmailID)>5:
                        #GenerateMessage(EmailID,SSID)   
                    # return modaloutput
                    #return"User Registered with following Number is {}  user Party Number is {} and Details is sent to Your mail if any ".format(MobileNo,SSID),modaloutput("User Registered with following Number is {}  user Party Number is {} and Details is sent to Your mail if any ".format(MobileNo,SSID))
          
                    
            
            # else:
                
            #     df.to_csv("./CSV/NewMembersList.csv",mode='a', header=False, index=False)    
            #     updateDateBaseNewlyAddedMemeber()
         
            #     return("User Registered with following Number is {} and user Party Number is {} ".format(MobileNo,SSID)),modaloutput("User Registered with following Number is {} and user Party Number is {} ")  
      
       
       
       
      

    return html.Div([ 
 
     
       # style={"text-align":"center","margin-top":"0.5rem","margin-bottom":"0.5rem","margin-right":"1.5rem"})
       
           # html.A("download",id="customelink"),
          
           
            html.Hr(),
            html.H5("Your Updated Record Status Table",style={"font-weight":"bold","text-align":"center","color":"#005e97","text-decoration":"underline"}),
            SpinnerComp,
                    
            html.Button("Send Ack to members",id="update_Membership",n_clicks=0,className='btn btn-primary btn-lg'),
            html.Div(id="updateDivMembers"),
       
            html.Hr(),
            dash_table.DataTable(
         id="newtable",
         export_format="csv",
         data=dfMain.to_dict('records'),
         columns=[{'name': i, 'id': i} for i in ["key",'ssid','name','gender','address','block','pincode','statename','districtname','assemblyname','contactno','emailid','date']],
       
         )]),dfReturn.to_dict('records')
 
    







    
@app.callback(
    
    
              Output("updateDivMembers", "children"),
              Output("spinner_div", "style"),
              
          
              Input("update_Membership", "n_clicks"),
              Input('newtable', "data"),
    
              
              )
def CustomEmailtoMembers(n_clicks,data):
    
    style={"display":"flex"}
   
    if n_clicks:
        
        dfall=pd.DataFrame().from_dict(data)
        # dfall.replace("None","Nodata")
        
        
        for i in range(0,len(dfall)):
         
            if (dfall['ssid'].loc[i]) is not None:
                
                print(dfall[i:i+1]['ssid'],i)
                
                CustompdfGeneratorpdfAd(dfall[i:i+1])
                
                print((dfall[i:i+1]))
        
        style={"display":"none"}
        return "Updated and Sent !!!!",style       
    return "",style  
# @app.server.route('/customdownload')
# def download_Custom_excel():
    
    

       
     

         
#         value=flask.request.args.get('value')
  
#         str_io=io.StringIO()
#         str_io.write(value)
#         mem=io.BytesIO()
#         mem.write(str_io.getvalue().encode('utf-8'))
#         mem.seek(0)
#         str_io.close()
#         #print(mem)


    
#         return flask.send_file(mem,
                          
#                             attachment_filename='ApnaDalMembersListCustom.xlsx',
#                             cache_timeout=1000,
#                             as_attachment=True)    
    



def updateDateBaseNewlyAddedMemeberCustom():
    
            print("updateDateBaseNewlyAddedMemeber")
            key='key'
            CSV_FILENAME="NewMembersList.csv"
            TABLE_NAME="MEMBERS_USERS_MANAGEMENT"
            createTableSchema='''(key VARCHAR(255) PRIMARY KEY,name VARCHAR(255),gender VARCHAR(255),address VARCHAR(1000),block VARCHAR(255),
                 pincode VARCHAR(255),statename VARCHAR(255),districtname VARCHAR(255),
                 assemblyname VARCHAR(255),contactno VARCHAR(255),emailid VARCHAR(500),date VARCHAR(255),ssid VARCHAR(10000));'''
            CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)
            
            print("updateDateBaseNewlyAddedMemeber2")

            pathT='./CSV/NewMembersList.csv'
            dfHis= Read_DataBase("MEMBERS_USERS_MANAGEMENT")
            dfHis.to_csv(pathT,index=False)
