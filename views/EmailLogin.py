#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:38:39 2022

@author: pdm
"""

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import psycopg2
import dash_table as dt
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
import io
import base64
import datetime
import numpy as np
from flask_login import logout_user, current_user
import os
import math
import random
import smtplib
import flask
from flask import session
from app import app

try:
    import httplib
except:
    import http.client as httplib


StyleLabel={"textAlign": "left","fontWeight":"bold","color":"#2b0593","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.8rem'}
StyleInput1={"textAlign": "left","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.5rem',"margin-right":'0.4rem'}

E_mailId=["officeapnadals@gmail.com","indiaapnadals@gmail.com",'ajay.cse2004@gmail.com']

OtpLayout=html.Div([
      dbc.Row(
          [  
               
                          dbc.Alert(
                            "OTP send Successfully to Your E-Mail(ओटीपी सफलतापूर्वक आपके ई-मेल पर भेजा गया ) ",
                            id="alert-no-fade",
                            dismissable=True,
                            fade=True,
                            is_open=True,
                            duration=4000,
                                  ),
                          
                          
                          
            
                        
              
               dbc.Row([
                   
                  dbc.Col(
                                  dbc.Label("Enter Your OTP(अपना ओटीपी दर्ज करें)", html_for="dropdown",style=StyleLabel), xs=12,sm=12,md=12,lg=12,xl=12,style={"text-align":"left"}
                     ),
                  dbc.Col(
                     
                                  dbc.Input(id="ENTEROTP",placeholder="Enter Your OTP...", type="text",value="",style=StyleInput1),xs=12,sm=12,md=12,lg=12,xl=12
                      ),
                 
                   
                   
                   ]),
               
               
               
               # html.Div([
                   

                   
               #     ],id='validStatus1',style={"margin-top":"3rem"}),
               
               
               
               
               # html.Div(id='1')
              
              ],style={"margin-top":"3rem"})
    
    ])


ErrorOTPLayout=html.Div([
    dbc.Row(
        [
            dbc.Alert(
                "Please Check Your Internet Connection(कृपया अपना इंटरनेट कनेक्शन जांचें)!!",
                id="alert-no-fade",
                dismissable=True,
                fade=False,
               is_open=True,
               color="danger",
            ),
            
            ]
        )
    
    ],style={"margin-top":"10px"})





emailLayout=html.Div([
        
        
        dbc.Row([
            dbc.Col(
                     dbc.Label("Enter Your Email-Id(अपना ईमेल-आईडी दर्ज करें)", html_for="dropdown",style=StyleLabel), md=12,xs=12,sm=12,lg=12,xl=12,style={"text-align":"left"}
               ),
            dbc.Col(
               
                [
                    
                   dcc.Dropdown(id="EmailID",placeholder="Select Your E-Mail ID", clearable=False,options=[{'label':name, 'value':name} for name in E_mailId],
                          
                          style=StyleInput1),
                 
                 dbc.FormFeedback("OTP will go to email address :-)", type="valid", style=StyleLabel,),
                 dbc.FormFeedback(
                     "Sorry, we only accept valid email id..",
                     type="invalid", style=StyleLabel,
                        ),
                 
                 
                 ]
                
                ,md=12,xs=12,sm=12,lg=12,xl=12
                ),
            
            ]),
        
    dbc.Row([
        dbc.Col(
                 dbc.Label("Enter Your Mobile Number(अपना मोबाइल नंबर दर्ज करें)", html_for="dropdown",style=StyleLabel),xs=12,sm=12,md=12,lg=12,xl=12,style={"text-align":"left"}
           ),
        dbc.Col([
            dbc.Input(id="MobileNo",placeholder=" Your Mobile Number..", type="text",
                      
                      style=StyleInput1),
            dbc.FormFeedback("phone number :-)", type="valid", style=StyleLabel,),
            dbc.FormFeedback(
                 "Sorry, we only accept valid phone number ",
                 type="invalid", style=StyleLabel,
                    ),
            
            
            ],
         xs=12,sm=12,md=12,lg=12,xl=12,
         
            ),
    
        
        ]),
    
    
        dbc.Row(
            
            dbc.Col([
               
                dbc.Button("Get OTP in Email(ईमेल में ओटीपी प्राप्त करें)", size="sm", className="me-1",id='sendOtp',
                           n_clicks=0,style={"text-align":"center","margin-top":"2rem","background-color":"green"}),
                
   
          
            
               ] ,  md=12,xs=12,sm=12,style={"text-align":"center"}
                ),
               
                
                  
           
            ),
        
        html.Div(id="Status"),
        html.Div(id="StatusValid"),
        
        
        # html.Div(id="notification",style={'display':'none'}),
        # html.Div(id="email_modal-ntf"),
        
      
        
        html.Div(id="EmailOtpcontainer",style={"display":"none"}),
        
    

        
        ],id="emailvalidation")
    


proceedCard = dbc.Card(
    [
        dbc.CardImg(src="/assets/proceed1.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("You are Succesfully Logged In", className="card-title"),
                html.P(
                      'Welcome to APNA-DALS official website',
                    className="card-text",
                ),
                dbc.Button("Proceed", color="primary",active=True, href="/details2",  external_link=True),
            ]
        ),
    ],
    style={"text-align":"center"},
)

layoutDirect = html.Div([
    
    
       dbc.Container([
        # html.Hr(),
        # cards,
        
        proceedCard,
        # dbc.Col(dbc.NavLink("Proceed", active=True, href="/details2",  external_link=True)),
        
        # html.Hr(),
           
           
           
           ],id='notification',style={'display':'none',"text-align":"center",
    "margin-bottom": "10rem",
    "margin-top": "10rem",
   " margin-left": "1rem",
    "margin-right": "5rem"}) ,
       # ,"margin-left":"3.5vmin","margin-right":"3.5vmin","margin-top":"3.5vmin","margin-bottom":"3.5vmin"
       
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







    
# validationLayout=html.Div(id="StatusValidOverAll")


                
             
@app.callback(
    Output("Status", "children"),
    # Output("OtpLayout1", "children"),
    Output('EmailOtpcontainer','children'),

    Input("sendOtp", "n_clicks"),
    State('EmailID','value'),
    State('MobileNo','value'),
    
)

def handleEmailLogin(sendOTP,emailid,mobileno):
    

   if (mobileno is None or emailid is None) and sendOTP>0 :
            
           
       return "Please Enter  above  Details(कृपया उपरोक्त विवरण दर्ज करें) ",""
   else:
           
           layout1=""
           layout2=""  
           otp=""

           # layout1=forgotIdLayout
               
         
           if sendOTP>0:
                
       
               if isMobileValidHere(mobileno) and len(mobileno)==10:
                   
                       print('ok mobile')
                   
               else:
                       layout2="Mobile Entery is not Ok(मोबाइल ठीक नहीं है) "
                       return layout2,""  
               if emailid.endswith(".com"):
                       print('ok emailid')           
               else:
                     layout2="Email Entery is not Ok(ईमेल ठीक नहीं है)"
                     return layout2,""
                 
               internetstatus=checkInternetHttplib()
               if(internetstatus):
                  layout2=OtpLayout
                  otp=GenerateOTP(emailid)
               else:
                  layout2=ErrorOTPLayout
                
           return layout2,otp
  


import re
  
def isMobileValidHere(s):
      
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("[6-9][0-9]{9}")
    return Pattern.match(s)
  



@app.callback(
    [Output("MobileNo", "valid"), 
     Output("MobileNo", "invalid")],
    [Input("MobileNo", "value")],
)
def check_validityMobile(text):
    if text :
       
        if isMobileValidHere(text) and len(text)==10:
            is_gmail=True
         
        else:
            is_gmail=False
     
        return is_gmail, not is_gmail
    return False, False


@app.callback(
    [Output("EmailID", "valid"), Output("EmailID", "invalid")],
    [Input("EmailID", "value")],
)
def check_validity(text):
    if text:
        is_gmail = text.endswith(".com")
        return is_gmail, not is_gmail
    return False, False


def GenerateOTP(emailid):
         digits = "0123456789"
         OTP = ""
         for i in range (6):
             OTP += digits[math.floor(random.random()*10)]
              
         otp = OTP + " is your OTP"
         message = otp
             
             
         SUBJECT = "Apna Dal-S"

         TEXT = "This message was sent by Apna Dal-S  Team \n "+ message
             
         message1 = 'From: Apna Dal-S\nSubject: {}\n\n{}'.format(SUBJECT, TEXT)
             
         s = smtplib.SMTP('smtp.gmail.com', 587)
         s.starttls()

         s.login("ajay.cse2004@gmail.com", "whgnysbsgusdexjw")
         s.sendmail('&&&&&',emailid,message1)
             
         return OTP

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
   
    Output('StatusValid', 'children'),
    Output('notification','style'),            # it is from notificationcontolr.py control ID

    
    Output("email_modal-ntf", "is_open"),
 
    Input("ENTEROTP",'value'),
    # State('Otpcontainer','children'),
    State('EmailOtpcontainer','children'),


    prevent_initiall_call=True
)

def renderOtpLayout(oTPentered,OTP):


   print(oTPentered,OTP) 
   print("session.get",session.get("login"))
   
   
   if len(oTPentered)==6:
           if oTPentered == str(OTP):
                  print("Success")
       
                  session["login"] = 1
                  print(session["login"])
             
                  # current_user.is_authenticated=True
            
                  return [
                      
                      
                      dbc.Row([
                          
                            dbc.Col(  dbc.Alert(
                                 "OTP is Verified and You are Logged in Successfully(ओटीपी सत्यापित है)",
                                 id="alert-no-fade",
                                 dismissable=True,
                                 fade=True,
                                 is_open=True,
                              
                                 
                             )),
                          
                         
                            
                            #dbc.Col(dbc.NavLink("Proceed", active=True, href="/details2",  external_link=True))
                          
                          
                          ])
                              

                        
                    ],{'display':'block',"text-align":"center",
             },False
                          
 
            
                
           else:
           
              session["login"] = 0
              return [
                  dbc.Alert(
                           "Entered OTP is Wrong,Please Try Again(दर्ज किया गया ओटीपी गलत है, कृपया पुनः प्रयास करें)",
                           id="alert-no-fade",
                           color="danger",
                           dismissable=True,
                           fade=True,
                           is_open=True,
                           
                       )
                  
                  
                  ],{'display':'none'},True 
   else:

     session["login"] = 0
     return[
         dbc.Alert(
                  "Enter Your 6-digit OTP which is sent to Your Mail-ID(अपना 6 अंकों का ओटीपी दर्ज करें जो आपकी मेल आईडी पर भेजा जाता है)",
                  id="alert-no-fade",
                  dismissable=True,
                  fade=True,
                  is_open=True,
                  color="info"
              )
         
         
         ] ,{'display':'none'},True   
       
        
        

      

