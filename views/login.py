import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash


layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlLogin', refresh=True),
        
            
        
        html.Div([
            dbc.Container([
                dbc.Row([
                    
                    dbc.Col(html.H5("Welcome to Admin Login Page"),style={'textAlign':'center',"font-size":'3.0vmin'}),
                    html.Hr(style={'width':'95%'}),
                    dbc.Col(html.Img(src='/assets/apnadal.jpg', height="150px"),style={"margin-top": "0.1rem",}),
                
                    dbc.Col(html.Img(src='/assets/apnadal3.jpg', height="150px"),style={"margin-top": "0.1rem",}),
                    ]
                        ),
  
                
                html.Hr(),
            ],style={"background-color":"",'textAlign':'center'}),
            dbc.Container(id='loginType', children=[
                dcc.Input(
                    placeholder='Enter your username',
                    type='text',
                    id='usernameBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                dcc.Input(
                    placeholder='Enter your password',
                    type='password',
                    id='passwordBox',
                    className='form-control',
                    n_submit=0,
                ),
                
                
                
                html.Br(),
                
                dbc.Row([
                    
                    dbc.Col([
                        
                        html.Button(
                            children='Admin Login',
                            n_clicks=0,
                            type='submit',
                            id='loginButton',
                            style={"font-size":"2.0vh"},
                            className='btn btn-primary btn-lg'
                            
                        ),
                        ]),
                    
                    dbc.Col([
                        # dbc.NavLink(
                            
                            html.Button(
                                
                             children= "OTP Login" ,
                             n_clicks=0,
                             type='submit',
                             id='Email_Login',
                             style={"font-size":"2.0vh"},
                            
                             className='btn btn-primary btn-lg'
                         # ),
                            # href="/mainpage",
                            
                            ) ,
                        ]),
                    
                    ]),
                
              
              
               
               
               
                html.Br(),
            ], className='form-group'),
        ]),
    ], className='jumbotron',style={'width':'100%'})
],style={'max-width':'500px','min-width':"100px",'margin-top':'5rem','margin-bottom':'5rem',})



################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - REDIRECT TO PAGE1 IF LOGIN DETAILS ARE CORRECT
################################################################################
@app.callback(Output('urlLogin', 'pathname'),
              [
              Input('Email_Login', 'n_clicks'),
              Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def sucess(Email_Login,n_clicks, usernameSubmit, passwordSubmit, username, password):
    #print("LOgin1")
    #print(username,password)
    if Email_Login>0:
        return "/emailLoginPage"
    
    else:
    
       user = User.query.filter_by(username=username).first()
       
    
       #print(user)
       if user:
           #print(user.password,password)
           if check_password_hash(user.password, password):
           #if user.password==password:
               #print("HIII")
               login_user(user)
               return '/details'
           else:
               #print("BYEE")
               pass
       else:
           pass


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('usernameBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    #print("LOgin2")
    #print(username,password)
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('passwordBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output2(n_clicks, usernameSubmit, passwordSubmit, username, password):
    #print("LOgin3")
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'
