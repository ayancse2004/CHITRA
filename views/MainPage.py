# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:52:03 2022

@author: BSTC 4
"""

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
from views.page2 import Com_dropdown_problem

import dash_trich_components as dtc

# from flask_login import logout_user, current_user

import os
import math
import random
import smtplib



 # current_user.is_authenticated
 # current_user.username



# User=format(current_user.username)



officalIframe =html.Iframe(src="https://www.apnadal.org/",
                style={"height": "1067px", "width": "100%"})





@app.callback(
    Output('Login_Status', 'children'),
    [Input('NavBAr', 'children')])
def ShowLoginContent(input1):
      if( current_user.is_authenticated):
            return   dbc.NavLink(current_user.username+"(Admin)",
                                 
                                 style={"color":"white","text-align":"left","text-decoration":"uppercase",},
                                 
                                 className="fa fa-user",href="/login",external_link=True)
           
      else:
          return   dbc.NavLink("Login",
                               style={"color":"white","text-align":"left"},
                               className="fa fa-user",href="/login",external_link=True)




custombtn=html.Div(
    [
  html.A( 
      
      html.I( className="facebookBtn smGlobalBtn",style={"margin-left":"3px"},), 
      
      href="https://www.facebook.com/ApnaDal.Official/"
      ),
  html.A(   html.I( className="twitterBtn smGlobalBtn",style={"margin-left":"3px"},),href="https://twitter.com/apnadalofficial"),
   html.A(  html.I( className="googleplusBtn smGlobalBtn",style={"margin-left":"3px"},),href="https://www.youtube.com/channel/UChsiArcNzKv9dDeV1S_zv-w"),
   
   html.Iframe("hi",src="https://www.youtube.com/channel/UChsiArcNzKv9dDeV1S_zv-w",
               style={"height": "1067px", "width": "100%"})
     
     ],style={"text-align":"center","margin":"5px"}
    )
    







Header= dbc.NavbarSimple(
    children=[
        # dbc.NavItem(dbc.NavLink("Page 1", href="#")),
      
        dbc.Container(
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='/assets/mainpage/logo.png', height="45px")),
                        # dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")
                                
                                
                                
                
                    ],
                    align="left",
                    className="g-0",
                ),
                href="/mainpage",
                style={"textDecoration": "none"},
           
         ),
           
           
            ),
     
           
        dbc.NavItem(dbc.Row(
            
            [
                         # dbc.Col(    html.I(className="fa fa-phone",style={"color":"white","text-align":"right","font-size":"20px"}),md=1,xs=1,sm=1),
                             
                         dbc.Col(     dbc.NavLink("+919454400742",style={"color":"white","text-align":"left"},className="fa fa-phone",href="#"),md=2,xs=2,sm=2),
                         
                #          html.I(className="far fa-list-alt"),
                # "An example info alert with an icon",
                
                             
            ]
            
            ),
            ),
            
            
            dbc.NavItem(dbc.Row(
                
                [
                             # dbc.Col(    html.I(className="fa fa-envelope",style={"color":"white","text-align":"right","font-size":"20px"}),md=1,xs=1,sm=1),
                                 
                             dbc.Col(     dbc.NavLink("officeapnadals@gmail.com  indiaapnadals@gmail.com",style={"color":"white","text-align":"left"},className="fa fa-envelope",href="#"),md=2,xs=2,sm=2),
                                 
                ]
                
                )
            
            ),
            
            dbc.NavItem( 
                
                
              id="Login_Status",
                
                
                
               
                
                ),
            
  
            
        
    ],
    
    
    id="NavBAr",
    brand="APNA DAL-S",
    brand_href="/mainpage",
    style={"font-weight":"bold"},
    color="#26176A",
    dark=True,
    links_left =False,
    fixed="top"

)
CONTENT_STYLE_FOOTER = {
    "bottom":"1.5rem",
    "position": "fixed",
    "margin-bottom": "0",
    "width":'100%',
    #"transition": "margin-left .5s",
    #"margin-left": "16.1rem",
    #"margin-right": "16.1rem",
    #"padding": "0.2rem 0.2rem",
    "background-color": "rgb(38, 23, 106)",
    "z-index":"499",
    
}



MainPageFooter=html.Div([
  
# html.Div(navigateTopLayout,style={"text-align":"right"}),   
html.Footer([
  
   
    # html.Div("",style={"textAlign": "center",'color':'white','font-weight':'bold'}, id='footer-text'),
    custombtn,
    
    
   

   
    ],style=CONTENT_STYLE_FOOTER),
  ])



ReachUS = dbc.Card(
    [
      
       
       dbc.Row([
           
           dbc.Col("",width=7),
           
           
           
           
           dbc.Col(   html.Img(src='/assets/mainpage/reachus1.jpg', width="100%",height="100%",),width=5,style={"height":"10rem"}
                   
            ),   
        
           
        
           
           ],style={"height":"10rem"}
          
           
           
           ),
       
       
     
       
       
        dbc.CardBody(
            [
                html.H5(" Join Apna dal-S (अपना दल-एस में शामिल हों)", className="card-title",style={"font-weight":"bold","color":"rgb(38, 23, 106)","font-size":"18px"}),
                html.Div(
                html.P(
                    '''
                    
                    Resolve to build a society whose citizens take pride in being a resident of India in the global world.
                    Where people of all caste, creed and sect have equal opportunity to develop freely and democratic institutions,
                    There should be participation and participation of all sections of the society without discrimination 
                    in administrative systems and tribunals etc., so that a humanistic, egalitarian and exploitation-free society can be established.
                    
                    (
                                       
                    एक ऐसे समाज निर्माण का संकल्प जिसके नागरिक वैश्विक दुनिया में भारतवासी होने का गर्व करे। 
                    जहां सभी जाति पंथ व संप्रदाय के लोगों को स्वतंत्र रूप से विकास के समान अवसर हो तथा लोकतांत्रिक संस्थाओं,
                    प्रशासनिक व्यवस्थाओं व न्यायाधिकरणों आदि स्थानों में भेदभाव रहित समाज के सभी वर्गो की हिस्सेदारी व भागीदारी हो जिससे मानवतावादी, समता-समरसता युक्त और शोषण मुक्त समाज की स्थापना हो.
                        
                        )
                    ''',
                    # "Some quick example text to build on the card title and "
                    # "make up the bulk of the card's content.",
                    className="card-text",
                ),style={"overflow":"auto","height":"10rem"}
                
                ),
                
                
                dbc.NavLink( dbc.Button("Reach US(हम तक पहुंचें) ", id="JOIN_US", 
                                        className="fa fa-arrow-right",
                                        
                                        color="primary",
                                
                                      
                                        
                                      ),
                           
                            
                            href="/reachform",
                            
                            style={"text-align":"left",},
                          ),
              # dbc.Button("Reach US(हम तक पहुंचें)", color="primary",href='/reachform',style={"position":"absolute"}),
            ],
        ),
    ],
    style={"width": "28rem","height":"27rem","border-bottom":"4px solid rgb(38, 23, 106)","border-radius":"10px"},
)



JoinUS = dbc.Card(
    [
     
     
     
     
       dbc.Row([
           
           dbc.Col("",width=7),
           
           
           
           
           dbc.Col(   html.Img(src='/assets/mainpage/join.jpg', width="100%",height="100%",),width=5,style={"height":"10rem"}
                   
            ),   
        
           
        
           
           ],style={"height":"10rem"}
          
           
           
           ),
   
       
       
        dbc.CardBody(
            [
                html.H5(" Join Apna dal-S (अपना दल-एस में शामिल हों)", className="card-title",style={"font-weight":"bold","color":"rgb(38, 23, 106)","font-size":"18px"}),
                dbc.Row(
                html.P(
                    '''
                    
                    The ocean of compassion flourished with the blessings of Lord Buddha,
                    flowered, dedicated to the national personality of Sardar Vallabhbhai Patel ji,
                    Bodhisattva, trying to give new impetus to the ideology of Mahamana Dr. Dedicated to Honorable Anupriya Patel ji,
                    the most respected, most respected MP and  Union Minister of State, 
                    who vocally raised the voice of the underprivileged on the floor of the Parliament
                    
                    (
                                       
                   करुणा के सागर भगवान बुद्ध के आशीर्वाद से पल्लवित, पुष्पित, सरदार वल्लभ भाई पटेल जी के राष्ट्रीय व्यक्तितत्व पर समर्पित, बोधिसत्व ,
                   महामना डॉक्टर सोनेलाल पटेल जी की विचारधारा को दिनों दिन नई गति देने के लिए प्रयासरत, पिछङो दलितों, किसान, कमेरो,
                   शोषितो, वंचितों की आवाज को संसद पटल पर मुखरता से उठाने वाली, परम सम्मानित, परम आदरणीय सांसद एवं केंद्रीय राज्य मंत्री माननीय अनुप्रिया पटेल जी को समर्पित | 
                        
                        )
                    '''
                    ,
                    # "Some quick example text to build on the card title and "
                    # "make up the bulk of the card's content.",
                    className="card-text",
                ),style={"overflow":"auto","height":"10rem"}
                
                ),
                dbc.NavLink( dbc.Button("Join US(हमसे जुड़ें) ", id="JOIN_US", 
                                        
                                        className="fa fa-arrow-right",
                                        color="primary",
                                
                                      
                                        
                                      ),
                          
                            
                            href="/userform",
                            
                            style={"text-align":"left"},
                          ),
              # dbc.Button("Join US(हमसे जुड़ें)", color="primary",href='/userform'),
            ]
            
            
            
        ),
    ],
    style={"width": "28rem","height":"27rem","border-bottom":"4px solid rgb(38, 23, 106)","border-radius":"10px"},
)


ContactUS = dbc.Card(
    [
       dbc.Row([
           
           # dbc.Col("",width=5),
           
           
           
           
           dbc.Col(   html.Img(src='/assets/mainpage/contact1.jpg', width="100%",height="100%",),width=12,style={"height":"10rem"}
                   
            ),   
        
           
        
           
           ],style={"height":"10rem"}
          
           
           
           ),
   
       
       
       
        dbc.CardBody(
            [
                html.H5(" Contact Apna dal-S (अपना दल-एस में शामिल हों)", className="card-title",style={"font-weight":"bold","color":"rgb(38, 23, 106)","font-size":"18px"}),
                dbc.Row(
                [
           
                     dbc.Col(dbc.NavLink( html.I( className="facebookBtn smGlobalBtn1",style={"margin-left":"3px"}),href="https://www.facebook.com/ApnaDal.Official/"),md=3,xs=3,sm=3),
                     dbc.Col(dbc.NavLink(  html.I( className="twitterBtn smGlobalBtn1",style={"margin-left":"3px"}),href="https://twitter.com/apnadalofficial"),md=3,xs=3,sm=3),   
                     dbc.Col(dbc.NavLink( html.I( className="googleplusBtn smGlobalBtn1",style={"margin-left":"3px"}),href="https://www.youtube.com/channel/UChsiArcNzKv9dDeV1S_zv-w"),md=3,xs=3,sm=3),
                     
                   
                   ],
                ),
                
              
 
    
     
                      dbc.Row( dbc.Col("Contact Information(Camp Office Lucknow)",style={"font-weight":"bold"})),
                      dbc.Row( dbc.Col("1-A Mall Avenue Lucknow-226001",className="fa fa-map-marker"),style={"margin-top":"2px"}),
                      # html.Br(),
                      dbc.Row( dbc.Col("+919454400742",className="fa fa-phone"),style={"margin-top":"2px"}),
                      # html.Br(),
                      dbc.Row( dbc.Col(
                          "officeapnadals@gmail.com ",className="fa fa-envelope"),style={"margin-top":"2px"}),
                    

            ],style={"overflow":"auto","height":"10rem"}
            
            
            
        ),
    ],
    style={"width": "28rem","height":"27rem","border-bottom":"4px solid rgb(38, 23, 106)","border-radius":"10px"},
)

reachOfficial = dbc.Card(
    [
       dbc.Row([
           
           # dbc.Col("",width=5),
           
           
           
           
           dbc.Col(   html.Img(src='/assets/mainpage/official.jpg', width="100%",height="100%",),width=12,style={"height":"25rem","opacity": 0.9},
                   
            ),   
        
           
        
           
           ],style={"height":"10rem"}
          
           
           
           ),
  
       
       
       
       
    dbc.CardImgOverlay(    
        
        # dbc.CardBody(
            [
                html.H5("APNA DAL-S OFFCIAL WEBSITE",style={"text-align":"center","font-weight":"bold","color":"rgb(38, 23, 106)"}),
                dbc.NavLink( dbc.Button("Visit Our Official Website(हमारी आधिकारिक वेबसाइट पर जाएं) ",  id="OFFICIAL",n_clicks=0,
                                       
                                         # className="fa fa-arrow-right",
                                         # color="primary",
                               
                                       # style={"text-align":"center","background":"none","color":"blue","border":"none","font-weight":"bold","text-decoration":"underline"}
                                       
                                       ),
                              # className="fa fa-arrow-right",
                           
                              href="https://www.apnadal.org/",
                           
                             style={"text-align":"left","top":"0"},
                           ),
                
  
            ]
            
            
           # ), 
        ),
    ],
    style={"width": "28rem","height":"27rem","border-bottom":"4px solid rgb(38, 23, 106)","border-radius":"10px"},
)







image={"height":"100%","width":"100%",}



MainContent=html.Div(
    [
    html.Hr(), 
    dbc.Row([
         dbc.Col(
             
                [
                 
                 dbc.Row(JoinUS),
                 dbc.Row(ReachUS,className="my-4"),
                 
                 
                 ],
             
             
           md=3),
         
         
         
         
         dbc.Col(
             [
                 
                  dbc.Carousel(
                    items=[
                   
                        {"key": "1", "src": "/assets/mainpage/s1.jpg","img_class_name":"image","img_style":image },
                        {"key": "2", "src": "/assets/mainpage/s2.png","img_class_name":"image","img_style":image},
                        {"key": "3", "src": "/assets/mainpage/s3.jpg","img_class_name":"image","img_style":image},
                        {"key": "4", "src": "/assets/mainpage/s4.jpg","img_class_name":"image","img_style":image},
                        {"key": "4", "src": "/assets/mainpage/s5.jpg","img_class_name":"image","img_style":image},
                       
                    ], 
                    controls=True,
                    indicators=True,
                    variant="dark",
                    interval=2000,
                    className="carousel",
                  
                    # style={"width":"100%","align-items":"center","height":"200px","border":"2px solid red",}
                  ), 
                 
                 
                 
                 ],
             
             
             md=6),
         
         
         
         
         
         dbc.Col(
             
             [
                 
                 dbc.Row(ContactUS),
                 dbc.Row(reachOfficial,className="my-4"),
                 
                 
                 ],md=3),
         
         
         
        
        
        ], justify="evenly",
        
        ),
    
    
    
    
    


 ],
    
    style={"margin-left":"0.5rem","margin-right":"0.5rem"}
 # style={"text-align":"center","width":"50vh","border":"2px solid red","height":"50vh","margin":"5rem 43rem"}

 )








# MainPageLayout1=html.Div("HIIIIIIIIIIIIIIIIIIIIIIIII",  id="MainLayout",)

MainPageLayout=Header,html.Br(),MainContent

layout=MainPageLayout




# no=0

# @app.callback(
    # Output('MainLayout', 'children'),
    # [Input('OFFICIAL', 'n_clicks')])
    # )
# def ShowOfficialWebsite(input1):
#       if input1>0:
#             # MainPageLayout=Header,officalIframe
#             return Header,html.Br(),officalIframe
           
#       else:
#           return Header,html.Br(),MainContent




# @app.callback(
#     Output('MainLayout', 'children'),
#     [Input('OFFICIAL', 'n_clicks')])
# def ShowOfficialWebsite1(input1):
#       global no
#       if input1>0:
#             no=3
#             # return no
#             # MainPageLayout=Header,officalIframe
#             # return Header,html.Br(),officalIframe
           
#       else:
#           no=0
#           # return no
#           # return Header,html.Br(),MainContent




# print(no)
# MainPageLayout=ShowOfficialWebsite(no)

# ShowOfficialWebsite(0)
        
         




# MainPageLayout=dbc.Row([
#     dbc.Row(Header),
#     # dbc.Row(MainContent),
    
#     ])
