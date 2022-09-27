# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:31:58 2022

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
from flask import Flask
from views.UserMemberFormEntry import Com_dropdown_STATE,Com_dropdown_PERSONNAME,Com_dropdown_PERSON_ADDRESS_DETAILS
from views.UserMemberFormEntry import USER_FORM,ReadMembersListfromCSV
from dash import Input, Output, html, no_update
from views.page2 import Com_dropdown_problem,updateDateBaseLatest,updateDateBaseHistory



import os
import math
import random
import smtplib


try:
    import httplib
except:
    import http.client as httplib






TEXTMSG="Are You Registered Member? (क्या आप अपना दल-एस के सदस्य हैं?) "

StyleLabel={"textAlign": "left","fontWeight":"bold","color":"#2b0593","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.8rem'}
StyleInput1={"textAlign": "left","margin-left":'0.4rem','font-size':'1rem',"margin-top":'0.5rem'}
MEMBERSHIP_OPTIONS=html.Div([
    
        html.H4("Welcome to Reach US Form(संपर्क करने के लिए आपका स्वागत है)", 
                style={"textAlign": "center",
                       'color':'#fff','fontSize':'25px',
                       'padding-top':'2px',
                       'fontWeight':'bold',
                       "background-color":"rgb(0, 127, 128)",
    
                       "font-family":"Segoe UI Semibold"}),
        dbc.Row([
          
     dbc.Row([
         html.Hr(),
          
         dbc.Col(
         dbc.Label(TEXTMSG, 
                   style={"color":"green","font-weight":"bold","text-align":"left","margin-left":"8px"}),md=4,sm=8,xs=12,
         style={"text-align":"left"}),
         
          # dbc.Col(
       
          #   dcc.RadioItems(
          #             ['Yes', 'No'],
          #             'Yes',
          #             id='axis-type',
          #             style={"text-align":"left",'margin-right':'2rem','padding':'2px 2px',"margin-left":"8px"},
                     
          #             inline=True
          #         ),md=8,
          #   style={"text-align":"left"}
          #   ),
          
          
          dbc.Col(
              
            
    [
        dbc.RadioItems(
            id='axis-type',
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 2},
               
            ],
            value=1,
        ),
       
    ],
    className="radio-group",
  

             style={"text-align":"left"} ,
              
              md=8,
              
              ),
          
         
         ],style={"text-align":"center","font-weight":"bold",}),
        
     
     
     ]),
        
        html.Hr(),
    
    
        html.Div(id='yesoutput'),
        html.Div(id='AfterSubmit',style={"color":"green","text-align":"center","font-weight":"bold"}),
        html.Div(id="SubmitStatus")
      
    
    ]),









# @app.callback(Output("output", "children"), [Input("axis-type", "value")])
# def display_value(value):
#     return f"Selected value: {value}"












       
layoutIfMember=html.Div(
    [
     
     # dbc.Row([
         
         
     
  dbc.Row([
      
    
     dbc.Row([
     
         
         dbc.Col(
                         dbc.Label("Enter Your Membership Number(अपनी सदस्यता संख्या दर्ज करें)", html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left",}
            ),
         dbc.Col(
            
                         dbc.Input(id="CAN_SSID",placeholder="Enter Your Membership Number...", type="text",value="",style=StyleInput1),md=4,sm=12,xs=12,style={"text-align":"left"}
             ),
        
        
        dbc.Col(
           
                    html.Label(
                                   "Forgot MemberId?(सदस्यता संख्या भूल गए ?)",id="forgotID",n_clicks=0,
                        ),md=3,sm=12,xs=12,
                    
                    
                  
                    
                    
            ),
     
          
        

        
         ],style={"text-align":"center","font-weight":"bold",}),
     dbc.Row([
     
         
         dbc.Col(
                         dbc.Label("Enter Your Mobile Number(अपना मोबाइल नंबर दर्ज करें)", html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left"}
            ),
         dbc.Col(
            
                         dbc.Input(id="CAN_MOBILE",placeholder="Enter Your Mobile Number...", type="text",value="",style=StyleInput1),md=4,sm=12,xs=12
             ),
          
        
         ],style={"text-align":"center","font-weight":"bold",}),
     
     
  
   
     
      html.Hr(),  
     
      html.Div(id='matchout',style={"text-align":'center'}),
      html.Div(id='tempvaluessid',style={"text-align":'center',"font-weight":"bold","color":"red"}),
      
      html.Div(id='btnCloseValue',style={"text-align":'left',"font-weight":"bold","color":"green"}),
      
    
     
      
      html.Hr(),
      
     
      # html.Button("Raise Your Matter",id='btninfossid',n_clicks=0),
         
         
         ]) ,
    # dbc.Button("Raise Your Matter", size="sm", className="me-1",id='btninfossid',n_clicks=0,style={"text-align":"center"}),
  # ]),
     
     
    
     
     ],
    
    
    )

# This Alert will show when Internet Connection is not Active
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


# This Alert will show when Internet Connection is Active and All the fields are Validated

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
                                  dbc.Label("Enter Your OTP(अपना ओटीपी दर्ज करें)", html_for="dropdown",style=StyleLabel), xs=12,sm=12,md=12,style={"text-align":"left"}
                     ),
                  dbc.Col(
                     
                                  dbc.Input(id="ENTER_OTP",placeholder="Enter Your OTP...", type="text",value="",style=StyleInput1),xs=12,sm=12,md=12,
                      ),
                 
                   
                   
                   ]),
               
               
               
               html.Div([
                   

                   
                   ],id='validStatus',style={"margin-top":"3rem"}),
               
               
               
               
               # html.Div(id='validStatus')
              
              ],style={"margin-top":"3rem"})
    
    ])








# This is rendered when the user clicked the forgot Id Link

forgotIdLayout=html.Div(
    [
       
     dbc.Row([
         
         dbc.Row([
             dbc.Col(
                      dbc.Label("Retrieve Your Membership Number(सदस्यता संख्या प्राप्त करें)", html_for="dropdown",style={'text-align':'center','color':'green','font-weight':'bold'}), md=12,xs=12,sm=12,
                ),
           
             
             ]),
         
         dbc.Row([
             dbc.Col(
                      dbc.Label("Enter Your Email-Id(अपना ईमेल-आईडी दर्ज करें)", html_for="dropdown",style=StyleLabel), md=12,xs=12,sm=12,style={"text-align":"left"}
                ),
             dbc.Col(
                
                 [dbc.Input(id="E_mailId",placeholder=" Your E-mailID..", type="text",
                           
                           style=StyleInput1),
                  
                  dbc.FormFeedback("email address :-)", type="valid", style=StyleLabel,),
                  dbc.FormFeedback(
                      "Sorry, we only accept valid email id..",
                      type="invalid", style=StyleLabel,
                         ),
                  
                  
                  ]
                 
                 ,md=12,xs=12,sm=12,
                 ),
             
             ]),
         dbc.Row([
             dbc.Col(
                      dbc.Label("Enter Your Mobile Number(अपना मोबाइल नंबर दर्ज करें)", html_for="dropdown",style=StyleLabel),xs=12,sm=12,md=12,style={"text-align":"left"}
                ),
             dbc.Col([
                 dbc.Input(id="Mobile_NO",placeholder=" Your Mobile Number..", type="text",
                           
                           style=StyleInput1),
                 dbc.FormFeedback("phone number :-)", type="valid", style=StyleLabel,),
                 dbc.FormFeedback(
                      "Sorry, we only accept valid phone number ",
                      type="invalid", style=StyleLabel,
                         ),
                 
                 
                 ],
              xs=12,sm=12,md=12,
              
                 ),
         
             
             ]),
         
         
         dbc.Row(
             
             dbc.Col([
                
                 dbc.Button("Get OTP(ओटीपी प्राप्त करें)", size="sm", className="me-1",id='btnsendOtp',
                            n_clicks=0,style={"text-align":"center","margin-top":"2rem","background-color":"green"}),
                 
           
                    
                            # dbc.Button("Close(बंद करें)",id="btnClose", n_clicks=0, size="sm", className="me-1",
                            #       style={"text-align":"center","margin-top":"2rem","background-color":"red"}),
                             
    
           
             
                ] ,  md=12,xs=12,sm=12,style={"text-align":"center"}
                 ),
                
                 
                   
            
             )
         
         
         
         
         ]),
     
     
     
     ],id='forgotIdLayout')


layout=MEMBERSHIP_OPTIONS



newForgotLayout=dbc.Modal(
            [
                dbc.ModalHeader(dbc.Row
                                
                                ([
                    
                                        dbc.Label("Recover Your Membership Number",
                                                  
                                                  
                                                style={"font-weight":"bold","color":"orange",
                                                       
                                                       "text-align":"center",
                                                       "font-size":"20px"
                                                       
                                                       }),
                                        
                                        
                                        dbc.Label("अपनी सदस्यता संख्या पुनर्प्राप्त करें",
                                                  style={"font-weight":"bold","color":"blue",
                                                         
                                                         "text-align":"center",
                                                         "font-size":"15px"
                                                         
                                                         },
                                                  
                                                  ),
                
                    
                                    ],
          
                                        ),style={"border":"2px solid green","text-align":"center"}
                                ),
                
                
                
                dbc.ModalBody(
                    
                    
                    [
                        forgotIdLayout,
                        html.Div(id='OtpLayout1',style={"text-align":'center',"font-weight":"bold","color":"red"}),
                     
                     
                     ]),
                
                dbc.ModalFooter(  
                    [
                    html.Div(id='Otpcontainer',style={"display":"none"}),
                    
                   
                    
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





@app.callback(
    Output("simple-toast", "is_open"),
    [Input("simple-toast-toggle", "n_clicks")],
)
def open_toast(n):
    if n == 0:
        return no_update
    return True


@app.callback(
    Output('yesoutput', 'children'),
    Input('axis-type', 'value'),
    )


def update_form(xaxis_type):
    
    
  
    
    if xaxis_type == 1:
       return layoutIfMember
           
    else:
        
        heading=dbc.Row([
            
          
            
                    html.Div(
                        [
                            dbc.Toast(
                                [
                               html.H3("Please Become Member Then Reach US By Using Your Membership(कृपया सदस्य बनें फिर अपनी सदस्यता का उपयोग करके हम तक पहुंचें)", className="mb-3",style={"color":"black","font-weight":"bold","font-size":"14px"}),
                
                
                
                            ],
                        id="simple-toast",
                        header="Be One Of Us(हम में से एक बनें) ",
                        icon="success",
                        dismissable=True,
                        is_open=True,
          
                        style={"position": "fixed", "top": 66, "right": 10, "width": 350, "background-color":"white","z-index":"55856885"},
                        ),
                    ]
                   ),
                       
                        #  dbc.Alert(
                        #     "Hello! I am an alert that doesn't fade in or out",
                        #     id="alert-no-fade",
                        #     dismissable=True,
                        #     fade=False,
                        #     is_open=True,
                        # ),
                        
                        html.Div( USER_FORM),
                        
                        ])
    
   
        
        return heading
        






@app.callback(
    
     
    Output('tempvaluessid', 'children'),
    Output('matchout', 'children'),
    Output('forgotID','n_clicks'),
    Output('forgotID','style'),
    

    Input('CAN_SSID','value')  ,  
    Input('CAN_MOBILE','value'), 
    Input('forgotID','n_clicks'),
 
    
 
    

    
    
)
def update_output_SUbDistrict(ssid,mobileno,forgotClicked):
    
    data=ReadMembersListfromCSV()
    fildata=data[data['ssid']==ssid]
    style={"text-align":"center",'display':'block',"background-color":"white","border":"none",
           "color":"blue","text-decoration":"underline","font-weight":"bold",'cursor':'grab','padding-top':'0.2rem'}
    styleDisable={"text-align":"center",'display':'none'}
    PROBLEM_LIST=["Appointment Related","Job-Related",'Land Related','Problem']
 

     
    if len(fildata)==1:
        if len(mobileno)==10:
            # print(fildata['contactno'])
            fildataM=fildata[fildata['contactno']==int(mobileno)]
           
       
            if len(fildataM)==1:
                
                MEMBERINFOOVERALL=dbc.Row([
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your State(आपका राज्य)", html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_STATE",placeholder=" Your state..", type="text",disabled =True,
                                      
                                      value=fildataM['statename'],style=StyleInput1),md=4,sm=12,xs=12,
                            ),
                        
                        ]),
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your District(आपका जिला)" , html_for="dropdown",style=StyleLabel), md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_DISTRICT",placeholder=" Your district..", type="text",disabled =True,
                                      
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
                                 dbc.Label("Your Gender(आपका लिंग )"  , html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                            dbc.Input(id="CAN_GENDER",placeholder=" Your Gender..", type="text",disabled =True,
                                      
                                      value=fildataM['gender'],style=StyleInput1),md=4,sm=12,xs=12
                            ),
                        
                        ]),
                 
                    
                    html.Hr(),    
                 
                    
                  dbc.Row(
                     [
                      dbc.Row([
                          dbc.Col(
                                          dbc.Label("Select Problem Description(समस्या विवरण का चयन करें)", html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,
                             ),
                          dbc.Col(
                                      dcc.Dropdown(
                                                  id="Com_problem_dropdown_ReachUS",
                                                  options=[{'label':name, 'value':name} for name in PROBLEM_LIST],
                                                  clearable=False,
                                                  style=StyleInput1,
                                                  ),md=4,sm=12,xs=12,
                             ),
                          
                          
                          ])
                        
                     ],className="mb-3",
                 ),
                    
                    
                    dbc.Row([
                        dbc.Col(
                                 dbc.Label("Your Problem(आपकी समस्या) " , html_for="dropdown",style=StyleLabel),md=4,sm=12,xs=12,style={"text-align":"left"}
                           ),
                        dbc.Col(
                           
                             
                                dbc.Textarea(id="ProblemDetails",
                                   invalid=False, size="lg", placeholder="A large, invalid Textarea",style=StyleInput1
                                ),md=4,sm=12,xs=12,),
                        
                        ]),
                    
                
                    
                    dbc.Row([
                        dbc.Col(
                            
                                dbc.Button("Raise Your Matter(अपनी बात उठाएं)", size="sm", className="me-1",id='btninfossid',n_clicks=0,style={"text-align":"center","margin-top":"2rem","background-color":"green"}),
                              md=12,
                                
                                ),
                    
                                             
                        
                        
                        ],style={"text-align":"center"}),
                    

                       ],style={"text-align":"left","font-weight":"bold",}),
                   
                return "Thanks for Choosing US(हमें चुनने के लिए धन्यवाद)" ,MEMBERINFOOVERALL,0,styleDisable
                # return dbc.Row("Thanks for Choosing US(हमें चुनने के लिए धन्यवाद)" ,id="AfterSubmit"),MEMBERINFOOVERALL,0,styleDisable
                
            else:
                if forgotClicked>0  :
                      
                     
                      return "Member Not Found with above details(उपरोक्त विवरण के साथ सदस्य नहीं मिला)", newForgotLayout,0,style
            
           
        
   
        return "Membership Found and please provide your Mobile no for further action(सदस्यता मिली और कृपया आगे की कार्रवाई के लिए अपना मोबाइल नंबर प्रदान करें)","",0,style

   

    
    elif forgotClicked>0  :
          
            return "",newForgotLayout,0,style
  
    
   
   
    else:
        
        return "Please enter your membership number(कृपया अपनी सदस्यता संख्या दर्ज करें)","",0,style
     
















import re
  
def isMobileValidHere(s):
      
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("[6-9][0-9]{9}")
    return Pattern.match(s)
  



@app.callback(
    [Output("Mobile_NO", "valid"), 
     Output("Mobile_NO", "invalid")],
    [Input("Mobile_NO", "value")],
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
    [Output("E_mailId", "valid"), Output("E_mailId", "invalid")],
    [Input("E_mailId", "value")],
)
def check_validity(text):
    if text:
        is_gmail = text.endswith(".com")
        return is_gmail, not is_gmail
    return False, False




# @app.callback(
#     Output("internet_status", "value"), 
#     # Input("E_mailId", "value"),
# )
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
    Output("forgotIdLayout", "children"),
    Output("OtpLayout1", "children"),
    Output('Otpcontainer','children'),
    #Input("btnClose", "n_clicks"),
    Input("btnsendOtp", "n_clicks"),
    State('E_mailId','value'),
    State('Mobile_NO','value'),
    
)


def handleForgotOtp(btnsendOtp,emailid,mobileno):

    



  if (mobileno is None or emailid is None) and btnsendOtp>0 :
       
      
       return forgotIdLayout,"Please Enter  above  Details(कृपया उपरोक्त विवरण दर्ज करें) ",""  
  else:
      
      layout1=""
      layout2=""  
      otp=""

      layout1=forgotIdLayout
          
    
      if btnsendOtp>0:
           
  
          if isMobileValidHere(mobileno) and len(mobileno)==10:
              
                  print('ok mobile')
              
          else:
                  layout2="Mobile Entery is not Ok(मोबाइल ठीक नहीं है) "
                  return  layout1 ,layout2,""    
          if emailid.endswith(".com"):
                  print('ok emailid')           
          else:
                layout2="Email Entery is not Ok(ईमेल ठीक नहीं है)"
                return  layout1 ,layout2,""
            
          internetstatus=checkInternetHttplib()
          if(internetstatus):
             layout2=OtpLayout
             otp=GenerateOTP(emailid)
          else:
             layout2=ErrorOTPLayout
           
      return dash.no_update,layout2,otp




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






@app.callback(
   
    Output('validStatus', 'children'),
    
    Input("ENTER_OTP",'value'),
    State('Otpcontainer','children'),
    State('Mobile_NO','value'),
    prevent_initiall_call=True
)

def renderOtpLayout(oTPentered,OTP,mobileno):

  
   print(oTPentered,OTP,mobileno) 
   if len(oTPentered)==6:
           if oTPentered == str(OTP):
               data=ReadMembersListfromCSV()
               dataM=data[data['contactno']==int(mobileno)]
          
               if len(dataM)==1:
                   # print(dataM)

                   return[
                    dbc.Col([
                        
                        dbc.Alert(
                                 "OTP is Verified(ओटीपी सत्यापित है)",
                                 id="alert-no-fade",
                                 dismissable=True,
                                 fade=True,
                                 is_open=True,
                              
                                 
                             ),
                        
                        
                           dbc.Alert(
                                 "Your Membership Number (आपकी सदस्यता संख्या)   " +(dataM['ssid']),
                                 id="alert-no-fade",
                                 dismissable=True,
                                 fade=True,
                                 is_open=True,
                                 
                                 
                             )
                        
                        ])
                   
                    
                    
                    ]  
               else:
                return [
                    dbc.Alert(
                             "Entered Mobile is not found in the Record(दर्ज किया गया मोबाइल रिकॉर्ड में नहीं मिला)",
                             id="alert-no-fade",
                             color="danger",
                             dismissable=True,
                             fade=True,
                             is_open=True,
                             
                         )
                    
                    
                    ]  
           
                
           else:
              return [
                  dbc.Alert(
                           "Entered OTP is Wrong,Please Try Again(दर्ज किया गया ओटीपी गलत है, कृपया पुनः प्रयास करें)",
                           id="alert-no-fade",
                           color="danger",
                           dismissable=True,
                           fade=True,
                           is_open=True,
                           
                       )
                  
                  
                  ]  
   else:
     return[
         dbc.Alert(
                  "Enter Your 6-digit OTP which is sent to Your Mail-ID(अपना 6 अंकों का ओटीपी दर्ज करें जो आपकी मेल आईडी पर भेजा जाता है)",
                  id="alert-no-fade",
                  dismissable=True,
                  fade=True,
                  is_open=True,
                  color="info"
              )
         
         
         ]  
       



@app.callback(
    Output("AfterSubmit", "children"), 
    Output("SubmitStatus", "children"),
    
    
  
    Input("btninfossid", "n_clicks"),
    
    
    
      State('CAN_DISTRICT','value'),
      State('CAN_NAME','value'),
   
    
      State('Com_problem_dropdown_ReachUS','value'),
      State('ProblemDetails','value'),

   
     
   
  )



def RegisterComplain(n_clicksData,PartNumberValue,PartSerialValue,ProblemList,ProblemDescriptionDetails):
             
  RepairEntryNewColumns=['key','partnumber','serialnumber','description','problemlist','problemdetails','assignto','taskstatus','complaintdate','attendeddate','closeddate'] 
  import os
  import numpy as np

 
  if n_clicksData>0:
    
      path='./CSV/RepairLifeCycleEntry.csv'
     
     
      if os.path.exists(path):
         
              try:
                  dfFile = pd.read_csv(path)
             
              except :
                  dfFile = pd.DataFrame()
                 
            

         
              if ProblemList is None:
                       
                        return dbc.Alert(
                             "Problem List is Blank!",
                             id="alert-no-fade",
                             dismissable=True,
                             fade=True,
                            is_open=True,
                            color="danger",
                            duration=4000,
                         ),html.Col()
                 
              
              if ProblemDescriptionDetails is None:
                       
                        return dbc.Alert(
                             "Problem Description is Blank!",
                             id="alert-no-fade",
                             dismissable=True,
                             fade=True,
                            is_open=True,
                            color="danger",
                            duration=4000,
                         ),html.Col()      
                   
           
         
              dfFileT = pd.DataFrame(index=np.arange(1),columns=np.arange(11))
              dfFileT.columns=RepairEntryNewColumns
              
              # print(dfFileT)
              
              # print(PartNumberValue[0])
              # print(PartSerialValue[0].strip())
             
              dfFileT['key']=PartNumberValue[0]+"-"+PartSerialValue[0].strip()
              
             
              mask=dfFile['key'].isin(list(dfFileT['key']))
              
              mask=np.sum(mask)
              #print(mask)
             
              if  mask>0:
                  return dbc.Alert(
                       "Complain Already done",
                       id="alert-no-fade",
                       dismissable=True,
                       fade=True,
                      is_open=True,
                      color="danger",
                      duration=4000,
                   ),modaloutputReachus("Complain Already done")
             

             
           
              else:
                  #RepairEntryNewColumns=['key','partnumber','serialnumber','partdescription','problemlist','problemdetails','assignto','Complaintdate','Attendeddate','Closeddate']
                  dfFileT['partnumber']=PartNumberValue
                  dfFileT['serialnumber']=PartSerialValue
                  dfFileT['description']=PartNumberValue
                 
               
                  dfFileT['problemlist']=ProblemList
                  dfFileT['problemdetails']=ProblemDescriptionDetails
                 
                  dfFileT['assignto']="IT-Cell"
                  dfFileT['taskstatus']="InProgress"
                 
                  start_date_object = datetime.today().strftime('%d-%m-%Y')
                 
            
                 
                  dfFileT['complaintdate']=start_date_object
                  dfFileT['attendeddate']=''
                  dfFileT['closeddate']=''
   
 

                  #print(dfFileT)
                  dfFileT.to_csv(path,mode='a', header=False, index=False)
                 
                  updateDateBaseLatest()
                 
                 
                  pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
                  key_column=dfFileT['key']+"_HIS_"+dfFileT.index.astype(str)
                  dfFileT.insert(0, 'key_id', key_column)
                  dfFileT.insert(8,'transferredto','')
                  dfFileT.to_csv(pathT,mode='a', header=False, index=False)
                  updateDateBaseHistory()
             
                  return dbc.Alert(
                     "Complain Created with Id "+(dfFileT['key']),
                     id="alert-no-fade",
                     dismissable=True,
                     fade=True,
                    is_open=True,
                    color="success",
                    duration=4000,
                 ),modaloutputReachus( "Complain Created with Id: "+(dfFileT['key']))
                 
             
      else:
          dfFileCreate = pd.DataFrame(columns=np.arange(11))
         
          dfFileCreate.columns=RepairEntryNewColumns
          #dfFileCreate.rename(columns = RepairEntryNewColumns, inplace = True)
         
          dfFileCreate.to_csv(path,index=False)
          updateDateBaseLatest()
         
         
          dfFileCreate.insert(0,'key_id','')
          dfFileCreate.insert(8,'transferredto','')
         
          pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
         
          dfFileCreate.to_csv(pathT,index=False)
          updateDateBaseHistory()
         
          return("File Does Not Exist Now Created"),modaloutputReachus("File Does Not Exist Now Created")
         
  return "",""


        
def modaloutputReachus(message):
    modaloutput= html.Div(
        [
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Confirmation")),
                    dbc.ModalBody(message,style={"font-weight":"bold"}),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close1", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                id="modal2",
                is_open=True,
                backdrop="static",
                centered=True
            ),
        ]
    )
    return modaloutput
  
  

@app.callback(
    Output("modal2", "is_open"),
    [ Input("close1", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modalReachUS(n2, is_open):
    if n2:
        return not is_open
    return is_open


     
  
  
 
 
