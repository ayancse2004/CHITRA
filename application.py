# index page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc

from app import app, server
from flask_login import logout_user, current_user
from views import login, error, page1, page2, profile, user_admin,page3

import numpy as np
from flask import Flask, jsonify

from views.UserMemberFormEntry import USER_FORM

from views.UserMemberFormEntry import layout

from views import ReachUS

from views import MainPage

import dash_trich_components as dtc



from views import login, error, page1, page2, profile, user_admin,page3,IndiaMap2
from views import UserMemberFormEntry,MemberAnalysis
from views import ReachUS
from views import EmailLogin
from flask import session
from views import NotificationControl


from views import NotificationControl

from views import PortfolioMngmnt
# import os
# print(os.environ['DISPLAY'])
# #os.environ['DISPLAY'] = '1'
# import pyautogui
# print(pyautogui.position())


HEADER_NAME="APNA DAL-S"

HEADER_NAME=""

SIDEBAR_HIDEN = {
    "position": "fixed",
    "margin-top": "1rem",
    
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f2e3e3",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    # "margin-top": "-0.2rem",
    "transition": "margin-left .5s",
    "margin-left": "12.1rem",
    "margin-right": "1.2rem",
    # "padding": "0.2rem 0.2rem",
    "background-color": "#f2e3e3",
    
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "0.5rem",
    "margin-right": "0.5rem",
    "z-index":"20005",
    "margin-bottom": "10rem",
 
   # "padding": "0.2rem 0.2rem",
    #"background-color": "#f2e3e3",
}


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    # "top": "2.8rem",
    "left": 0,
    "bottom": 0,
    "width": "12.2rem",
    "height":"100vh",
    "z-index": 99999,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f2ece6",
    

    

}


CONTENT_STYLE_FOOTER = {
    "bottom":"0rem",
    "position": "fixed",
    "margin-bottom": "0",
    "width":'100%',
    #"transition": "margin-left .5s",
    #"margin-left": "16.1rem",
    #"margin-right": "16.1rem",
    #"padding": "0.2rem 0.2rem",
    "background-color": "#1fa67a",
    "z-index":"1999",
    
}

navigateTopLayout= html.Div(
                             html.A(  html.I( className="HomeBtn smGlobalBtn",style={"margin-left":"3px",},),href="mainpage",),
                             ),


custombtn=dbc.Row([
    
    dbc.Col(
        [
         
         
         
      
         
      html.A( 
          
          html.I( className="facebookBtn smGlobalBtn",style={"margin-left":"3px"},), 
          
          href="https://www.facebook.com/ApnaDal.Official/"
          ),
        html.A(   html.I( className="twitterBtn smGlobalBtn",style={"margin-left":"3px"},),href="https://twitter.com/apnadalofficial"),
        html.A(  html.I( className="googleplusBtn smGlobalBtn",style={"margin-left":"3px"},),href="https://www.youtube.com/channel/UChsiArcNzKv9dDeV1S_zv-w"),
      
     
      
         
         ],style={"text-align":"center","margin":"0.2px"}
        ),
    
    dbc.Col(    html.Div(navigateTopLayout),)
        



    
    
    ])










FOOTER=html.Div([
    

html.Footer([
  
    
  dbc.Row([
      
      
      
      
        
      dbc.Col([
          
          html.Div(id="AdminCtrl"),
          
          ],lg=1,sm=2,xs=2,md=1,style={"text-align":"center"}
              
              ),
      
      dbc.Col([
          
          html.Div( "Copyright © 2022 Apnadal-S. Designed By IT-CELL and Developed by Hanumanganj-Singh Software Solution" ,
                   style={"textAlign": "center",'color':'white','font-weight':'bold','font-size':'1.5vh'}, id='footer-text'),
          
          ],lg=7,sm=4,xs=12,md=7
              
              ),
    
      
      
      dbc.Col([
          
          custombtn,
          
          
          ],lg=4,sm=6,xs=12,md=4,style={"text-align":"center"}
              
              ),
      
      
      
      ])

 

    ],style=CONTENT_STYLE_FOOTER,id="footer"),
  ])




@app.callback(
    Output('AdminCtrl', 'children'),
    [Input('footer', 'children')])
def ShowAdminCtrl(input1):
    
    #print()
    if session.get("login")==1:
         print("Login in Footer")
         return  page3.navlayout
    
    else:
        if( current_user.is_authenticated):
             return  page3.navlayout
           
        else:
             return   ""








navBar = dbc.Navbar(id='navBar',
    children=[
        
        
   
        ],
    sticky='top',
     
    style={"z-index":"55","min-height":"3rem"},
    
    
    color="#ff9933",
  
    #dark=True,
    className='text-light font-weight-bold',
 
    
)

sidebar = html.Div(id='sideBar',
    children=[
       
        ],
    
    
    className='text-light font-weight-bold'

)


content = html.Div(id="pageContent",
                   
    children=[
    
    ],style=CONTENT_STYLE1)







subcontent= html.Div(
  id="page_content1",children=[],)







app.layout = html.Div([
    dcc.Store(id='side_click'),
    dcc.Location(id='url',refresh=True),

    html.Div([
        
        navBar,
        # offcanvas,
        content,
        # subcontent,
        FOOTER,
        
        
    ])
] ,style={"height":"100%"},id='table-wrapper')

#"background-color": "#f8f9fa"

################################################################################
# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
################################################################################
@app.callback(
    
             Output('pageContent', 'children'),
              
              
              [Input('url', 'pathname'),
               
               ])
def displayPage(pathname):
    
    print("session.get",session.get("login"))
    
    if pathname == '/login':
             if session.get("login")==1:
                 return page3.layout
                 
             if current_user.is_authenticated:
                 return page3.layout
                
             else:
            
               return login.layout
    
    if pathname == '/':
       
        if current_user.is_authenticated:
            return MainPage.layout
           
        else:
            return MainPage.layout

    elif pathname == '/logout':
        if session.get("login")==1:
            session['login']=0
            return MainPage.layout 
        if current_user.is_authenticated:
            logout_user()
            return MainPage.layout 
        else:
            return MainPage.layout 

    # if pathname == '/page1':
    #     if current_user.is_authenticated:
    #         return page3.layout
    #     else:
    #         return login.layout

    # if pathname == '/page2':
 
    #     if current_user.is_authenticated:
    #         return page3.layout
    #     else:
    #         return login.layout
        
    if pathname == '/page3':
            if current_user.admin ==1 or current_user.admin ==0:
                return page3.layout
            else:
                return login.layout
            
    if pathname == '/details':
         if session.get("login")==1:
             return page3.layout
         if current_user.is_authenticated:
             if current_user.admin ==1 or current_user.admin ==0:
                return page3.layout
             else:
               return login.layout


         try: 
             
             if current_user.admin ==1 or current_user.admin ==0:
                    return page3.layout
             else:
                   return login.layout   
         except:  
             print(current_user)
             return login.layout   
            
    if pathname == '/details2':
         if session.get("login")==1:
              return page3.layout
         else:
              return login.layout

    if pathname == '/profile':
     
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout
        
    if pathname == '/userform':
            
            return (USER_FORM)
        
        
    if pathname == '/emailLoginPage':
        
        if session.get("login")==1:
            return page3.layout
        if current_user.is_authenticated:
            if current_user.admin ==1 or current_user.admin ==0:
               return page3.layout
            else:
              return EmailLogin.layoutDirect


        try: 
            
            if current_user.admin ==1 or current_user.admin ==0:
                   return page3.layout
            else:
                  return EmailLogin.layoutDirect   
        except:  
            
            return EmailLogin.layoutDirect 

   
    
    if pathname == '/adminform':
                
                return (layout) 
            
    if pathname == '/reachform':
                        
            return (ReachUS.layout) 
    if pathname == '/notifications':
    
        
        if session.get("login")==1:
            return page3.layout
        if current_user.is_authenticated:
            if current_user.admin ==1 or current_user.admin ==0:
               return page3.layout
            else:
              return NotificationControl.layoutDirect


        try: 
            
            if current_user.admin ==1 or current_user.admin ==0:
                   return page3.layout
            else:
                  return NotificationControl.layoutDirect   
        except:  
            
            return NotificationControl.layoutDirect 
                        
            # return (NotificationControl.layout)     
            
            
            
    if pathname == '/memberslist':
    
        
        if session.get("login")==1:
            return page3.layout
        if current_user.is_authenticated:
            if current_user.admin ==1 or current_user.admin ==0:
               return page3.layout
            else:
              return UserMemberFormEntry.layoutDirect


        try: 
            
            if current_user.admin ==1 or current_user.admin ==0:
                   return page3.layout
            else:
                  return UserMemberFormEntry.layoutDirect   
        except:  
            
            return UserMemberFormEntry.layoutDirect         

    if pathname == '/mainpage':
          
        if current_user.is_authenticated:
               return MainPage.layout
            
        else:
            return MainPage.layout 
        
    # if pathname =="/proceedcard":
    #     return EmailLogin.layoutDirect
    if pathname == '/portfolio':
        
        
        return PortfolioMngmnt.layout 
        
        
        if session.get("login")==1:
            return page3.layout
        if current_user.is_authenticated:
            if current_user.admin ==1 or current_user.admin ==0:
               return page3.layout
            else:
               return PortfolioMngmnt.layout


        try: 
            
            if current_user.admin ==1 or current_user.admin ==0:
                   return page3.layout
            else:
                  return PortfolioMngmnt.layout  
        except:  
            
            return PortfolioMngmnt.layout 
       
    if pathname == '/admin':
      
        if current_user.is_authenticated:
            if current_user.admin == 1:
                return user_admin.layout
            else:
                return error.layout
        else:
            return MainPage.layout


    else:
        return error.layout


################################################################################
# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
################################################################################
@app.callback(
    Output('navBar', 'children'),
    [Input('pageContent', 'children'),
     Input('url', 'pathname')])
def navBar(input1,pathname):
    if session.get("login")==1:
        navBarContents = [
        
        
          page3.navlayout,
        
        
           dbc.Row(
               [
                   # dbc.Col(html.Img(src='/assets/apnadal.jpg', height="40px"),style={"margin-top": "0.1rem","text-align":"left"}),
                   # dbc.Col(html.Img(src='/assets/apnadal3.jpg', height="40px"),style={"marginpage1-top": "0.1rem",}),
                   dbc.Col(html.Img(src='/assets/apnadal.jpg', height="40px"),style={"margin-top": "0.1rem","text-align":"left","margin-left":"0.5rem"}),
                   dbc.Col(html.Img(src='/assets/apnadal3.jpg', height="40px"),style={"margin-top": "0.1rem","margin-right": "0.4rem",}),
                   # dbc.Col(html.Button("Home",id="Back_to_Home",n_clicks=0)),
                   
                   # dbc.Col(dbc.NavbarBrand(HEADER_NAME, className="ms-2"),style={"margin-left": "0.5rem",}),
                  
               ],style={"text-align":"left",},
               align="left",
               
               className="g-0",
          
              
           ),
         

        
       
            
           dbc.DropdownMenu(
              
                #nav=True,
                 toggle_style={
           "textTransform": "uppercase",
           "background": "rgb(255, 153, 51)",
           "border":"2px solid orange",
           "color":"blue",
           "font-weight":"bold"
              },
                color="rgb(255, 153, 51)",
                in_navbar=True,
                label="Admin",
            
                children=[
                    dbc.DropdownMenuItem('Profile', href='/profile',),
                    dbc.DropdownMenuItem('Admin', href='/admin'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem('Logout', href='/logout'),
                ],
              style={"textDecoration": "none","color":"black",'padding-left':'0rem',"margin-top": "0.1rem","right":"0","text-align":"right"}
            ),  
                    
                    
         
                  
       
    ]
    
        if pathname=="/mainpage":
               return ""
        
        else:
               return navBarContents
    
    
    
    
    if current_user.is_authenticated:
        if current_user.admin ==1:
            navBarContents = [
                
                
                # dbc.Row(
                #    dbc.Button("Menu", outline=False, n_clicks=0,color="primary", id="btn_sidebar", className="fa fa-list-alt",),
                #    id="Row_lg"),
                # dbc.Row(
                #    dbc.Button("", outline=False, n_clicks=0,color="primary", id="btn_sidebar", className="fa fa-list-alt fa-4x",),
                #    id="Row_sm"),
                
                  page3.navlayout,
                
                
                   dbc.Row(
                       [
                           # dbc.Col(html.Img(src='/assets/apnadal.jpg', height="40px"),style={"margin-top": "0.1rem","text-align":"left"}),
                           # dbc.Col(html.Img(src='/assets/apnadal3.jpg', height="40px"),style={"marginpage1-top": "0.1rem",}),
                           dbc.Col(html.Img(src='/assets/apnadal.jpg', height="40px"),style={"margin-top": "0.1rem","text-align":"left","margin-left":"0.5rem"}),
                           dbc.Col(html.Img(src='/assets/apnadal3.jpg', height="40px"),style={"margin-top": "0.1rem","margin-right": "0.4rem",}),
                           # dbc.Col(html.Button("Home",id="Back_to_Home",n_clicks=0)),
                           
                           # dbc.Col(dbc.NavbarBrand(HEADER_NAME, className="ms-2"),style={"margin-left": "0.5rem",}),
                          
                       ],style={"text-align":"left",},
                       align="left",
                       
                       className="g-0",
                  
                      
                   ),
                 
            
                  # dbc.NavItem(dbc.NavLink('Home', href='/mainpage',
                  #   style={"textDecoration": "none","color":"black","text-align":"left",'padding-left':'3.5rem'})),
                  
                  
                  
                  
               
                 # dbc.Offcanvas(
                 #     [
                    
                     
                 #     dbc.Row([
                 #         dbc.Col([
                         
                 #         html.I( className="fa fa-info-circle fa-2x"),],xs=1),
                 #         dbc.Col([
                 #         dbc.NavLink("Total Members(India)",id='id_4',style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},),
                 #         ],xs=11),
                         
                 #         ],),
                 #     dbc.Row([
                 #         dbc.Col([
                 #         html.I( className="fa fa-list-alt fa-2x"),],xs=1),
                 #         dbc.Col([
                 #         dbc.NavLink("Member Registration",id='id_3', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
                 #         ],xs=11),
                         
                 #         ],style={"left":"0"}),
                 #     dbc.Row([
                 #         dbc.Col([
                 #         html.I( className="fa fa-info-circle fa-2x"),],xs=1),
                 #         dbc.Col([
                 #         dbc.NavLink("Reach US",id='id_6', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
                 #         ],xs=11),
                         
                 #         ],),
                 #     dbc.Row([
                 #         dbc.Col([
                 #         html.I( className="fa fa-cog fa-2x"),],xs=1),
                 #         dbc.Col([
                 #         dbc.NavLink("Active Members Analysis",id='id_5',style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
                 #         ],xs=11),
                         
                 #         ],),
                 #     dbc.Row([
                 #         dbc.Col([
                           
                 #         html.I( className="fa fa-home fa-2x"),], xs=1 ),
                 #         dbc.Col([ dbc.NavLink("Visitor Mgmt",id='id_1',style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
                 #            ],xs=11),
                           
                         
                 #         ],),
                 #     dbc.Row([
                 #         dbc.Col([
                 #         html.I( className="fa fa-chart-line fa-2x"),],xs=1),
                 #         dbc.Col([
                 #         dbc.NavLink("Complain Mgmt",id='id_2', style={"color":"white","font-weight":"bold","font-family": "Times New Roman","cursor":"pointer"},)
                 #         ],xs=11),
                         
                 #         ]),
                     
                     
                     
                     
                     
                     
                
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                 #     ], className="g-12",
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                 #     id="offcanvas",
                 #     title="Main Menu",
                 #     is_open=False,
                     
                 #     style={"color":"white","background-color":"rgb(70, 161, 164)","font-weight":"bold"}
                 # ),
                 
                 
                # dbc.NavItem(dbc.NavLink('Admin Control', href='/page3',id="AC_lg",
                #         style={"textDecoration": "none","color":"black","text-align":"left",})),
                
                # dbc.NavItem([dbc.NavLink('AC', href='/page3',id="AC_sm",
                #         style={"textDecoration": "none","color":"black","text-align":"left",}),
                            
                            
        #                     dbc.Tooltip(
           
        #     "Admin Control",
        #     target="AC_sm",
        # ),
                            
                            
        #                     ],
                            
                            
        #                     ),
                
               
                    
                   dbc.DropdownMenu(
                      
                        #nav=True,
                         toggle_style={
                   "textTransform": "uppercase",
                   "background": "rgb(255, 153, 51)",
                   "border":"2px solid orange",
                   "color":"blue",
                   "font-weight":"bold"
                      },
                        color="rgb(255, 153, 51)",
                        in_navbar=True,
                        label=current_user.username,
                    
                        children=[
                            dbc.DropdownMenuItem('Profile', href='/profile',),
                            dbc.DropdownMenuItem('Admin', href='/admin'),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem('Logout', href='/logout'),
                        ],
                      style={"textDecoration": "none","color":"black",'padding-left':'0rem',"margin-top": "0.1rem","right":"0","text-align":"right"}
                    ),  
                            
                            
                 
                          
               
            ]
            
            if pathname=="/mainpage":
                   return ""
            
            else:
                   return navBarContents

        else:
            navBarContents = [
                page3.navlayout,
               
                
                html.A(
                   # Use row and col to control vertical alignment of logo / brand
                   dbc.Row(
                       
                         # page_content
                       [
                           dbc.Col(html.Img(src='/assets/apnadal.jpg', height="40px"),style={"margin-top": "0.1rem","text-align":"left"}),
                           dbc.Col(html.Img(src='/assets/apnadal3.jpg', height="40px"),style={"margin-top": "0.1rem",}),
                           
                           # dbc.Col(dbc.NavbarBrand(HEADER_NAME, className="ms-2"),style={"margin-left": "0.5rem",}),
                           
                           
                       ],
                       style={"text-align":"left","margin-left":"0rem"},
                       align="left",
                       
                       className="g-0",
                      
                   ),
                   href='/page1',
                   style={"textDecoration": "none"},
                   ),
                 # dbc.Button("Sidebar", outline=True, n_clicks=0,color="primary", className="mr-4", id="btn_sidebar"),
                 # dbc.Offcanvas(
                 #     layout_dtc,
                 #     # html.P(
                 #     #     "This is the content of the Offcanvas. "
                 #     #     "Close it by clicking on the close button, or "
                 #     #     "the backdrop."
                 #     # ),
                 #     id="offcanvas",
                 #     title="Title",
                 #     is_open=True,
                 # ),
             
                # dbc.NavItem(dbc.NavLink('Local Control', href='/page3',
                                        
                #                         style={"textDecoration": "none","color":"black","text-align":"left",'padding-left':'0rem'}
                                        
                                        
                #                         )),
            
                dbc.DropdownMenu(
                    #nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem('Logout', href='/logout'),
                    ],
                    style={"textDecoration": "none","color":"black",'padding-left':'0rem',"margin-top": "0.1rem"}
                ),
            ]
            
            if pathname=="/mainpage":
                   return ""
            
            else:
                   return navBarContents

    else:
        return ''






# New Layout



# @app.route('/')
#     def index():
        
# @server.route("/login1")
# def hello():
#     if current_user.is_authenticated:
#         return "user is Authenticated"
       
#     else:
   
#       return "login.layout"






















# New Layout

# layout_dtc = dbc.Col([
#     dtc.SideBar([
        
#         dtc.SideBarItem(id='id_4', label="Total Members(India)", icon="fas fa-info-circle"),
        
      
        
#         dtc.SideBarItem(id='id_3', label="Member Registration", icon="far fa-list-alt"),
        
        
#         dtc.SideBarItem(id='id_6', label="Reach US", icon="fas fa-chart-line"),
        
#         dtc.SideBarItem(id='id_5', label="Active Members Analysis", icon="fas fa-cog"),
      
#         dtc.SideBarItem(id='id_1', label="Visitor Mgmt", icon="fas fa-home"),
        
#         dtc.SideBarItem(id='id_2', label="Complain Mgmt", icon="fas fa-chart-line"),
        
        
       
        
     

     
#     ]),
    
    # html.H4("", style={"textAlign": "center","margin-top": "20px",'color':'#fff','height':'50px','fontWeight':'bold',"background-color":"rgb(91, 127, 128)","font-family":"Segoe UI Semibold",'width':'48px'}),
    
    
    # html.Div([
    # ], id="page_content",style={"margin-bottom": "6rem","max-height":'100%',"margin-top":"4.2rem","position":"static",}),

    
  
# ],style={"margin-top":"-3.8rem","z-index":"1090","position":"static",})





# offcanvas = html.Div(navlayout
#     [
#         # dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
#         dbc.Offcanvas(
#             layout_dtc,
#             # html.P(
#             #     "This is the content of the Offcanvas. "
#             #     "Close it by clicking on the close button, or "
#             #     "the backdrop."
#             # ),
#             id="offcanvas",
#             title="Title",
#             is_open=True,
#         ),
#     ],id="test"
# )











# @app.callback(
#     Output('offcanvas', 'is_open'),
#     [Input('btn_sidebar', 'n_clicks')],
#     [State("offcanvas", "is_open")],)

# def ShowOffCanvas(n1, is_open):
    
#     if n1>0:
#       return not is_open
     
#     return is_open 
        
 
        
 
    
 
    
 
    
 
    
 
# import pandas as pd
 
    

# @app.callback(
#     Output("page_content1", "children"),
#     [
#         Input("id_1", "n_clicks_timestamp"),
#         Input("id_2", "n_clicks_timestamp"),
#         Input("id_3", "n_clicks_timestamp"),
#         Input("id_4", "n_clicks_timestamp"),
#         Input("id_5", "n_clicks_timestamp"),
#         Input("id_6", "n_clicks_timestamp"),
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
        
       
 




################################################################################
# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
################################################################################
# @app.callback(
#     Output('sideBar', 'children'),
#     [Input('pageContent', 'children')])
# def SideBar(input1):
#     if current_user.is_authenticated:
#         if current_user.admin == 1:
#             navBarContents = [

#                 dbc.Nav(
#                     [
#                         # dbc.NavLink("Home", href="/page-1", id="page-1-link"),
#                         # dbc.NavLink("Cabinet's Param", href="/page-2", id="page-2-link"),
#                         # dbc.NavLink("Prognostic ", href="/page-3", id="page-3-link"),
#                         # dbc.NavLink("CWCM-A1", href="/page-4", id="page-4-link"),
#                         # dbc.NavLink("Parameter Trends",href="/page-5", id="page-5-link"),
#                         # dbc.NavLink("Parameter View",href="/page-6", id="page-6-link"),
#                         # dbc.NavLink("Cabinet MTBF",href="/page-7", id="page-7-link"),
                        
                                        
                 
#                         dbc.NavLink("Visitor Mgmt", href="/page1", id="page-1-link"),
                     
#                         dbc.NavLink("Visitor Info",href="/page2", id="page-2-link"),
                    
#                         dbc.NavLink("Local Control",href="/page3", id="page-3-link"),
                     
                        
             
        
                       
#                     ],
#                     pills=True,
#                     vertical=True,
                  
                    
                    
                  
#                 ),
               
#             ]
#             return navBarContents

#         else:
#             navBarContents = [
#             dbc.Nav(
#                 [
                        
#                         dbc.NavLink("Visitor Mgmt", href="/page1", id="page-1-link", style={"color": "black",}),
#                         html.Br(),
#                         dbc.NavLink("Visitor Info",href="/page2", id="page-2-link", style={"color": "black",}),
#                         html.Br(),
#                         dbc.NavLink("Local Control",href="/page3", id="page-3-link", style={"color": "black",}),
#                         html.Br(),
                   
#                 ],
#                 vertical=True,
#                 pills=True,
#             ),
#             ]
#             return navBarContents

#     else:
#         return ''



# @app.callback(
#     [
#         Output("sideBar", "style"),
#         Output("pageContent", "style"),
#         Output("side_click", "data"),
#     ],
    
 

#     Input("btn_sidebar", "n_clicks"),
#     State("side_click", "data"),

 
# )
# def toggle_sidebar(n, nclick):
    
#     if n:
    
#         #print(n,nclick)
#         if nclick == "SHOW":
#             sidebar_style = SIDEBAR_HIDEN
#             content_style = CONTENT_STYLE1
#             cur_nclick = "HIDDEN"
#         else:
#             sidebar_style = SIDEBAR_STYLE
#             content_style = CONTENT_STYLE
#             cur_nclick = "SHOW"
#     else:
#         #print(n,nclick)
#         sidebar_style = SIDEBAR_STYLE
#         content_style = CONTENT_STYLE
#         cur_nclick = 'SHOW'

#     return sidebar_style, content_style, cur_nclick
    

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
# @app.callback(
#     [Output(f"page-{i}-link", "active") for i in range(1, 4)],
  
   
#     Input("url", "pathname"),
# )
# def toggle_active_links(pathname):
#     #print("HI")
#     if pathname == "/":
#         # Treat page 1 as the homepage / index
#         return True,False,False
#     return [pathname == f"/page{i}" for i in range(1, 4)]

application = app
application.title='Dash on AWS EB!'

if __name__ == "__main__":
    application.run_server(debug=False, port=5556,host='0.0.0.0')