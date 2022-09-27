
# Dash packages
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



# key='key'
# CSV_FILENAME="RepairLifeCycleEntry.csv"
# TABLE_NAME="COMPLAIN_MANAGEMENT"
# createTableSchema='''(key VARCHAR(255) PRIMARY KEY,partnumber VARCHAR(255),serialnumber VARCHAR(255),description VARCHAR(1000),problemlist VARCHAR(255),
#         problemdetails VARCHAR(255),assignto VARCHAR(255),taskstatus VARCHAR(255),Complaintdate VARCHAR(255),Attendeddate VARCHAR(255),Closeddate VARCHAR(255));'''
# CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)


###############################################################################
########### PAGE 2 LAYOUT ###########
###############################################################################


#print(datetime.today().strftime("%d-%m-%Y"))

PROBLEM_TAKER=["President","Working President","UP Minister","Cabinet Minister","Others","IT Cell","UP-PS"]

PROBLEM_LIST=["Appointment Related","Job-Related",'Land Related','Problem']

def LoadStatusInfoPageHistory():
    
    import os
   
    #print("Called Status Row")   
    path='./CSV/RepairLifeCycleEntry_HISTORY.csv'
    if os.path.isfile(path):
        try:
            dfFile = pd.read_csv(path)
            #print("LoadStatusInfoPageHistory",dfFile)
            return dfFile
        except :
            dfFile = pd.DataFrame()
            return dfFile
           
            
        if len(dfFile.index)>0:
                return dfFile
        else:
            
        
           dfFile.loc[0] = 'INVALID'
      

           #print(dfFile)
           return dfFile
            
     
    else:
        print("NULL")
        pd.DataFrame()


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

def LoadStatusInfoPageLatest_Query(col=None,con=None):
    
    import os
   
    print("Called Query Row")   
    path='./CSV/RepairLifeCycleEntry.csv'
    if os.path.isfile(path):
        try:
            dfFile = pd.read_csv(path)
        except :
            dfFile = pd.DataFrame()
           
            
        if len(dfFile.index)>0:
                #print(dfFile)
                #print(col,con)
                dfFile=dfFile[dfFile[col]==con]
                #print("Query")
                #print(dfFile)
                return dfFile
        else:
             dfFile.loc[0] = 'INVALID'
        

             #print(dfFile)
             return dfFile
              
     
    else:
        pd.DataFrame()


def ReturnDateisValidorNot(DataData=None):
    from datetime import datetime
 
    # initializing string
    test_str = DataData
     
    # printing original string
    #print("The original string is : " + str(test_str))
     
    # initializing format
    format2 = "%d-%m-%Y"
     
    # checking if format matches the date
    res = True
     
    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(test_str, format2))
    except ValueError:
        res = False
     
    # printing result
    print("Does date match format? : " + str(res))
    return res


def TwoDataValidation(InitialDate=None,TobeCheckedDate=None):

 

    # initializing string
    Initial_Date_test_str = InitialDate
    
    Last_Date_test_str = TobeCheckedDate
     

  
    format2 = "%d-%m-%Y"
     

    oldDate = []
     
    # using try-except to check for truth value
    try:
        oldDate = (datetime.strptime(Initial_Date_test_str, format2))
    except ValueError:
        oldDate = []
     
        
    NewDate = []
        
       # using try-except to check for truth value
    try:
           NewDate = (datetime.strptime(Last_Date_test_str, format2))
    except ValueError:
           NewDate = []  
    # printing result
    

    res=NewDate>=oldDate
    print("comparision Result of Two dates? : " + str(res))
    return res

def GetNumberofDays(InitialDate=None,TobeCheckedDate=None):

 
    # initializing string
    Initial_Date_test_str = InitialDate
    
    Last_Date_test_str = TobeCheckedDate
     

    format2 = "%d-%m-%Y"
    print(InitialDate,TobeCheckedDate) 

    oldDate = []
     
    # using try-except to check for truth value
    try:
        oldDate = (datetime.strptime(Initial_Date_test_str, format2))
    except ValueError:
        oldDate = []
     
        
    NewDate = []
        
       # using try-except to check for truth value
    try:
           NewDate = (datetime.strptime(Last_Date_test_str, format2))
    except ValueError:
           NewDate = []  
    # printing result
    

    res=NewDate-oldDate
    
    #print("No of days : " + str(res))
    return str(res)








CardFooterStyle={

    "textAlign":"right",
    'background-color':'white',
    }


CardHeaderStyle={

    #'height':'35px',
    #"font-size": "25px",
    "color":"white",
    'textAlign':"right",
    'fontWeight': 'bold',
   
    }

CardImageStyle={"opacity": 1.0,'height':'50px','width':'50px',"margin-top": "0.5rem","margin-left":"1rem"}

CardBodyStyle={"margin-top":"-0.1rem","font-size": "25px","color":"white",'textAlign':"right",'fontWeight': 'bold',}


CardStyle={"margin-left":"1.1rem","margin-right":"1.1rem"}

data=LoadStatusInfoPageHistory()
  
OpenData=data[data['taskstatus']=='InProgress']
OpenData2=data[data['taskstatus']=='Not Completed']

OpenCard = dbc.Card(
    [
         dbc.CardHeader("Open Complaints!",style=CardHeaderStyle),
         dbc.Row(
             
                 [
                    dbc.Col(
                        dbc.CardImg(src="/static/images/Open.png", top=True,style=CardImageStyle,),
                        ),
                    
                    dbc.Col(
                            dbc.CardBody(
                                            [
                                            html.H6(len(OpenData)+len(OpenData2),id="Card_Open" ,className="card-title",style=CardBodyStyle),
                                    
                                            ]
                                        ),
                            ),
                    ]
                 ),
       
        dbc.CardFooter("", style=CardFooterStyle,),
    ],
    style=CardStyle,
    color="danger",
    
   
)

OpenData=data[data['taskstatus']=='InProgress']

ProgessCard = dbc.Card(
    [
         dbc.CardHeader("In Progress Complaints!",style=CardHeaderStyle),
         dbc.Row(
             
                 [
                    dbc.Col(
                        dbc.CardImg(src="/static/images/Progress.png", top=True,style=CardImageStyle,),
                        ),
                    
                    dbc.Col(
                            dbc.CardBody(
                                            [
                                            html.H6(len(OpenData),id="Card_Progress" ,className="card-title",style=CardBodyStyle),
                                    
                                            ]
                                        ),
                            ),
                    ]
                 ),
       
        dbc.CardFooter("", style=CardFooterStyle,),
    ],
    color="info",
    style=CardStyle,
   
)

OpenData=data[data['taskstatus']=='Not Completed']
WaitingCard = dbc.Card(
    [
         dbc.CardHeader("Not Completed Complaints!",style=CardHeaderStyle),
         dbc.Row(
             
                 [
                    dbc.Col(
                        dbc.CardImg(src="/static/images/Waiting.png", top=True,style=CardImageStyle,),
                        ),
                    
                    dbc.Col(
                            dbc.CardBody(
                                            [
                                            html.H6(len(OpenData),id="Card_Waiting" ,className="card-title",style=CardBodyStyle),
                                    
                                            ]
                                        ),
                            ),
                    ]
                 ),
       
        dbc.CardFooter("", style=CardFooterStyle,),
    ],
    color="warning",
    style=CardStyle,
   
)

OpenData=data[data['taskstatus']=='Completed']

CompletedCard = dbc.Card(
    [
         dbc.CardHeader("Completed Complaints!",style=CardHeaderStyle),
         dbc.Row(
             
                 [
                    dbc.Col(
                        dbc.CardImg(src="/static/images/Completed.png", top=True,style=CardImageStyle,),
                        ),
                    
                    dbc.Col(
                            dbc.CardBody(
                                            [
                                            html.H6(len(OpenData),id="Card_Completed" ,className="card-title",style=CardBodyStyle),
                                    
                                            ]
                                        ),
                            ),
                    ]
                 ),
       
        dbc.CardFooter("", style=CardFooterStyle,),
    ],
    color="success",
    style=CardStyle,
   
)


cards = dbc.CardGroup([
    
    OpenCard,
    ProgessCard,
    WaitingCard,
    CompletedCard,
    ])

# layout = dbc.Container([

#         html.H4('Page 1 Layout',style={'textAlign': 'center','color':'black',"background-color": "#f0f3f7",}),
#         cards,
       
#         html.Hr(),


# ], className="mt-4")


#print(PART_NUMBER_DATABASE_df)

ComCardStyle={'background-color':'#e65563','color':'white', 'textAlign':"left",
  'fontWeight': 'bold',}

ComCardImageStyle={"opacity": 1.0,'height':'50px','width':'50px',
                   "margin-top": "0.1rem","margin-left":"1rem"}



Com_dropdown_PART =dbc.Row(
    [
    dbc.Row([
        
        dbc.Col(
                        dbc.Label("Select Home Town ", html_for="dropdown"),md=12,sm=12,xs=12,lg=3,
           ),
        dbc.Col(
                    dcc.Dropdown(
                                id="Part_Com_dropdown",
                                options=[{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],
                                ),md=12,sm=12,xs=12,lg=8,
           ),
        
        ])
    
   
    ],
    className="mb-3",
    
)

Com_dropdown_SERIAL =dbc.Row(
    
    [
     dbc.Row(
         [
             dbc.Col(
                             dbc.Label("Name of Candidate", html_for="dropdown"),md=12,sm=12,xs=12,lg=3,
                ),
             dbc.Col(
                             dbc.Input(id="PART_SERAIL_NUMBER",placeholder="Type Serial Number ...", type="text"),md=12,sm=12,xs=12,lg=8,
                 ),
             
             
             ])
     
     
    ],
    className="mb-3",
    
)

Com_dropdown_DESC=dbc.Row(
    [
     dbc.Row([
         dbc.Col(
                         dbc.Label("Part Description", html_for="dropdown"),md=12,sm=12,xs=12,lg=3,
            ),
         dbc.Col(
                     dbc.Input(id="Part-Description-container",style={"border":"1px pink solid"}),md=12,sm=12,xs=12,lg=8,
                    #html.Label(id='Part-Description-container',style={"border":"1px pink solid"}),
            ),
         ])
     
    ],
    className="mb-3",
    
)


Com_dropdown_problem = dbc.Row(
    [
     dbc.Row([
         dbc.Col(
                         dbc.Label("Select Problem Description", html_for="dropdown"),md=12,sm=12,xs=12,lg=3,
            ),
         dbc.Col(
                     dcc.Dropdown(
                                 id="Com_problem_dropdown",
                                 options=[{'label':name, 'value':name} for name in PROBLEM_LIST],
                                 clearable=False,
                                 ),md=12,sm=12,xs=12,lg=8,
            ),
         
         
         ])
       
    ],className="mb-3",
)

text_input_problem = dbc.Row(
    
    [
     dbc.Row([
         dbc.Col( dbc.Label("Problem Description Details."),md=12,sm=12,xs=12,lg=3,),
        
         dbc.Col(
                     dcc.Textarea(
                     id='textarea-example',
                     placeholder="Type Something here....",
                     value='',
                     style={'width': '100%', 'height': 70},
                     ),md=12,sm=12,xs=12,lg=8,
                ),
        
         ])
        
    ],className="mb-3",
)

COM_ASSIGN_LAYOUT=dbc.Row(
    [
     dbc.Row([
         dbc.Col( dbc.Label("Assigned To",),md=12,sm=12,xs=12,lg=2,style={"text-align":"left"}),
         
         dbc.Col(
                     dcc.Dropdown(
                                 id="Com_Assign_dropdown",
                                 options=[{'label':name, 'value':name} for name in PROBLEM_TAKER],
                                 clearable=False,
                                 ),
                     
                     md=12,sm=12,xs=12,lg=2,
            ),
        
         dbc.Col( dbc.Label("Status"),md=12,sm=12,xs=12,lg=1,style={'textAlign':'left'}),
         
         dbc.Col(
                     dcc.Dropdown(
                                 id="Com_Status_dropdown",
                                 options=[{'label':name, 'value':name} for name in ["InProgress","Not Completed"]],
                                 clearable=False,
                                 ),md=12,sm=12,xs=12,lg=2,
            ),
         
         
         dbc.Col( dbc.Label("Creation Date/Issue Date"),md=12,sm=12,xs=12,lg=2,style={'textAlign':'left'}),
        
         dbc.Col(
                    dcc.DatePickerSingle(
                                            id='my-date-picker-single',
                                            min_date_allowed=date(2010, 8, 5),
                                            max_date_allowed=date.today(),
                                           
                                            initial_visible_month=date.today() - timedelta(days=7),
                                            display_format='DD-MM-YYYY',
                                            date=date.today() - timedelta(days=7),
                                   ) ,md=12,sm=12,xs=12,lg=2,
                ),
         
         
         
         
         ],),
     
          
       
        
    ],className="mb-2",
)











COM_PROGRESS_LAYOUT = dbc.Row(
    [
     
       dbc.Col( dbc.Label("Attended Date"),style={'textAlign':'left'}),
      
       dbc.Col(
                  dcc.DatePickerSingle(
                                          id='my-date-picker-single-A',
                                          min_date_allowed=date(2010, 8, 5),
                                          max_date_allowed=date(2040, 9, 19),
                                          initial_visible_month=date(2022, 1, 1),
                                          date=date(2040, 1, 1),
                                          display_format='DD-MM-YYYY',
                                          
                                          clearable=True,
                                 ) ,
              ),
    ],className="mb-3",style={"margin-left":"-8rem","margin-right":"3rem"}
)


COM_COMPLETED_LAYOUT = dbc.Row(
    [
    
       dbc.Col( dbc.Label("Completed Date"),style={'textAlign':'left'}),
      
       dbc.Col(
                  dcc.DatePickerSingle(
                                          id='my-date-picker-single-C',
                                          min_date_allowed=date(2010, 8, 5),
                                          max_date_allowed=date(2040, 9, 19),
                                          initial_visible_month=date(2022, 1, 1),
                                          date=date(2040, 1, 1),
                                          display_format='DD-MM-YYYY',
                                          
                                          clearable=True,
                                 ) ,
              ),
       
       
       
    ],className="mb-3",
    
)





COM_INITIAL_LAYOUT = dbc.Row(
    [
    dbc.Row([
        dbc.Col( dbc.Label("Creation Date/Issue Date"),md=12,sm=12,xs=12,lg=2,style={'textAlign':'left'}),
       
        dbc.Col(
                   dcc.DatePickerSingle(
                                           id='my-date-picker-single',
                                           min_date_allowed=date(2010, 8, 5),
                                           max_date_allowed=date.today(),
                                          
                                           initial_visible_month=date.today() - timedelta(days=7),
                                           display_format='DD-MM-YYYY',
                                           date=date.today() - timedelta(days=7),
                                  ) ,md=12,sm=12,xs=12,lg=2,
               ),
        
        
        #COM_PROGRESS_LAYOUT,
        #COM_COMPLETED_LAYOUT
        
       
        
        
        
        ])
    
  
         
         
      
             
                  
    ],className="mb-3",
)





com_EVENT_CLICK=dbc.Col([
    
    
    dbc.Button(
                            "Update", id="com_Update_Btn", className="me-2", n_clicks=0,style={"margin-right":"0.5rem","margin-top":"0.5rem",}
                            ),
    
    
                           dbc.Button(
                                "Reset", id="com_Reset_Btn", className="me-2", n_clicks=0,style={"margin-top":"0.5rem",}
                                ),
                           
                           html.Span(id="UpdateRow_Info", style={"verticalAlign": "middle"}),
    ],className="d-grid gap-10 d-md-flex justify-content-md-end",)





Complain_Card = dbc.Card(
    [
        dbc.Row( [
                dbc.Col(
                    dbc.CardImg(src="/static/images/Waiting.png", top=True,style=ComCardImageStyle,),width=1,
                    ),
        
                dbc.Col(
                    dbc.CardHeader("Register New Complaints for Members",style=ComCardStyle),
                    ),
                ],style={'background-color':'#e65563',"margin-left":"0.5rem","margin-right":"0.5rem","margin-top": "0.5rem",}),
        
        
        dbc.CardBody(
                    [
                        Com_dropdown_PART,
                        Com_dropdown_SERIAL,
                        Com_dropdown_DESC,
                        Com_dropdown_problem,
                        text_input_problem,
                        COM_ASSIGN_LAYOUT,

                        #COM_INITIAL_LAYOUT,
                     
                        com_EVENT_CLICK,
                    ]
                    ),
    ],
    


)




COMPLAIN_MGMT_LAYOUT=dbc.Container(Complain_Card)


value="Single Member Entry Page->New Only"
HTML_SUMMARY_LIST_SINGLE_REPAIR_PAGE=html.Details(id="1"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,style={'background-color':'#fefffe'},
                                           
                  
                             
                                ),
                             
                             html.Div([
                                 
                                html.Hr(), 
                                COMPLAIN_MGMT_LAYOUT,
                                
                                 
                                 ]),
                     ],
                          open=True)






Com_dropdown_PART_MULTI =dbc.Row(
    [
     dbc.Row([
         
         
         dbc.Col(
                         dbc.Label("Select Part Number", html_for="dropdown"),width=3
            ),
         dbc.Col(
                     dcc.Dropdown(
                                 id="Com_dropdown_MULTI",
                                 options=[{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],
                                 value= PART_NUMBER_DATABASE_df['partnumber'],
                                 multi=True,
                                 )
            ),
         
         
         
         
         ])
    
    ],
    className="mb-3",
    
)

dfTable=PART_NUMBER_DATABASE_df.head(1)


COMPLAIN_MGMT_LAYOUT_TABLE=html.Div([
    dash_table.DataTable(
        id='table-dropdown',
  
        columns=[
            {'id': 'partnumber', 'name': 'Part Number','editable': False},
            {'id': 'serialnumber', 'name': 'Serial Number'},
            {'id': 'description', 'name': 'Part Desc','editable': False},
            {'id': 'problemlist', 'name': 'Problem Desc', 'presentation': 'dropdown'},
           {'id': 'problemdetails', 'name': 'Desc Details'},
            
            {'id': 'assignto', 'name': 'Assign To', 'presentation': 'dropdown'},
            {'id': 'taskstatus', 'name': 'Status   .','presentation': 'dropdown'},
            {'id': 'complaintdate', 'name': 'Complaint date (dd-mm-yyyy)',},
            #{'id': 'Attendeddate', 'name': 'Attended date','editable': False},
            #{'id': 'Closeddate', 'name': 'Closed date','editable': False},
            
          
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
        data=dfTable.to_dict('records'),
        css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
          

       
        editable=True,
        row_deletable=True,
        
        
        dropdown={          
                            'partnumber':
                            {
                                
                                
                                'options': [
                                    
                                    
                                    {'label': i, 'value': i} for i in PART_NUMBER_DATABASE_df['partnumber'].unique()
                                ]
                            },
                            
                            'problemlist': {
                                'options': [
                                    {'label': i, 'value': i} for i in PROBLEM_LIST
                                ]
                                
                            },
                            
                            
                            'assignto': {
                                 'options': [
                                    {'label': i, 'value': i}
                                    for i in PROBLEM_TAKER
                                ]
                            },
                            
                            'taskstatus': {
                                 'options': [
                                    {'label': i, 'value': i}
                                    for i in ["InProgress","Not Completed"]
                                ]
                            },
                       },
            
            
            
     
            
            
    ),
    
    dbc.Col( [
    # dbc.Button('Add Row', id='com-editing-rows-button', n_clicks=0,style={   "margin-left": "0.1rem",
    #    "margin-right":"0.1rem","margin-top":"0.5rem"}),
    
    dbc.Button(
                "Update Record", id="UpdateDatabase_Table", className="me-4", n_clicks=0,style={"margin-top":"0.5rem"},
                ),
    ]),
    
    html.Span(id="com-example-output-m", style={"verticalAlign": "middle"}),
    
    html.Div(id='table-dropdown-container')
])



    
    
    
    
value="Multi Members Complain Page->New Only"
HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE=html.Details(id="1"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             
                             html.Div([
                                 
                                html.Hr(), 
                                Com_dropdown_PART_MULTI,
                                html.Hr(), 
                                COMPLAIN_MGMT_LAYOUT_TABLE,
                                html.Div(id='div_History')
                               
                                 
                                 ]),
                     ],
                          open=False)





dfFileHISTORY=LoadStatusInfoPageHistory()
#print(dfFileHISTORY)




    

Com_dropdown_PART_MULTI_VIEW=dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select District from List", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_VIEW",
                             options=[{'label':name, 'value':name} for name in LoadStatusInfoPageHistory()['partnumber'].unique()],
                             value= PART_NUMBER_DATABASE_df['partnumber'],
                             multi=True,
                             ),
        ),
    ],
    className="mb-3",
    
)

COMPLAIN_MGMT_LAYOUT_TABLE_VIEW=html.Div([
    dash_table.DataTable(
        id='table-dropdown-view',
        
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
       
      
       
      style_data_conditional=(
                              [
                                       {
                                           'if': {
                                               'filter_query': '{taskstatus} =InProgress',
                                               'column_id': 'taskstatus',
                                           },
                                           'backgroundColor': 'dodgerblue',
                                           'color': 'white',
                                           
                   
                                       },
                                       
                                        {                   
                                       
                                       'if': {
                                           'filter_query': '{taskstatus} =Completed',
                                           'column_id': 'taskstatus',
                                       },
                                       'backgroundColor': 'green',
                                       'color': 'white'
                                       },
                                        
                                        {                   
                                       
                                       'if': {
                                           'filter_query': '{taskstatus} eq "Not Completed"',
                                           'column_id': 'taskstatus',
                                       },
                                       'backgroundColor': 'red',
                                       'color': 'white'
                                       },
                   
                            ]
              
                        
                            ),

     
      ),
    

])

value="Complain Status Page for Members"
HTML_SUMMARY_ITEM_VIEW_PAGE=html.Details(id="1"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             
                             html.Div([
                                 
                                html.Hr(), 
                                Com_dropdown_PART_MULTI_VIEW,
                                html.Hr(), 
                                COMPLAIN_MGMT_LAYOUT_TABLE_VIEW,
                                html.Div(id='div_History_View')
                               
                                 
                                 ]),
                     ],
                          open=False)



def updateDateBaseHistory():
            key='key_id'
            CSV_FILENAME="RepairLifeCycleEntry_HISTORY.csv"
            TABLE_NAME="COMPLAIN_MANAGEMENT_HISTORY"
            createTableSchema='''(key_id VARCHAR(500) PRIMARY KEY,key VARCHAR(255) ,partnumber VARCHAR(255),serialnumber VARCHAR(255),description VARCHAR(1000),problemlist VARCHAR(255),
                    problemdetails VARCHAR(255),assignto VARCHAR(255),transferredto VARCHAR(255),taskstatus VARCHAR(255),complaintdate VARCHAR(255),attendeddate VARCHAR(255),closeddate VARCHAR(255));'''
            CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)
            pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
          
            
          
            #print(dfTable)
            dfHis= Read_DataBase("COMPLAIN_MANAGEMENT_HISTORY")
            dfHis.to_csv(pathT,index=False)
    
    
def updateDateBaseLatest():
    
    
            key='key'
            CSV_FILENAME="RepairLifeCycleEntry.csv"
            TABLE_NAME="COMPLAIN_MANAGEMENT"
            createTableSchema='''(key VARCHAR(255) PRIMARY KEY,partnumber VARCHAR(255),serialnumber VARCHAR(255),description VARCHAR(1000),problemlist VARCHAR(255),
            problemdetails VARCHAR(255),assignto VARCHAR(255),taskstatus VARCHAR(255),complaintdate VARCHAR(255),attendeddate VARCHAR(255),closeddate VARCHAR(255));'''
            CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)

            pathT='./CSV/RepairLifeCycleEntry.csv'
            dfHis= Read_DataBase("COMPLAIN_MANAGEMENT")
            dfHis.to_csv(pathT,index=False)



def Update_DataBaseByStatusCSV(dataFrame=None):
    
            key='key'
            TABLE_NAME="COMPLAIN_MANAGEMENT"
            Update_DataBaseByStatus(dataFrame,TABLE_NAME,key)

           




@app.callback(
    [
     
     Output('Part_Com_dropdown', 'options'),
     Output('Com_dropdown_MULTI', 'options'),
     
     Output('Com_dropdown_MULTI_VIEW', 'options'),
   

     
     ],
    Input('Part_Com_dropdown', 'value')
)
def update_output(value):
    
    PART_NUMBER_DATABASE_df=Read_DataBase("PART_NUMBER_DATABASE")
    df=PART_NUMBER_DATABASE_df[ PART_NUMBER_DATABASE_df['partnumber']==value]
    
    
    
    #print(PART_NUMBER_DATABASE_df)
    return [{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],[{'label':name, 'value':name} for name in PART_NUMBER_DATABASE_df['partnumber']],[{'label':name, 'value':name} for name in LoadStatusInfoPageHistory()['partnumber'].unique()]
   


@app.callback(
    Output('table-dropdown', 'data'),
    [Input('Com_dropdown_MULTI', 'value'),
     
     ],
    State('table-dropdown', 'data'),
 )
def add_row(value,data):
    
    
    dfold=pd.DataFrame.from_dict(data)
    if len(dfold.index)>0:
    
        mask=dfold['partnumber'].isin(list(value))
        
        dfold=dfold[mask]
    
        #print(dfold)

    #print('Com_dropdown_MULTI')
    
    df=PART_NUMBER_DATABASE_df
    
    mask=df['partnumber'].isin(list(value))
    
    df=df[mask]
    
    df.reset_index(inplace=True,drop=True)

    
    dfAll=pd.DataFrame()
    
    
    if len(dfold.index)>0:
        
        dfAll = pd.merge(dfold, df, on=['partnumber','description'], how='outer')
    
    else:
        dfAll=df
       
    
    #print(dfAll)
    
    return dfAll.to_dict('records')

RepairEntryNewColumns=['key','partnumber','serialnumber','description','problemlist','problemdetails','assignto','taskstatus','complaintdate','attendeddate','closeddate']

@app.callback(
    Output('div_History', 'children'),
    [Input('UpdateDatabase_Table', 'n_clicks'),
     
     ],
    State('table-dropdown', 'data'),
 )
def InsertData_row(n_clicks,data):
    
    import os
    import numpy as np

    path='./CSV/RepairLifeCycleEntry.csv'
    if os.path.isfile(path):
        try:
            dfFile = pd.read_csv(path)
        except :
            dfFile = pd.DataFrame()
        if len(dfFile.index)<=0:
            if n_clicks>0:
                
                return "Data Base Updated not Created"
            
        else:
                if n_clicks>0:
                    
                    dfTable=pd.DataFrame.from_dict(data)
                    
                    #print(dfTable)
                    
                    if 'serialnumber' not in dfTable:
                        
                        return("Serial Number is blank")
                    
                                                
                    if 'problemlist' not in dfTable:   
                
                        return("Problem Desc is blank") 
                    else:
                    
                           if dfTable['problemlist'].isnull().any():
                               return("some other problemlist is blank") 
                    
                    if 'problemdetails' not in dfTable:
                        return("problemdetails remark is blank") 
                    else:
                    
                           if dfTable['problemdetails'].isnull().any():
                               return("some other problemdetails remark is blank") 
                           

                    
                    if 'assignto' not in dfTable :
                        
                        return("Assignee is blank") 
                    else:
                       if dfTable['assignto'].isnull().any():
                           return("Some other Assignee is blank") 
                        
                    if 'taskstatus' not in dfTable:  
                        
                        return("Task Status is blank") 
                    else:
                       if dfTable['taskstatus'].isnull().any():
                           return("Some other Task Status is blank") 

                    if 'complaintdate' not in dfTable:  
                        
                    
                        return("Complaint Date is blank") 
                    elif  dfTable['complaintdate'].isnull().any():
                         
                               return("Some other complaint Date is blank") 
                    else:
                        res=[ReturnDateisValidorNot(i) for i in dfTable['complaintdate']]
                        #print(res)
                        if False in res:
                            return("Complaintdate Date is wrong format ,right is (dd-mm-YYYY)")

                        
                        
                    
                    dfTable['key']=dfTable['partnumber']+"-"+dfTable['serialnumber']
                    
                    dfTable['attendeddate']=''
                    
                    dfTable['closeddate']=''
 
                    
                   
                    #print(dfTable['problemdetails'])
                    
                    # shift column 'Name' to first position
                    key_column = dfTable.pop('key')
  
                    # insert column using insert(position,column_name,
                    # first_column) function
                    dfTable.insert(0, 'key', key_column)
                    
                    
                    
                    
                    
                    dfTable=dfTable[RepairEntryNewColumns]
                    
                    #print("Multi User Entry",dfTable)
                    
                    
                    path='./CSV/RepairLifeCycleEntry.csv'
                    
                    dfFile = pd.read_csv(path)
                    
                    mask=dfFile['key'].isin(list(dfTable['key']))
                    
                    maskSum=np.sum(mask)
                   
                    #print(mask)
                    
                    if  maskSum>0:
                        return("Complain Alrealy Registered Updated for row number {}".format(list(mask.index)))

                    
                    else:
                       dfTable.to_csv(path,mode='a', header=False, index=False)
                       updateDateBaseLatest()
                
                   
                       pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
                       key_column=dfTable['key']+"_HIS_"+dfTable.index.astype(str)
                       
                       dfTable.insert(0, 'key_id', key_column)
                       dfTable.insert(8,'transferredto','')
                       dfTable.to_csv(pathT,mode='a', header=False, index=False)
                       
                       updateDateBaseHistory()
                       return("Complain Created with Id {}".format(dfTable['key']))
    
    else:
        return "File not Updated"
   


@app.callback(
    Output('UpdateRow_Info', 'children'),
   
    [Input('com_Update_Btn', 'n_clicks'),
     
     ],
    
    
      
      State('Part_Com_dropdown','value'),
      State('PART_SERAIL_NUMBER','value'),
      State('Part-Description-container','value'),
      
      State('Com_problem_dropdown','value'),
      State('textarea-example','value'),
      
      
      
      State('Com_Assign_dropdown','value'),
      State('Com_Status_dropdown','value'),
      
      State('my-date-picker-single','date'),
      State('my-date-picker-single','date-A'),
      State('my-date-picker-single','date-C'),
   
     
   
 )



def UpdateData_row(n_clicksData,PartNumberValue,PartSerialValue,
                   PartDescValue,ProblemList,ProblemDescriptionDetails,
                   AssigneeName,TaskStatus,InitialDate,AttendedDate,
                   CompletedDate):
    
 import os
 import numpy as np

 
 if n_clicksData>0:
    
     path='./CSV/RepairLifeCycleEntry.csv'
     
     
     if os.path.exists(path):
         
             try:
                 dfFile = pd.read_csv(path)
             
             except :
                 dfFile = pd.DataFrame()
                 
             #print(PartNumberValue,len(PartSerialValue),PartSerialValue)

         
             
             if PartNumberValue is None:
                 return("Part Number is blank!")
                 
                 
             elif PartSerialValue is None:
                 
                 return("Serial Number is blank!")
             
             elif PartDescValue is None:
                    
                    return("Part Description is Blank!")   
             
                    
             else:
                 
                 Serial=list(PartSerialValue)
                 #print(Serial)
                 res = any(' ' in ele for ele in Serial)
                 print(res)
                 # if res:
                 #     return("Serial Number is blank with white spaces!")
        
                     
                         
           
             if ProblemList is None:
                       
                       return("Problem List is blank") 
                   
             elif AssigneeName is None:
                 return("Assignee  is blank!") 
             
                
             elif TaskStatus is None:
                 return("TaskStatus  is blank!") 
        
             elif InitialDate is None :
                 return("InitialDate is blank") 
                
               
         
             dfFileT = pd.DataFrame(index=np.arange(1),columns=np.arange(11))
             dfFileT.columns=RepairEntryNewColumns
             
             dfFileT['key']=PartNumberValue+"-"+PartSerialValue
             
             #print(dfFileT['key'])
             
             mask=dfFile['key'].isin(list(dfFileT['key']))
             mask=np.sum(mask)
             #print(mask)
             
             if  mask>0:
                 return("Complain Alrealy Registered Updated")
             

             
           
             else:
                 #RepairEntryNewColumns=['key','partnumber','serialnumber','partdescription','problemlist','problemdetails','assignto','Complaintdate','Attendeddate','Closeddate']
                 dfFileT['partnumber']=PartNumberValue
                 dfFileT['serialnumber']=PartSerialValue
                 dfFileT['description']=PartDescValue
                 
                 #print('PartDescValue',PartDescValue)
                 dfFileT['problemlist']=ProblemList
                 dfFileT['problemdetails']=ProblemDescriptionDetails
                 
                 dfFileT['assignto']=AssigneeName
                 dfFileT['taskstatus']=TaskStatus
                 
                 start_date_object = date.fromisoformat(InitialDate)
                 
                 start_date_string = start_date_object.strftime('%d-%m-%Y')
                 
                 dfFileT['complaintdate']=start_date_string
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
             
                 return("Complain Created with Id {}".format(dfFileT['key']))
             
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
         
         return("File Does Not Exist Now Created")
         
     
@app.callback(
      Output('table-dropdown-view', 'data'),
      Output('table-dropdown-view', 'columns'),
      [Input('Com_dropdown_MULTI_VIEW', 'value'),
       
       ],
     
   )
def Status_row_Page_Table(value):
      
     dfFile=LoadStatusInfoPageHistory()
     #dfFile=Read_DataBase('COMPLAIN_MANAGEMENT_HISTORY')
     
     #print(dfFile,value)
     if len(dfFile.index)>0:
         
              
                if  value is  None:      
                    
                    return dfFile.to_dict('records'), [{"name": i, "id": i} for i in dfFile.columns]
                
                if  value == ['']:      
                    
                    return dfFile.to_dict('records'), [{"name": i, "id": i} for i in dfFile.columns]
                
                if  value ==[]:      
                    
                    return dfFile.to_dict('records'), [{"name": i, "id": i} for i in dfFile.columns]
        
                else:      
                    mask=dfFile['partnumber'].isin(list(value))
                
                    dfFile=dfFile[mask]
                
                    dfFile.reset_index(inplace=True,drop=True)
                    return dfFile.to_dict('records'), [{"name": i, "id": i} for i in dfFile.columns]

         
       
     else:
          print("Status NOT PATH")



#   NEW LAYOUT


NEWCOMPLAINLAYOUT=html.Div(
    
    [
     
    
     HTML_SUMMARY_LIST_SINGLE_REPAIR_PAGE,
     
     
     html.Hr(), 
     HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE,
   
     
     ]
    
    
    )




#INPROGRESS LAYOUT
dfFileLatest=LoadStatusInfoPageLatest()

dfFileLatest_Completed=dfFileLatest[dfFileLatest['taskstatus']=='Completed']

dfFileLatest_InProgress=dfFileLatest[dfFileLatest['taskstatus']=='InProgress']
dfFileLatest_InProgress.insert(7, 'transferredto', '')


Com_dropdown_PART_MULTI_INPROGRESS =dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select Part Number", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_INPROGRESS",
                             options=[{'label':name, 'value':name} for name in LoadStatusInfoPageLatest()['partnumber'].unique()],
                             
                             multi=True,
                             ),
        ),
     
     
    ],
    className="mb-3",
    
)

COMPLAIN_MGMT_LAYOUT_TABLE_INPROGRESS=html.Div([
    dash_table.DataTable(
        id='table-dropdown-INPROGRESS',
  
        columns=[
            {'id': 'key', 'name': 'key','editable': False},
            {'id': 'partnumber', 'name': 'Part Number','editable': False},
            {'id': 'serialnumber', 'name': 'Serial Number','editable': False},
            {'id': 'description', 'name': 'Part Desc','editable': False},
            {'id': 'problemlist', 'name': 'Problem Desc', 'presentation': 'dropdown'},
           {'id': 'problemdetails', 'name': 'Desc Details'},
            
            {'id': 'assignto', 'name': 'Current Assignee','editable': False},
            {'id': 'transferredto', 'name': 'New Assignee', 'presentation': 'dropdown'},
            {'id': 'taskstatus', 'name': 'Status   .','presentation': 'dropdown'},
            {'id': 'complaintdate', 'name': 'Complaint date (dd-mm-yyyy)','editable': False},
            {'id': 'attendeddate', 'name': 'Attended date','editable': True},
            {'id': 'closeddate', 'name': 'Closed date','editable': True},
            
          
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
        data=dfFileLatest_InProgress.to_dict('records'),
        style_table={
                'minHeight': '16rem',
                'overflowX': 'scroll',
                'width': '100%',
                'minWidth': '100%',
            },
        style_data_conditional=(
                                [
                                    
                                   
                                    
                                    
                                    
                                    
                                    
                                            {
                                                'if': {
                                                   
                                                    'column_id': 'key',
                                                },
                                                'backgroundColor': '#86878a',
                                                'color': 'white',
                                                'font-weight':'bold',
                                                'text-decoration': 'underline',
                                                'cursor':'pointer',
                                                
                        
                                            },
                                            
                                    
                                    
                                         
                     
                              ]
                
                          
                              ),
       
        css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
          
     
       
        editable=True,
        row_deletable=True,
        filter_action='native',
     
        
        
        dropdown={          
                          
                            
                            'problemlist': {
                                'options': [
                                    {'label': i, 'value': i} for i in PROBLEM_LIST
                                ]
                            },
                            
                            
                            'transferredto': {
                                 'options': [
                                    {'label': i, 'value': i}
                                    for i in PROBLEM_TAKER
                                ]
                            },
                            
                            'taskstatus': {
                                 'options': [
                                    {'label': i, 'value': i}
                                    for i in ["InProgress","Not Completed","Completed"]
                                ]
                            },
                       },
            
            
        
    ),
    
    dbc.Col( [
    # dbc.Button('Add Row', id='com-editing-rows-button', n_clicks=0,style={   "margin-left": "0.1rem",
    #    "margin-right":"0.1rem","margin-top":"0.5rem"}),
    
    dbc.Button(
                "Update Record", id="UpdateDatabase_Table_INPROGRESS", className="me-4", n_clicks=0,style={"margin-top":"0.5rem"},
                ),
    ]),
    
    html.Span(id="com-example-output-m-INPROGRESS", style={"verticalAlign": "middle"}),
    
    html.Div(id='table-dropdown-container-INPROGRESS'),
    
    html.Div(id='click-data-Inprogress'),
])







value="Multi Members Complain Page->InProgress Only"
HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE_INPROGRESS=html.Details(id="2"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             
                             html.Div([
                                 
                                html.Hr(), 
                                Com_dropdown_PART_MULTI_INPROGRESS,
                                html.Hr(), 
                                COMPLAIN_MGMT_LAYOUT_TABLE_INPROGRESS,
                                html.Div(id='div_History_INPROGRESS')
                               
                                 
                                 ]),
                     ],
                          open=True)



#Not Completed Page Layout



dfFileLatest_NOTCOMPLETE=dfFileLatest[dfFileLatest['taskstatus']=='Not Completed']
dfFileLatest_NOTCOMPLETE.insert(7, 'transferredto', '')


Com_dropdown_PART_MULTI_NOTCOMPLETE =dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select Part Number", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_NOTCOMPLETE",
                             options=[{'label':name, 'value':name} for name in LoadStatusInfoPageLatest()['partnumber'].unique()],
                          
                             multi=True,
                             
                             ),
        ),
     
     
    ],
    className="mb-3",
    
)

COMPLAIN_MGMT_LAYOUT_TABLE_NOTCOMPLETE=html.Div([
    dash_table.DataTable(
        id='table-dropdown-NOTCOMPLETE',
  
        columns=[
            {'id': 'key', 'name': 'key','editable': False},
            {'id': 'partnumber', 'name': 'Part Number','editable': False},
            {'id': 'serialnumber', 'name': 'Serial Number','editable': False},
            {'id': 'description', 'name': 'Part Desc','editable': False},
            {'id': 'problemlist', 'name': 'Problem Desc', 'presentation': 'dropdown'},
           {'id': 'problemdetails', 'name': 'Desc Details'},
            
            {'id': 'assignto', 'name': 'Current Assignee','editable': False},
            {'id': 'transferredto', 'name': 'New Assignee', 'presentation': 'dropdown'},
            {'id': 'taskstatus', 'name': 'Status   .','presentation': 'dropdown'},
            {'id': 'complaintdate', 'name': 'Complaint date (dd-mm-yyyy)','editable': False},
            {'id': 'attendeddate', 'name': 'Attended date','editable': True},
            {'id': 'closeddate', 'name': 'Closed date','editable': True},
            
          
        ],
        
        page_current= 0,
        page_size= 10,
        data=dfFileLatest_NOTCOMPLETE.to_dict('records'),
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
        
       
        css=[ {"selector": ".Select-menu-outer", "rule": 'display : block !important'} ],
          

       
        editable=True,
        row_deletable=True,
        
        
        dropdown={          
                          
                            
                            'problemlist': {
                                'options': [
                                    {'label': i, 'value': i} for i in PROBLEM_LIST
                                ]
                            },
                            
                            
                            'transferredto': {
                                 'options': [
                                    {'label': i, 'value': i}
                                    for i in PROBLEM_TAKER
                                ]
                            },
                            
                            'taskstatus': {
                                 'options': [
                                    {'label': i, 'value': i}
                                    for i in ["InProgress","Not Completed","Completed"]
                                ]
                            },
                       },
            
            
        
    ),
    
    dbc.Col( [
    # dbc.Button('Add Row', id='com-editing-rows-button', n_clicks=0,style={   "margin-left": "0.1rem",
    #    "margin-right":"0.1rem","margin-top":"0.5rem"}),
    
    dbc.Button(
                "Update Record", id="UpdateDatabase_Table_NOTCOMPLETE", className="me-4", n_clicks=0,style={"margin-top":"0.5rem"},
                ),
    ]),
    
    html.Span(id="com-example-output-m-NOTCOMPLETE", style={"verticalAlign": "middle"}),
    
    html.Div(id='table-dropdown-container-NOTCOMPLETE')
])







value="Multi Members Complain Page->Not Complete Only"
HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE_NOTCOMPLETE=html.Details(id="NOT"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             html.Hr(), 
                             html.Div([
                                 
                            
                                Com_dropdown_PART_MULTI_NOTCOMPLETE,
                                html.Hr(), 
                                COMPLAIN_MGMT_LAYOUT_TABLE_NOTCOMPLETE,
                                html.Div(id='div_History_NOTCOMPLETE')
                               
                                 
                                 ]),
                     ],
                          open=True)








# Complted Page Layout

Com_dropdown_PART_MULTI_COMPLETED =dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select Part Number", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_COMPLETED",
                             options=[{'label':name, 'value':name} for name in LoadStatusInfoPageLatest()['partnumber'].unique()],
                          
                             multi=True,
                             
                             ),
        ),
     
     
    ],
    className="mb-3",
    
)

COMPLAIN_MGMT_LAYOUT_TABLE_COMPLETED=html.Div([
    dash_table.DataTable(
        id='table-dropdown-view-completed',
        data=LoadStatusInfoPageLatest_Query('taskstatus','Completed').to_dict('records'),
        columns=[{"name": i, "id": i} for i in LoadStatusInfoPageLatest().columns],
        
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
     
      ),
    

])



value="Completed Multi Members Complain Page"
HTML_SUMMARY_ITEM_COMPLETED_PAGE=html.Details(id="COM"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             html.Hr(), 
                             html.Div([
                                 
                                Com_dropdown_PART_MULTI_COMPLETED,
                                html.Hr(),
                                COMPLAIN_MGMT_LAYOUT_TABLE_COMPLETED,
                             
                               
                                 
                                 ]),
                     ],
                          open=True)



# OVERALL or Detailed Pagae


Com_dropdown_PART_MULTI_OVERALL=dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select Part Number", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_OVERALL",
                             options=[{'label':name, 'value':name} for name in LoadStatusInfoPageLatest()['partnumber'].unique()],
                          
                             multi=True,
                             
                             ),
        ),
     
     
    ],
    className="mb-3",
    
)

overAllColName=["Key",'Part Number','Serial Number','Part Des','Problem List','Details','Asignee','Status','Complaint Date','Attended Date','Closed Date']

COMPLAIN_MGMT_LAYOUT_TABLE_OVERALL=html.Div([
    dash_table.DataTable(
        id='table-dropdown-view-overall',
        data=LoadStatusInfoPageLatest().to_dict('records'),
        columns=[{"name": i, "id": j} for i,j in zip(overAllColName,LoadStatusInfoPageLatest().columns) ],
        
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
       
       style_data_conditional=(
                               [
                                   
                                   
                                   {
                                       "if": {"state": "active"},
                                       "backgroundColor": "rgba(150, 180, 225, 1)",
                                       "border": "1px solid blue",
                                   },
                                   {
                                       "if": {"state": "selected"},
                                       "backgroundColor": "rgba(0, 116, 217, 1)",
                                       "border": "1px solid blue",
                                   },
                                   
                                   
                                   
                                   
                                   
                                           {
                                               'if': {
                                                  
                                                   'column_id': 'key',
                                               },
                                               'backgroundColor': '#86878a',
                                               'color': 'white',
                                               'text-decoration': 'underline'
                                               
                       
                                           },
                                           
                                   
                                   
                                        {
                                            'if': {
                                                'filter_query': '{taskstatus} =InProgress',
                                                'column_id': 'taskstatus',
                                            },
                                            'backgroundColor': 'dodgerblue',
                                            'color': 'white',
                                            
                    
                                        },
                                        
                                         {                   
                                        
                                        'if': {
                                            'filter_query': '{taskstatus} =Completed',
                                            'column_id': 'taskstatus',
                                        },
                                        'backgroundColor': '#42cc46',
                                        'color': 'white'
                                        },
                                         
                                         {                   
                                        
                                        'if': {
                                            'filter_query': '{taskstatus} eq "Not Completed"',
                                            'column_id': 'taskstatus',
                                        },
                                        'backgroundColor': 'red',
                                        'color': 'white'
                                        },
                    
                             ]
               
                         
                             ),
       
       
       
       
       export_format="csv",
       page_current= 0,
       page_size= 10,
       
   

     
      ),
    html.Div(id='click-data'),
    html.Div(id='click-data1'),
    

])



value="Overall or Detailed Multi Members Complain Page"
HTML_SUMMARY_ITEM_OVERALL_PAGE=html.Details(id="overall"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             html.Hr(), 
                             html.Div([
                                 
                                 Com_dropdown_PART_MULTI_OVERALL,
                                  html.Hr(),
                                COMPLAIN_MGMT_LAYOUT_TABLE_OVERALL,
                             
                               
                                 
                                 ]),
                     ],
                          open=True)



# ANALYSIS PAGE


AnaLysisInfo=["Overall","Overview"]

Com_dropdown_PART_MULTI_ANALYSIS=dbc.Row(
    [
     dbc.Col(
                     dbc.Label("Select Part Number", html_for="dropdown"),width=3,
        ),
     dbc.Col(
                 dcc.Dropdown(
                             id="Com_dropdown_MULTI_ANALYSIS",
                             options=[{'label':name, 'value':name} for name in AnaLysisInfo],
                          
                           
                             
                             ),
        ),
     
     
    ],
    className="mb-3",
    
)

value="Analysis View Page"
HTML_SUMMARY_ITEM_ANALYSIS_PAGE=html.Details(id="Analysis"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                  
                             
                                ),
                             html.Hr(), 
                             html.Div([
                                 
                                 Com_dropdown_PART_MULTI_ANALYSIS,
                                 html.Hr(),
                                 html.Div(id="ANALYSIS-OUTPUT")
                               
                             
                               
                                 
                                 ]),
                     ],
                          open=True)



RepairPageTab_cardLayout = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="New Complain Page", tab_id="New" ,label_style={"color": "#000f08"}),
                    
                    dbc.Tab(label="InProgress Complain Page", tab_id="InProgress",label_style={"color": "#000f08"}),
                    
                    dbc.Tab(label="Not Completed Complain Page", tab_id="NotCompleted",label_style={"color": "#000f08"}),
                    
                    dbc.Tab(label="Completed Complain Page", tab_id="Completed" ,label_style={"color": "#000f08"}),
                    dbc.Tab(label="Overall/Details Page", tab_id="Overall" ,label_style={"color": "#000f08"}),
                    dbc.Tab(label="Analysis View Page", tab_id="Analysis" ,label_style={"color": "#000f08"}),
                ],
                id="Repair-card-tabs",
                active_tab="New",
                style={'color':'green',"background-color": "#8f96c2", 'fontWeight': 'bold',}
            )
        ),
        dbc.CardBody(html.Div(id="Repair-card-content", className="card-text")),
    ]
)






layout = html.Div([

        html.H4('Members Detail page',style={'textAlign': 'center','color':'black',"background-color": "#f0f3f7",}),
        html.Hr(),
        cards,
        
        RepairPageTab_cardLayout,
        
        html.Hr(),
        HTML_SUMMARY_ITEM_VIEW_PAGE


], style={"margin-left":"2.1rem","margin-right":"1.1rem",})





@app.callback(
    Output("Repair-card-content", "children"), 
    [Input("Repair-card-tabs", "active_tab")]
)
def Repair_Page_tab_content(active_tab):
    if active_tab == "New":
       return NEWCOMPLAINLAYOUT
    elif active_tab == "InProgress":
       return HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE_INPROGRESS
    elif active_tab == "NotCompleted":
       return HTML_SUMMARY_LIST_MULTI_REPAIR_PAGE_NOTCOMPLETE
    
    elif active_tab == "Completed":
        return HTML_SUMMARY_ITEM_COMPLETED_PAGE
    
    elif active_tab == "Overall":
        return HTML_SUMMARY_ITEM_OVERALL_PAGE
   
    elif active_tab == "Analysis":
        return HTML_SUMMARY_ITEM_ANALYSIS_PAGE   
   
    
    return html.Div("This shouldn't ever be displayed...")



@app.callback(
    Output('com-example-output-m-INPROGRESS', 'children'),
    [Input('UpdateDatabase_Table_INPROGRESS', 'n_clicks'),
     
     ],
    State('table-dropdown-INPROGRESS', 'data'),
 )
def InsertData_row_InProgress(n_clicks,data):
    
    import os
    import numpy as np
    path='./CSV/RepairLifeCycleEntry.csv'
    if os.path.isfile(path):
        try:
            dfFile = pd.read_csv(path)
        except :
            dfFile = pd.DataFrame()
        if len(dfFile.index)>0:
            dfFileInProgress=dfFile[dfFile['taskstatus']=='InProgress']
           
            if n_clicks>0:
                dfTable=pd.DataFrame.from_dict(data)
                #print(dfTable)
                
               
                
                dfTable['assigntoTemp']= dfTable['assignto']
                
              
                if dfTable['partnumber'] is None or dfTable['serialnumber'] is None:
                      
                      return("Part Number or Serial Number is blank")
                  
                   
                elif dfTable['problemlist'] is None:
                          
                          return("Problem List is blank") 
                      
                elif dfTable['assignto'] is None or dfTable['taskstatus'] is None:
                      
                      return("Assignee or Task Status is blank") 
                
                
                
                
                for i in range(0,len(dfTable['assignto'])):
                    
     
          
                        if dfTable['transferredto'].iloc[i]==dfTable['assignto'].iloc[i]:
                            return ("New Assignee can not be same like old one at row {}".format(i))
                        
                     
                        if len(dfTable['transferredto'].iloc[i])>0:
                            dfTable['assignto'].iloc[i]=dfTable['transferredto'].iloc[i]
                     
                            
                            
  
                
                if 'attendeddate' not in dfTable.columns or dfTable['attendeddate'].isnull().any():
                    
                
                    return("All or Some Other Attended Date is blank")
                else:
                    
                    res=[ReturnDateisValidorNot(i) for i in dfTable['attendeddate']]
                    #print(res)
                    if False in res:
                        return("Attended Date is wrong format ,right is (dd-mm-YYYY)")
                
                    res=[TwoDataValidation(i,j) for i,j in zip(dfTable['complaintdate'],dfTable['attendeddate']) ]
                    #print(res)
                    if False in res:
                        return("Attended Date is can not be older than Complaint Date")
                    
                    res=[TwoDataValidation(i,datetime.today().strftime("%d-%m-%Y")) for i in (dfTable['attendeddate']) ]
                    #print(res)
                    if False in res:
                        return("Future Date can not be put")
              
                
                    
                if 'taskstatus' not in dfTable.columns or dfTable['taskstatus'].isnull().any():
                    
                    return("TaskStatus  is blank")
                
                check=np.where(dfTable['taskstatus']=='Completed', 1, 0)  # -1 is broadcast
                
                for i in range(0,len(check)):
                    if check[i]==1:
                        
                       if dfTable['closeddate'].iloc[i] is None:
                        # if 'Closeddate' not in dfTable.columns or dfTable['Closeddate'].iloc[i].isnull():
                           
                          return("Closed Date is blank")
                        
                       else:
                            res=ReturnDateisValidorNot(dfTable['closeddate'].iloc[i]) 
                            if res==False:
                                return("Closeddate Date is wrong format ,right is (dd-mm-YYYY)")
                            
                            res=[TwoDataValidation(i,datetime.today().strftime("%d-%m-%Y")) for i in (dfTable['closeddate']) ]
                            #print(res)
                            if False in res:
                                return("Future Date can not be put")
                    
                    
                    else:
                        dfTable['closeddate'].iloc[i]=''
                        
                
                 
                key_Assign = dfTable.pop('assigntoTemp')
                df=dfTable 
                

                df=pd.concat([dfFile,df]).drop_duplicates(['key'],keep='last') 
                
               
                
                df.drop('transferredto', axis=1, inplace=True)
                #df.drop('Key_ID', axis=1, inplace=True)
               
                #df.drop(labels='Locations', axis=1)
                df.to_csv(path,index=False)
                Update_DataBaseByStatusCSV(dfTable)
                
              
                
                pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
                dfHis=dfTable.copy()
                dfHis=dfTable[df.columns]
  
                
                key_column=dfTable['key']+"_HIS_"+str(len(LoadStatusInfoPageHistory()))
                if 'key_id' not in dfTable.columns:
                    dfHis.insert(0, 'key_id', key_column)
              
                dfHis["assignto"]=key_Assign
                
                dfHis.insert(8, 'transferredto', dfTable['transferredto'])
                dfHis.to_csv(pathT,mode='a', header=False, index=False)
                updateDateBaseHistory()
                
                
                return "Data Base Updated {} Time".format(n_clicks)
            
            
  



#//

@app.callback(
      Output('table-dropdown-INPROGRESS', 'data'),
      Output('table-dropdown-INPROGRESS', 'columns'),
      Output('Com_dropdown_MULTI_INPROGRESS', 'options'),

      
      [Input('Com_dropdown_MULTI_INPROGRESS', 'value'),
       
       ],
      State('table-dropdown-INPROGRESS', 'columns'),

     
   )
def Update_InProgress_Page_Table(value,columns):
      
     dfFileLatest_InProgress=LoadStatusInfoPageLatest()
     dfFileLatest_InProgress=dfFileLatest_InProgress[dfFileLatest_InProgress['taskstatus']=='InProgress']
     
     #print("table-dropdown-INPROGRESS",dfFileLatest_InProgress['description'])
     dfFileLatest_InProgress.insert(7,'transferredto','')
     
     options=[{'label':name, 'value':name} for name in dfFileLatest_InProgress['partnumber'].unique()]
     
     #print(options)
     
     #print("table-dropdown-INPROGRESS",dfFileLatest_InProgress.columns)
         
    # dfFileLatest_InProgress.insert(7, 'transferredto', '')
     if len(dfFileLatest_InProgress.index)>0:
         
         
                 if  value is  None:      
                     
                     return dfFileLatest_InProgress.to_dict('records'),columns,options
                 if  value == ['']:      
                     
                     return dfFileLatest_InProgress.to_dict('records'),columns,options
                 if  value ==[]:      
                     
                     return dfFileLatest_InProgress.to_dict('records'),columns,options
         
                 else:      
                      mask=dfFileLatest_InProgress['partnumber'].isin(list(value))
                  
                      dfFileLatest_InProgress=dfFileLatest_InProgress[mask]
                  
                      dfFileLatest_InProgress.reset_index(inplace=True,drop=True)
                      #dfFileLatest_InProgress.drop('key', axis=1, inplace=True)
                      
                      #dfFileLatest_InProgress.drop('transferredto', axis=1, inplace=True)
                      
                      #print(dfFileLatest_InProgress) 
                      return dfFileLatest_InProgress.to_dict('records'),columns,options
           
                     
                  
       
     else:
          #print("NOT PATH")
          return pd.DataFrame().to_dict('records'),columns,options
      
        
      
        
      
        
      
        
      
@app.callback(
    Output('com-example-output-m-NOTCOMPLETE', 'children'),
    [Input('UpdateDatabase_Table_NOTCOMPLETE', 'n_clicks'),
     
     ],
    State('table-dropdown-NOTCOMPLETE', 'data'),
 )
def InsertData_row_NotCompleted(n_clicks,data):
    
    import os
    import numpy as np
    path='./CSV/RepairLifeCycleEntry.csv'
    if os.path.isfile(path):
        try:
            dfFile = pd.read_csv(path)
        except :
            dfFile = pd.DataFrame()
        if len(dfFile.index)>0:
            dfFileInProgress=dfFile[dfFile['taskstatus']=='Not Completed']
           
            if n_clicks>0:
                dfTable=pd.DataFrame.from_dict(data)
                
                dfTable['assigntoTemp']= dfTable['assignto']
                
              
                if dfTable['partnumber'] is None or dfTable['serialnumber'] is None:
                      
                      return("Part Number or Serial Number is blank")
                  
                   
                elif dfTable['problemlist'] is None:
                          
                          return("Problem List is blank") 
                      
                elif dfTable['assignto'] is None or dfTable['taskstatus'] is None:
                      
                      return("Assignee or Task Status is blank") 
                
                
                
                
                for i in range(0,len(dfTable['assignto'])):
                    
     
          
                        if dfTable['transferredto'].iloc[i]==dfTable['assignto'].iloc[i]:
                            return ("New Assignee can not be same like old one at row {}".format(i))
                        
                     
                        if len(dfTable['transferredto'].iloc[i])>0:
                            dfTable['assignto'].iloc[i]=dfTable['transferredto'].iloc[i]
                     
                            
                            
  
                
                if 'attendeddate' not in dfTable.columns or dfTable['attendeddate'].isnull().any():
                    
                
                    return("All or Some Other Attended Date is blank")
                else:
                    
                    res=[ReturnDateisValidorNot(i) for i in dfTable['attendeddate']]
                    #print(res)
                    if False in res:
                        return("Attended Date is wrong format ,right is (dd-mm-YYYY)")
                
                    res=[TwoDataValidation(i,j) for i,j in zip(dfTable['complaintdate'],dfTable['attendeddate']) ]
                    #print(res)
                    if False in res:
                        return("Attended Date is can not be older than Complaint Date")
                    
                    res=[TwoDataValidation(i,datetime.today().strftime("%d-%m-%Y")) for i in (dfTable['attendeddate']) ]
                    #print(res)
                    if False in res:
                        return("Future Date can not be put")
              
                
                    
                if 'taskstatus' not in dfTable.columns or dfTable['taskstatus'].isnull().any():
                    
                    return("TaskStatus  is blank")
                
                check=np.where(dfTable['taskstatus']=='Completed', 1, 0)  # -1 is broadcast
                
                for i in range(0,len(check)):
                    if check[i]==1:
                        
                       if dfTable['closeddate'].iloc[i] is None:
                        # if 'Closeddate' not in dfTable.columns or dfTable['Closeddate'].iloc[i].isnull():
                           
                          return("Closed Date is blank")
                        
                       else:
                            res=ReturnDateisValidorNot(dfTable['closeddate'].iloc[i]) 
                            if res==False:
                                return("Closeddate Date is wrong format ,right is (dd-mm-YYYY)")
                            
                            res=[TwoDataValidation(i,datetime.today().strftime("%d-%m-%Y")) for i in (dfTable['closeddate']) ]
                            #print(res)
                            if False in res:
                                return("Future Date can not be put")
                    
                    else:
                        dfTable['closeddate'].iloc[i]=''
                        
                
                 
                key_Assign = dfTable.pop('assigntoTemp')
                df=dfTable
                df=pd.concat([dfFile,df]).drop_duplicates(['key'],keep='last') 
                df.drop('transferredto', axis=1, inplace=True)
                df.to_csv(path,index=False)
                Update_DataBaseByStatusCSV(dfTable)
               
                

                
                pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
                dfHis=dfTable.copy()
                dfHis=dfTable[df.columns]
  
                
                key_column=dfTable['key']+"_HIS_"+str(len(LoadStatusInfoPageHistory()))
                if 'key_id' not in dfTable.columns:
                    dfHis.insert(0, 'key_id', key_column)
              
                dfHis["assignto"]=key_Assign
                
                dfHis.insert(8, 'transferredto', dfTable['transferredto'])
                dfHis.to_csv(pathT,mode='a', header=False, index=False)
                #print(dfTable)
                updateDateBaseHistory()
                return "Data Base Updated {} Time".format(n_clicks)
            
    

@app.callback(
      Output('table-dropdown-NOTCOMPLETE', 'data'),
      Output('table-dropdown-NOTCOMPLETE', 'columns'), 
      Output('Com_dropdown_MULTI_NOTCOMPLETE', 'options'),

      
      [Input('Com_dropdown_MULTI_NOTCOMPLETE', 'value'),
       
       ],
      State('table-dropdown-NOTCOMPLETE', 'columns'),

     
   )
def Update_dfFileLatest_NOTCOMPLETE_Page_Table(value,columns):
      
     dfFileLatest_NOTCOMPLETE=LoadStatusInfoPageLatest()
     dfFileLatest_NOTCOMPLETE=dfFileLatest_NOTCOMPLETE[dfFileLatest_NOTCOMPLETE['taskstatus']=='Not Completed']
     dfFileLatest_NOTCOMPLETE.insert(7,'transferredto','')
     options=[{'label':name, 'value':name} for name in dfFileLatest_NOTCOMPLETE['partnumber'].unique()]
     

     #print(dfFileLatest_NOTCOMPLETE)
         
    # dfFileLatest_InProgress.insert(7, 'transferredto', '')
     if len(dfFileLatest_NOTCOMPLETE.index)>0:
         
                  if  value is  None:      
                      
                      return dfFileLatest_NOTCOMPLETE.to_dict('records'),columns,options
                  if  value == ['']:      
                      
                      return dfFileLatest_NOTCOMPLETE.to_dict('records'),columns,options
                  if  value ==[]:      
                      
                      return dfFileLatest_NOTCOMPLETE.to_dict('records'),columns,options
                  else:
                      mask=dfFileLatest_NOTCOMPLETE['partnumber'].isin(list(value))
                  
                      dfFileLatest_NOTCOMPLETE=dfFileLatest_NOTCOMPLETE[mask]
                  
                      dfFileLatest_NOTCOMPLETE.reset_index(inplace=True,drop=True)
                      #dfFileLatest_InProgress.drop('key', axis=1, inplace=True)
                      
                      #dfFileLatest_InProgress.drop('transferredto', axis=1, inplace=True)
                      
                 
                      return dfFileLatest_NOTCOMPLETE.to_dict('records'),columns,options
   
                          
                  
       
     else:
          print("NOT PATH COMPLETE")
          return pd.DataFrame().to_dict('records'),columns,options

@app.callback(
      Output('table-dropdown-view-completed', 'data'),
      Output('table-dropdown-view-completed', 'columns'),
      Output('Com_dropdown_MULTI_COMPLETED', 'options'),

      
      [Input('Com_dropdown_MULTI_COMPLETED', 'value'),
       
       ],
      State('table-dropdown-view-completed', 'columns'),

     
   )
def Update_dfFileLatest_COMPLETED_Page_Table(value,columns):
      
     dfFileLatest_COMPLETED=LoadStatusInfoPageLatest()
     dfFileLatest_COMPLETED=dfFileLatest_COMPLETED[dfFileLatest_COMPLETED['taskstatus']=='Completed']
     dfFileLatest_COMPLETED.insert(7,'transferredto','')
     options=[{'label':name, 'value':name} for name in dfFileLatest_COMPLETED['partnumber'].unique()]
     

     #print(dfFileLatest_NOTCOMPLETE)
         
    # dfFileLatest_InProgress.insert(7, 'transferredto', '')
     if len(dfFileLatest_COMPLETED.index)>0:
         
                  if  value is  None:      
                      
                      return dfFileLatest_COMPLETED.to_dict('records'),columns,options
                  if  value == ['']:      
                      
                      return dfFileLatest_COMPLETED.to_dict('records'),columns,options
                  if  value ==[]:      
                      
                      return dfFileLatest_COMPLETED.to_dict('records'),columns,options
                  else:
                      mask=dfFileLatest_COMPLETED['partnumber'].isin(list(value))
                  
                      dfFileLatest_COMPLETED=dfFileLatest_COMPLETED[mask]
                  
                      dfFileLatest_COMPLETED.reset_index(inplace=True,drop=True)
                      #dfFileLatest_InProgress.drop('key', axis=1, inplace=True)
                      
                      #dfFileLatest_InProgress.drop('transferredto', axis=1, inplace=True)
                      
                 
                      return dfFileLatest_COMPLETED.to_dict('records'),columns,options
   
                          
                  
       
     else:
          print("NOT PATH COMPLETE")
          return pd.DataFrame().to_dict('records'),columns,options

@app.callback(
      Output('table-dropdown-view-overall', 'data'),
      Output('table-dropdown-view-overall', 'columns'),     

      
      [Input('Com_dropdown_MULTI_OVERALL', 'value'),
       
       ],
      State('table-dropdown-view-overall', 'columns'),

     
   )
def Update_dfFileLatest_OVERALL_Page_Table(value,columns):
      
     dfFileLatest_COMPLETED=LoadStatusInfoPageLatest()

     

     #print(dfFileLatest_NOTCOMPLETE)
         
    # dfFileLatest_InProgress.insert(7, 'transferredto', '')
     if len(dfFileLatest_COMPLETED.index)>0:
         
                  if  value is  None:      
                      
                      return dfFileLatest_COMPLETED.to_dict('records'),columns
                  if  value == ['']:      
                      
                      return dfFileLatest_COMPLETED.to_dict('records'),columns
                  if  value ==[]:      
                      
                      return dfFileLatest_COMPLETED.to_dict('records'),columns
                  else:
                      mask=dfFileLatest_COMPLETED['partnumber'].isin(list(value))
                  
                      dfFileLatest_COMPLETED=dfFileLatest_COMPLETED[mask]
                  
                      dfFileLatest_COMPLETED.reset_index(inplace=True,drop=True)
                      #dfFileLatest_InProgress.drop('key', axis=1, inplace=True)
                      
                      #dfFileLatest_InProgress.drop('transferredto', axis=1, inplace=True)
                      
                 
                      return dfFileLatest_COMPLETED.to_dict('records'),columns
   
                          
                  
       
     else:
          print("NOT PATH COMPLETE")
          return pd.DataFrame().to_dict('records'),columns






# define callback        
@app.callback(
    Output('click-data', 'children'),
    Output('click-data1','children'),
    [Input('table-dropdown-view-overall', 'active_cell')],
     # (A) pass table as data input to get current value from active cell "coordinates"
    [State('table-dropdown-view-overall', 'data')],
    [State('table-dropdown-view-overall', 'page_current')],
    [State('table-dropdown-view-overall', 'page_size')],
    
)
def display_overall_data(active_cell, table_data,page_current,page_size):
    

    print(page_current,page_size)
    if active_cell:
        cell = json.dumps(active_cell, indent=2)    
        row = active_cell['row']
        col = active_cell['column_id']
        row=row+page_current*page_size
        value = table_data[row][col]
        out = '%s\n%s' % (cell, value)
        df=pd.DataFrame()
        dfD=pd.DataFrame()
        
        if value is not None:
        
            df=pd.DataFrame(LoadStatusInfoPageHistory())
    
            df['key']=df['key'].str.upper()
            dfFiltered=df[df['key']==value.upper()]
            
            
    
            dfD=pd.DataFrame(LoadStatusInfoPageLatest())
            dfD['key']=dfD['key'].str.upper()
            dfFiltereddfD=dfD[dfD['key']==value.upper()]
        
        
     
        
            RepairEntryNewColumns=['key','partnumber','serialnumber','description','problemlist','problemdetails','assignto','taskstatus','complaintdate','attendeddate','closeddate']
            Columns=['key','District Name','Name','description','problem list','problem details','assignto','status','complaint date','attended date','closed date']
            
            DialogLayout=""
            
            if len(dfFiltereddfD)>0 and col=='key':
         
            
                rows=[]
                for x,y in zip(RepairEntryNewColumns,Columns):
                    #print("dfFiltered[x]",dfFiltered[x],x)
                    if x!="key":
                      row= html.Tr([html.Th(str(y).upper()), html.Th(dfFiltereddfD[x])])
                      rows.append(row)
                   
        
                table_body = [html.Tbody(rows)]
                table = dbc.Table(table_body, bordered=True)
                
         
            
         
                DialogLayout=dbc.Modal(
                        [
                            dbc.ModalHeader(dbc.Row
                                            
                                            ([
                                                # dfFiltered['serialnumber'].str.upper()
                                
                                                    dbc.Label(dfFiltereddfD['serialnumber']+":" +" "+" Complaint Current Status",
                                                              
                                                              
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
         
            
         
            
         
            
            
            
            if col=='key' and len(dfFiltered)>0:
    
                print("display_overall_data",dfFiltered,value,col)
                print(dfFiltered[['complaintdate','attendeddate','closeddate']])
    
                import plotly.express as px
                import numpy as np
         
                dfFiltered['Complaintdate1'] =  pd.to_datetime(dfFiltered['complaintdate'], format='%d-%m-%Y')
                dfFiltered['Attendeddate1'] =  pd.to_datetime(dfFiltered['attendeddate'], format='%d-%m-%Y')
                dfFiltered['Closeddate1'] =  pd.to_datetime(dfFiltered['closeddate'], format='%d-%m-%Y')
                
                
               
                
                AssineeList=[str(i)+"->" for i in dfFiltered['assignto'].unique()]
                
    
             
                discrete_map_resource = { 'InProgress': 'blue', 'Not Completed': 'red', 'Completed': 'green',}
                dfT=pd.DataFrame() 
                for i in range(0,len(dfFiltered)):
                    if i==0:
                        df = pd.DataFrame(
                                [
                              
                                
                                dict(Task=dfFiltered['assignto'].iloc[i], Start=dfFiltered['Complaintdate1'].iloc[i], Finish=dfFiltered['Attendeddate1'].iloc[i], Status=dfFiltered['taskstatus'].iloc[i]),
                               
                    
                         
                                ]
                            )
                        df["id"] = df.index
                        dfT=pd.concat([dfT,df])
                        
                    if i==1:
                            df = pd.DataFrame(
                                    [
                                  
                                     
                                    dict(Task=dfFiltered['assignto'].iloc[i-1], Start=dfFiltered['Complaintdate1'].iloc[i], Finish=dfFiltered['Attendeddate1'].iloc[i], Status=dfFiltered['taskstatus'].iloc[i-1]),
                                 
                                    
                                    dict(Task=dfFiltered['assignto'].iloc[i], Start=dfFiltered['Attendeddate1'].iloc[i], Finish=dfFiltered['Closeddate1'].iloc[i], Status=dfFiltered['taskstatus'].iloc[i]),
                        
                             
                                    ]
                                )
                            df["id"] = df.index
                            dfT=pd.concat([dfT,df])  
                    if i>=2:
                            df = pd.DataFrame(
                                    [
                                  
                                     
                                    dict(Task=dfFiltered['assignto'].iloc[i-2], Start=dfFiltered['Complaintdate1'].iloc[i-2], Finish=dfFiltered['Attendeddate1'].iloc[i-2], Status=dfFiltered['taskstatus'].iloc[i-2]),
                                    
                                    dict(Task=dfFiltered['assignto'].iloc[i], Start=dfFiltered['Attendeddate1'].iloc[i-1], Finish=dfFiltered['Attendeddate1'].iloc[i], Status=dfFiltered['taskstatus'].iloc[i]),
                                    
                                    dict(Task=dfFiltered['assignto'].iloc[i-1], Start=dfFiltered['Attendeddate1'].iloc[i-1], Finish=dfFiltered['Closeddate1'].iloc[i-1], Status=dfFiltered['taskstatus'].iloc[i-1]),
                                    
                                    dict(Task=dfFiltered['assignto'].iloc[i], Start=dfFiltered['Attendeddate1'].iloc[i], Finish=dfFiltered['Closeddate1'].iloc[i], Status=dfFiltered['taskstatus'].iloc[i]),
                        
                             
                                    ]
                                )
                            df["id"] = df.index
                            dfT=pd.concat([dfT,df])          
                            
    
                fig = px.timeline(
                                 dfT, x_start="Start", x_end="Finish", y="Task", color="Status",color_discrete_map=discrete_map_resource, custom_data=["id"]
                                 )
                fig.update_yaxes(autorange="reversed")
           
                        
                LabelStyle={
        
                    #'height':'35px',
                    "font-size": "15px",
                    "color":"black",
                    'textAlign':"right",
                    'fontWeight': 'bold',
                   
                   
                    }
                
                LabelStyleInfo={
        
                    #'height':'35px',
                    "font-size": "13px",
                    "color":"black",
                    'textAlign':"left",
                    "margin-left":"0.4rem",
                    "margin-right":"1rem",
                  
                   
                    }
                LAYOUTINFO=html.Div(
                    
                    [
                        dbc.Card([
                        dbc.CardHeader("Over All Time Details of Member's Complain", className="card-title",style={'textAlign':'center',}),
                        dbc.CardBody([
                                   
                            
                      
                    
                                dbc.Row([
                                    
                                    dbc.Col([
                                    
                                    dbc.Label("Complaint ID:",style=LabelStyle),
                                    dbc.Label(dfFiltered['key'].unique(),style=LabelStyleInfo),
                                    
                                    dbc.Label("Problem Type:",style=LabelStyle),
                                    dbc.Label(dfFiltered['problemlist'].unique(),style=LabelStyleInfo),
                                    ]),
                                    
                                    
                                    dbc.Col([
                                        dbc.Label("Asignee List:",style=LabelStyle),
                                        dbc.Label(AssineeList,style=LabelStyleInfo),
                                        
                                        dbc.Label("Complaint Date:",style=LabelStyle),
                                        dbc.Label(dfFiltered['complaintdate'].unique(),style=LabelStyleInfo)
                                        
                                       ] ),
                                    
                                    dbc.Col([
                                        dbc.Label("Status:",style=LabelStyle),
                                        dbc.Label(dfFiltered['taskstatus'].iloc[-1],style=LabelStyleInfo),
                                        
                                        dbc.Label("Attended Date:",style=LabelStyle),
                                        dbc.Label(dfFiltered['attendeddate'].iloc[-1],style=LabelStyleInfo),
                                        
                                        dbc.Label("Completed Date:",style=LabelStyle),
                                        dbc.Label(dfFiltered['closeddate'].iloc[-1],style=LabelStyleInfo)
                                        
                                       ] ),
                                    
                                    
                                    ]),
                                dbc.Row([
                                    
                               
                                        
                                        dbc.Col(
                                            dbc.Label("",style=LabelStyle),
                                            ),
                                        
                                        
                                        dbc.Col([
                                            
                                            html.Hr(),
                                            dbc.Label("Progress:",style=LabelStyle),
                                            html.Div([dcc.Graph(id="timeline", figure=fig,style={'height':'14rem'})]),
                                     
                                            ]),
                                        
                                        dbc.Col(
                                            dbc.Label("",style=LabelStyle),
                                            ),
                                        
                                        
                                       
                                    ]),
                                
                                
                                
                                
                                
                                
                                ]),
                                
                        ]),
                              
                    
                    ],style={"margin-top":"4rem"})
                
                
                
                return LAYOUTINFO,DialogLayout
            else:
                 return '',''
        else:
              return '',''
              
            
    else:
        out = 'no cell selected'
    return out,''








@app.callback(

      Output('ANALYSIS-OUTPUT', 'children'),

      
      Input('Com_dropdown_MULTI_ANALYSIS', 'value'),
       
  
    
   )
def Update_ANALYSIS_Page_Table(value):
   
    data=pd.DataFrame()
    data=LoadStatusInfoPageLatest()

    data["Count"]=1


    
    #print(DataList)



    if value is None or value == [''] or value ==[]: 
         pivLayout=''
         listHeader=['partnumber', 'taskstatus', 'assignto','Count']
         dataNeeded=data[listHeader]
        
         DataList=dataNeeded.values.tolist()

         DataList.insert(0, listHeader)
         
         pivLayout=html.Div([dash_pivottable.PivotTable(
                                    data=DataList,

                                    cols=["taskstatus"],
                                    rows=["assignto"],
                                    vals=["Count"]
                                    ),
                                    ])
            
         return pivLayout
  

    if  value =='Overall':   
        
        dataNeeded=data
        dataNeeded["NoOfDays"]='0'
        
        # if 'Complaintdate' not in dataNeeded.columns or dataNeeded['Complaintdate'].isnull().any():
            
        
        #     return("All or Some Other Complaint Date is blank")
        
            
        for i in range(0,len(dataNeeded)):
                
                if dataNeeded["taskstatus"].iloc[i]=="Completed":
                    #print("OKKK!")
                    
                    dataNeeded.at[i,'NoOfDays']=GetNumberofDays(dataNeeded['complaintdate'].iloc[i],dataNeeded['closeddate'].iloc[i]).split(' ')[0]
                    #print(dataNeeded.at[i,'NoOfDays'])
                  
                    
                elif dataNeeded["taskstatus"].iloc[i]=="Not Completed" or dataNeeded["taskstatus"].iloc[i]=="InProgress":
                    
                    
                    if len(str(dataNeeded['attendeddate'].iloc[i]))>5:
                        print("OKKK")
                    
                        dataNeeded.at[i,'NoOfDays']=GetNumberofDays(dataNeeded['complaintdate'].iloc[i],str(dataNeeded['attendeddate'].iloc[i])).split(' ')[0]
                    
                
                
       # print(dataNeeded.columns)  
        #print(dataNeeded)
        DataG=dataNeeded.copy()
        dataNeeded.drop(['key','Count','problemdetails'], axis = 1,inplace=True)
        
        
        #print(DataG.dtypes)
        
        DataG['NoOfDays']=DataG['NoOfDays'].astype(int)
        
        
        DataG=DataG.sort_values(by=['NoOfDays'],ascending=False)
        
        # print(DataG.dtypes)
        # print(DataG)
        
        
        figG = px.bar(DataG, x='key', y='NoOfDays',color="partnumber",title="Time Taken for Problem Solving")
        
        GRAPH_G =dcc.Graph(id="timeline0", figure=figG),

        
        
        LAYOUT_TABLE_COMPLETED=dbc.Row(
            [
                dbc.Col(
                    
                   
                    
                    dash_table.DataTable(
                             id='overall',
                             data=dataNeeded.to_dict('records'),
                             columns=[{"name": i, "id": i} for i in dataNeeded.columns],
                             
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
                            
                            
                            style_data_conditional=[
                                                           {
                                                               'if': {
                                                                   'filter_query': '{taskstatus} eq "Completed"'
                                                               },
                                                               'backgroundColor': 'green',
                                                               'fontWeight': 'bold',
                                                                'color': 'white'
                                                           },
                                                           
                                                           {
                                                               'if': {
                                                                   'filter_query': '{taskstatus} eq "Not Completed"'
                                                               },
                                                               'backgroundColor': 'red',
                                                               'fontWeight': 'bold',
                                                                'color': 'white'
                                                           },
                                                           
                                                           {
                                                               'if': {
                                                                   'filter_query': '{taskstatus} eq "InProgress"'
                                                               },
                                                               'backgroundColor': 'yellow',
                                                               'fontWeight': 'bold',
                                                                'color': 'black'
                                                           },
                                                           
                                                           {
                                                               'if': {
                                                                   'filter_query': '{NoOfDays} >=10',
                                                                   'column_id': 'NoOfDays',
                                                               },
                                                               'backgroundColor': 'white',
                                                               'color': 'red',
                                                               
                                       
                                                           },
                                                           
                                                           {
                                                               'if': {
                                                                   'filter_query': '{NoOfDays} <10',
                                                                   'column_id': 'NoOfDays',
                                                               },
                                                               'backgroundColor': 'white',
                                                               'color': 'green',
                                                               
                                       
                                                           },
                                                           
                                                    ]
                            
                            
                            
                            
                            
                            
                          
                           ),
                    
                    
                    
                        ),
                
                
                dbc.Col(GRAPH_G),
                #dbc.Col(html.Div("One of three columns")),
            ]
        ),
        
        
        
        #print(DataG)
        
      
               
          
    
        
        return LAYOUT_TABLE_COMPLETED
    
    
    else: 
        
         # data['RepairTimes']= data.groupby('partnumber')['partnumber'].transform('size')
         # dataOverview=data.drop_duplicates(subset=['partnumber'])
         
         # fig = px.bar(dataOverview, x='partnumber', y='RepairTimes')
         
         
         data['Repaired']= data['partnumber'].map(data['partnumber'].value_counts())
         data=data.sort_values(by=['Repaired'],ascending=False)
         
         dataOverview=data.drop_duplicates(subset=['partnumber'])
         
       
         figP = px.bar(dataOverview, x='partnumber', y='Repaired',title='Most Problem came from  these District')
         
         data['Repaired']=1
         
         
         
         figS = px.bar(data, x='partnumber', y='Repaired',color="serialnumber",title="Most Problem came from  these District with Person Name")
         
         
         
         
         data=LoadStatusInfoPageHistory()
         
         dataOverview=data[data['taskstatus']=='Completed']
         dataOverview=dataOverview[['serialnumber','taskstatus','key']].value_counts(ascending=False).reset_index(name='count')
      
         
         #print(dataOverview)
         
         
         
         figST = px.bar(dataOverview, x='key', y='count',title='Person who visited Most',labels={"key":"Part Number-Serial Number","count":"No Of Times repair Completed"})
         
         
         
        
         om_dropdown_PART_MULTI_NOTCOMPLETE1 =dbc.Row(
            [
             dbc.Row([
                 dbc.Col(html.Div([dcc.Graph(id="timeline1", figure=figP)])),
                 
                 dbc.Col(html.Div([dcc.Graph(id="timeline2", figure=figS)])),
                 
                 ]),
             dbc.Row([
                 dbc.Col(html.Div([dcc.Graph(id="timeline3", figure=figST)])),
                 
                 dbc.Col(''),
                 
                 ]),
            
            
             
            ],
            className="mb-3",
            
         )
         
         
      
         # mask=dfFileLatest_InProgress['partnumber'].isin(list(value))
     
         # dfFileLatest_InProgress=dfFileLatest_InProgress[mask]
     
         # dfFileLatest_InProgress.reset_index(inplace=True,drop=True)
         # #dfFileLatest_InProgress.drop('key', axis=1, inplace=True)
         
         # #dfFileLatest_InProgress.drop('transferredto', axis=1, inplace=True)
         
         # #print(dfFileLatest_InProgress) 
         return om_dropdown_PART_MULTI_NOTCOMPLETE1
           
                     
                  
    
      
# define callback        
@app.callback(
    Output('click-data-Inprogress', 'children'),
    [Input('table-dropdown-INPROGRESS', 'active_cell')],
     # (A) pass table as data input to get current value from active cell "coordinates"
    [State('table-dropdown-INPROGRESS', 'data'),
   
    State('table-dropdown-INPROGRESS', 'page_current'),
    State('table-dropdown-INPROGRESS', 'page_size')],

    
)
def display_InProgress_data_dialog(active_cell, table_data,page_current,page_size):
    

 
    if active_cell:
        cell = json.dumps(active_cell, indent=2)
       
        row = active_cell['row']
        col = active_cell['column_id']
        row=row+page_current*page_size
    
    
    
    
        value = table_data[row][col]
        
        if value is not None:
            df=pd.DataFrame(LoadStatusInfoPageLatest())
            df['key']=df['key'].str.upper()
            dfFiltered=df[df['key']==value.upper()]
            
            
            print(dfFiltered)
            
            RepairEntryNewColumns=['key','partnumber','serialnumber','description','problemlist','problemdetails','assignto','taskstatus','complaintdate','attendeddate','closeddate']
            Columns=['key','District Name','Name','description','problem list','problem details','assignto','status','complaint date','attended date','closed date']
            
            
            if len(dfFiltered)>0 and col=='key':
         
            
                rows=[]
                for x,y in zip(RepairEntryNewColumns,Columns):
                    #print("dfFiltered[x]",dfFiltered[x],x)
                    if x!="key":
                      row= html.Tr([html.Th(str(y).upper()), html.Th(dfFiltered[x])])
                      rows.append(row)
                   
        
                table_body = [html.Tbody(rows)]
                table = dbc.Table(table_body, bordered=True)
                
                
                
                return dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.Row
                                                
                                                ([
                                    
                                                        dbc.Label(dfFiltered['serialnumber'].str.upper()+" "+" Complaint Details",
                                                                  
                                                                  
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

        else:
            return ""  
            
      
        
      

















