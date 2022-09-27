
# Dash packages
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app


###############################################################################
########### LANDING PAGE LAYOUT ###########
###############################################################################




# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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




FILE_NAME='partnumberdb.csv'




#Ajay Server
DATA_BASE="ddk9j9hbst548l"
DATA_USER="fdpleuqoxwwedw"
DATA_PASSWORD="19a8118e4b9bd63e8d54fd9bac7f2fd3fd5d9b996fbec7cf33f3314e16344574"
DATA_HOST="ec2-54-225-234-165.compute-1.amazonaws.com"
DATA_PORT="5432"


#ayan server
DATA_BASE="d2772itge7u7vu"
DATA_USER="gzfalyypqzwoif"
DATA_PASSWORD="288512b83c8db859600b174c860b288ed7d7b497fcd26dd353026d3fe1594b7d"
DATA_HOST="ec2-3-208-79-113.compute-1.amazonaws.com"
DATA_PORT="5432"


# DATA_BASE="MROT"
# DATA_USER="postgres"
# DATA_PASSWORD="bel123"
# DATA_HOST="192.168.0.20"
# DATA_PORT="5432"

# DATA_BASE="adsn"
# DATA_USER="postgres"
# DATA_PASSWORD=""
# DATA_HOST="192.168.0.150"
# DATA_PORT="5432"


def Update_DataBase(strFILE_NAME=None,TableName=None):
    """ query data from the vendors table """
    conn = None
    try:
        
        conn = psycopg2.connect(database=DATA_BASE, user = DATA_USER, password = DATA_PASSWORD, host = DATA_HOST, port = DATA_PORT)
        
    
        print("Database created successfully........")
        if conn:
            #print(conn)
            
            cur = conn.cursor()
            sql_query='''CREATE TABLE IF NOT EXISTS  "{}" '''.format( TableName)
            sql_query=sql_query+'''(partnumber VARCHAR(255) PRIMARY KEY,description VARCHAR(255));'''
            a=cur.execute(sql_query)
         
            cur.execute('''SELECT * from "PART_NUMBER_DATABASE";''')
            
          
            #cur.execute('''select * from "LoadStatusInfoPageHistory";''')
            #print("The number of parts: ", cur.rowcount)
            tupples = cur.fetchall()   
            
            col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
            col_names_str += "table_name = '{}';".format( TableName)
           
            cur.execute( col_names_str )
            
            col_names = ( cur.fetchall() )
            
            #print(col_names)
            #print(tupples)
            
            columnsAll=[]
            for tup in col_names:

            # append the col name string to the list
                columnsAll += [ tup[0] ]
                #print(tup[0])
            
            df = pd.DataFrame(tupples, columns=columnsAll)
            row = cur.fetchone()
         
            while row is not None:
                #print(row)
                row = cur.fetchone()   
           
            with open(strFILE_NAME, 'r') as f:
                  import csv
                  next(f)
                  spamreader=csv.reader(f)
                  df1=pd.DataFrame()
                  df1=[row for row in spamreader]
                  dfNew = pd.DataFrame (df1, columns =columnsAll)
        
                  mask=dfNew["partnumber"].str.upper().isin(df["partnumber"].str.upper())
                  mask=-mask
                  #print(mask)
                  #print(dfNew[mask])
                  dfNew=dfNew[mask]
                  dfNew["partnumber"]=dfNew["partnumber"].str.upper()
                  
                  dfNew = dfNew.drop_duplicates(subset = ["partnumber"])
                  strFILE_NAMET=strFILE_NAME.split('.csv')
                  #print(strFILE_NAMET)
                  
                  dfNew.to_csv(strFILE_NAMET[0]+"TEMP",index=False)
                  try:
                      with open(strFILE_NAMET[0]+"TEMP", 'r') as f:
                          next(f)
                          cur.copy_from(f, TableName, sep=',', columns=('partnumber', 'description'))
                    
                  except (Exception) as error:
                      print(error)
                      
               
        
            conn.commit()
          
            cur.close()
            conn.close()
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




def Read_DataBase(TableName=None):
    """ query data from the vendors table """
    print("Read Data Base Called")
    conn = None
    try:
        
        conn = psycopg2.connect(database=DATA_BASE, user = DATA_USER, password = DATA_PASSWORD, host = DATA_HOST, port = DATA_PORT)
        
        
        # conn.autocommit = True

        # #Creating a cursor object using the cursor() method
        # cursor = conn.cursor()

        # #Preparing query to create a database
        # sql = '''CREATE database ADSN''';

        # #Creating a database
        # cursor.execute(sql)
        # print("Database created successfully........")
        if conn:
           
            
            cur = conn.cursor()
        
            cur.execute('''select * from "{}";'''.format(TableName))
            #print("The number of parts: ", cur.rowcount)
            tupples = cur.fetchall()
            
            
            col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
            col_names_str += "table_name = '{}';".format( TableName)
           
            cur.execute( col_names_str )
            
            col_names = ( cur.fetchall() )
            
          
            
            columnsAll=[]
            for tup in col_names:

            # append the col name string to the list
                columnsAll += [ tup[0] ]
                #print(tup[0])
            
            df = pd.DataFrame(tupples, columns=columnsAll)
            
            #print(df)
            
           
        
            cur.close()
            conn.close()
            return df
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def execute_SQL_DF_query(df, table):
    
    conn = None
    try:
        conn = psycopg2.connect(database=DATA_BASE, user = DATA_USER, password = DATA_PASSWORD, host = DATA_HOST, port = DATA_PORT)

        if conn:
                cur = conn.cursor()
                """
                Using cursor.executemany() to insert the dataframe
                """
                print(df)
                df.to_csv('partnumberdbT.csv',index=False)
                try:
                   with open('partnumberdbT.csv', 'r') as f:
                       next(f)
                       cur.copy_from(f, "PART_NUMBER_DATABASE", sep=',', columns=('partnumber', 'description'))
                 
                except (Exception) as error:
                    
                   print(error)
                   return 1
                cur.close()
                conn.commit()
                conn.close()


    except (Exception, psycopg2.DatabaseError) as error:
        
       print(error)
       return 1
    finally:
       if conn is not None:
           conn.close()



def parse_data(contents, filename):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV or TXT file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        elif "txt" or "tsv" in filename:
            # Assume that the user upl, delimiter = r'\s+'oaded an excel file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter=r"\s+")
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df



def Check_parse_data_Status(df1,df2):
   
    col1=df1.columns
    col2=df2.columns
    status=col1==col2
    status=status*1
        
    print(col1)
    print(col2)
 
    if 0 in status:
        print(status)
        return False
    else:
        print(status)
        return True
        


Update_DataBase(FILE_NAME,"PART_NUMBER_DATABASE")
PART_NUMBER_DATABASE_df=Read_DataBase("PART_NUMBER_DATABASE")
print(PART_NUMBER_DATABASE_df)




CARD_HEADER_STYLE_2={'textAlign': 'center',"color":"white",
                   "font-size": "14px",
                   "padding": "0.01rem 0.01rem",
                                              
                   "font-family": "Segoe UI Semibold",
                   
                   "background-color": "#5b7f80"}


CARD_HEADER_STYLE_1={'textAlign': 'center',"color":"white",
                   "font-size": "14px",
                   
                                              
                   "font-family": "Segoe UI Semibold",
                   
                   "background-color": "#5c7f80"}


CARD_HEADER_STYLE_SUMMARY={'textAlign': 'left',"color":"white",
                   "font-size": "20px",
                   "margin-bottom": "10px",
                                              
                   "font-family": "Segoe UI Semibold",
                   "background-color": "#eeffFF"}


TABLE_STYLE_HEADER={
'backgroundColor': '#999eba',
'color': 'white',
'fontWeight': 'bold',
'textAlign': 'center',
#'border': '1px solid pink',
}



HTML_SUMMARY_STYLE={"color":"black",
       "margin-left": "0.1rem",
       "margin-right":"0.1rem",
       'textAlign': 'left',
       "font-size": "20px",
        "font-family": "Segoe UI Semibold",
       "background-color": "#fafcff",
     
  }


PART_NUMBER_DATABASE_TABLE_LAYOUT=dbc.Card(

                                dbc.CardBody([
                                    
                                               #html.H3("Part Number and Description Details", className="card-title",style=CARD_HEADER_STYLE_2),
                                                                         
                                                html.Hr(),
                                                dt.DataTable(
                                                    id='part_number_table', data=PART_NUMBER_DATABASE_df.to_dict('records'),
                                                    columns=[{"name": str(i).upper(), "id": i} for i in PART_NUMBER_DATABASE_df.columns],
                                                    
                                                    style_data={
                                                        'whiteSpace': 'normal',
                                                        'color': 'black',
                                                        'backgroundColor': '#f2f4f5',
                                                        #'border': '1px solid blue' 
                                                        },
                                                    
                                                    
                                                    style_header=TABLE_STYLE_HEADER,
                                                    
                                                  
                                                    tooltip_data=[
                                                                    {
                                                                        column: {'value': str(value), 'type': 'markdown'} for column, value in row.items()} 
                                                                     for row in PART_NUMBER_DATABASE_df.to_dict('records')
                                                                     
                                                                    
                                                                    
                                                                ],
                                                    
                                                    tooltip_duration=None,
                                                    
                                                    css=[{
                                                                    'selector': '.dash-table-tooltip',
                                                                    'rule': 'background-color: grey; font-family: monospace; color: white'
                                                        }],
                                                                                                                            
                                                    style_cell={'textAlign': 'left'}, # left align text in columns for readability
                                                    
                                                    fixed_columns={'headers': True, 'data': 1},
                                                    
                                                    style_table={'minWidth': '100%'},
                                                    
                                                    style_cell_conditional=[
                                                                            {'if': {'column_id': PART_NUMBER_DATABASE_df.columns[0]},'width': '20%'},
                                                                            {'if': {'column_id': PART_NUMBER_DATABASE_df.columns[1]},'width': '70%'},
                                                                            
                                                                            
                                                        ],
                                                    
                                                    style_data_conditional=[
                                                                                    {
                                                                                                'if': {'row_index': 'odd'},
                                                                                                'backgroundColor': '#f5f6f7',#'rgb(255, 255, 250)'
                                                                                        }
                                                                            ],
                                                    
                                                       
                                                                
                                                    filter_action="native",
                                                    sort_action="native",
                                                    sort_mode="multi",
                                                    column_selectable="single",
                                                    #row_selectable="multi",
                                                    #row_deletable=True,
                                                    selected_columns=[],
                                                    selected_rows=[],
                                                    page_action="native",
                                                    page_current= 0,
                                                    page_size= 10,
                                                                                                
                                                    ),
                                                
                                                
                                                
                                                #dbc.Alert(id='tbl_out'),
                                               
                                               ]),
                                               )





PART_NUMBER_DATABASE_BROWSE= html.Div(
                                                    [
                                                    dcc.Upload(
                                                                id="upload-data",
                                                                children=html.Div(["Drag and Drop or ", html.A("Browse Files for Updating the Data Base")]),
                                                                style={
                                                                   
                                                                    "height": "60px",
                                                                    "lineHeight": "60px",
                                                                    "borderWidth": "1px",
                                                                    "borderStyle": "dashed",
                                                                    "borderRadius": "5px",
                                                                    "textAlign": "center",
                                                                    "margin": "10px",
                                                                },
                                                                # Allow multiple files to be uploaded
                                                                multiple=True,
                                                                ),
                                                
                                                            html.Div(id="output-data-upload"),
                                                     ],
                                            id="partnumber_browse",
                                            style={
                                                            "margin-top": "1px",
                                                            'display':'none'
                                                 }
                                        )


PART_NUMBER_DATABASE_MANUALLY= html.Div(
                                                    [
                                                   
                                                        
                                                   dt.DataTable(
                                                           id='adding-rows-table',
                                                           columns=[{
                                                               'name': '{}'.format(str(i).upper()),
                                                               'id': '{}'.format(i),
                                                               'deletable': False,
                                                               'renamable': False
                                                               } for i in ["partnumber","description"]],
                                                           data=[
                                                             {'{}'.format(i): (j + (i-1)*5) for i in range(1, 1)}
                                                              for j in range(0)
                                                             ],
                                                           editable=True,
                                                           row_deletable=True,
                                                           
                                                
                                                           style_cell={'textAlign': 'left'}, # left align text in columns for readability
                       
                                                           
                                                           style_header=TABLE_STYLE_HEADER,
                                                           
  
                                             
                                                           
                                                           style_table={'minWidth': '100%'},
                                                           
                                                           style_cell_conditional=[
                                                                                   {'if': {'column_id': PART_NUMBER_DATABASE_df.columns[0]},'width': '30%'},
                                                                                   {'if': {'column_id': PART_NUMBER_DATABASE_df.columns[1]},'width': '60%'},
                                                                                   
                                                                                   
                                                               ],
                                                           
                                                     
                                                           ),
                                                   
                                                   
                                                        dbc.Col( [
                                                        dbc.Button('Add Row', id='editing-rows-button', n_clicks=0,style={   "margin-left": "0.1rem",
                                                           "margin-right":"0.1rem","margin-top":"0.5rem"}),
                                                        
                                                        dbc.Button(
                                                                    "Update DataBase", id="example-button-m", className="me-4", n_clicks=0,style={"margin-top":"0.5rem"},
                                                                    ),
                                                        ]),
                                                        
                                                        html.Span(id="example-output-m1", style={"verticalAlign": "middle"}),
                                                        
                                                   
                                                        
                                                   
                                                     ],
                                            id="partnumber_manually",
                                            style={
                                                            "margin-top": "1px",
                                                            'display':'none'
                                                 }
                                        )



USER_CHOICE_LAYOUT=dbc.Card(

                        dbc.CardBody([
                                    
                              #html.H4("Part Number and Description update choice", className="card-title",style=CARD_HEADER_STYLE_1),

                             

                              dcc.Dropdown(
                                          id='demo-dropdown',
                                          options=[{'label':name, 'value':name} for name in ["Manually","File"]],
                                          value='Manually'
                                          ),
                          
                                    ]),
                        )




value="District List and Description Details"
HTML_SUMMARY_LIST=html.Details(id="1"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                              style=HTML_SUMMARY_STYLE,
                             
                                ),
                             
                             html.Div([
                                 
                                PART_NUMBER_DATABASE_TABLE_LAYOUT,
                                 
                                 ]),
                     ],style=CARD_HEADER_STYLE_SUMMARY,
                          open=True)

value="District  List and Add choice"
HTML_SUMMARY_LIST_UPDATE=html.Details(id="1"+'{}'.format(value),
                children=[

                             html.Summary('{}'.format(value),id='{}'.format(value) ,
                                           
                              style=HTML_SUMMARY_STYLE,
                             
                                ),
                             
                             html.Div([
                                 
                                USER_CHOICE_LAYOUT,
                                PART_NUMBER_DATABASE_BROWSE,
                                PART_NUMBER_DATABASE_MANUALLY,
                                 
                                 ]),
                             ]
                    )





PART=html.Div([
                html.H4('Visitor Managament Layout',style={'textAlign': 'center','color':'black',"background-color": "#f0f3f7",}),
                HTML_SUMMARY_LIST,
                HTML_SUMMARY_LIST_UPDATE,
                
                          
             
],style={"background-color": "#ffffff",})



#948a8a

layout=PART
# layout = dbc.Container([

#         html.H2('Page 1 Layout'),
#         html.Hr(),
#         PART,


# ],style={"background-color": "#f5f5f5",}, className="mt-4")




@app.callback(
    Output("output-data-upload", "children"),
    [Input("upload-data", "contents"), 
     Input("upload-data", "filename")],
)


def update_table(contents, filename):
    table = html.Div()

    if contents:
        contents = contents[0]
        filename = filename[0]
        #print(contents)
        #print(filename)
        global dfAll
        dfAll = parse_data(contents, filename)
        
        CheckStatus=Check_parse_data_Status(PART_NUMBER_DATABASE_df,dfAll)
       # print(CheckStatus)
        
        if CheckStatus:
            table = html.Div(
                [
                    html.H5(filename),
                    dt.DataTable(
                        data=dfAll.to_dict("records"),
                        columns=[{"name": i, "id": i} for i in dfAll.columns],
                        page_action="native",
                        page_current= 0,
                        page_size= 5,
                    ),
                    #html.Hr(),
                    # html.Div("Raw Content"),
                    # html.Pre(
                    #     contents[0:200] + "...",
                    #     style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
                    # ),
                    
                    
                    dbc.Button(
                                "Update DataBase", id="example-button", className="me-4", n_clicks=0
                                ),
                    html.Span(id="example-output", style={"verticalAlign": "middle"}),
                    ],
       
                )
        else:
            table = html.Div([
                html.Label("Wrong file uploaded")
                ])
            
    return table






 
 
 # conn.autocommit = True

 # #Creating a cursor object using the cursor() method
 # cursor = conn.cursor()

 # #Preparing query to create a database
 # sql = '''CREATE database ADSN''';

 # #Creating a database
 # cursor.execute(sql)
 # print("Database created successfully........")





@app.callback(
   Output("example-output", "children"),
  
    
    [Input("example-button", "n_clicks")],
    State("part_number_table", "data")
)
def on_button_click(n,data):
    print("Click",n)
    if n ==0:
        print(n)
        return "Not clicked.",data
    elif n>0: 

        
        mask=dfAll["partnumber"].str.upper().isin(PART_NUMBER_DATABASE_df["partnumber"].str.upper())
        mask=-mask
        #print(mask)
        #print(dfNew[mask])
        dfAllTemp=dfAll[mask]
        dfAllTemp["partnumber"]=dfAllTemp["partnumber"].str.upper()
        #print(dfAllTemp)
        dfAllTemp = dfAllTemp.drop_duplicates(subset = ["partnumber"])
        #print(dfAllTemp)
        ret=execute_SQL_DF_query(dfAllTemp,"PART_NUMBER_DATABASE")
        if ret==1 or len(dfAllTemp.index)<=0:
            return "Not Updated"
        else :
            
            return "Updated Database."



@app.callback(
   [Output('partnumber_browse', 'style'),
    
   Output('partnumber_manually', 'style'), 
    
    ],
    Input('demo-dropdown', 'value')
)
def update_output(value):
    
     
    style1={
       "margin-top": "50px",
       'display':'none'
       }
    style2={
       "margin-top": "50px",
       'display':'none'
       }
    if value=="File":
      
        style1={
           "margin-top": "50px",
           'display':'block'
           }
    if value=="Manually":
       
         style2={
            "margin-top": "50px",
            'display':'block'
            }   
    return style1,style2


@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
    
    print(list(rows))
   
    
    
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows



@app.callback(
    [Output("example-output-m1", "children"),
    Output("part_number_table", "data")],

    Input("example-button-m", "n_clicks"),
    State('adding-rows-table', 'data'),
)
def on_button_click_manually(n,data):
    global PART_NUMBER_DATABASE_df
    if n is None:
        return "Not clicked.",Read_DataBase("PART_NUMBER_DATABASE").to_dict('records')
    elif n>0: 

        #print(data)
        df=pd.DataFrame.from_dict(data)
        
        df=df[df.columns[[1,0]]]
        
        #print(df)
        mask=df["partnumber"].str.upper().isin(PART_NUMBER_DATABASE_df["partnumber"].str.upper())
        mask=-mask
        #print(mask)
        #print(dfNew[mask])
        df=df[mask]
        df["partnumber"]=df["partnumber"].str.upper()
        #print(dfAllTemp)
        df = df.drop_duplicates(subset = ["partnumber"])
        nan_value = float("NaN")
        df.replace("", nan_value, inplace=True)
        df=df.dropna()
        df.columns=sorted(df.columns)
        #print(df)
        ret=execute_SQL_DF_query(df,"PART_NUMBER_DATABASE")
       
        if ret==1 or len(df.index)<=0:
            return "Not Updated",PART_NUMBER_DATABASE_df.to_dict('records')
        else :
            PART_NUMBER_DATABASE_df=Read_DataBase("PART_NUMBER_DATABASE")
            #print(PART_NUMBER_DATABASE_df)
            return f"Updated {n} times Database.",PART_NUMBER_DATABASE_df.to_dict('records')


    return "",Read_DataBase("PART_NUMBER_DATABASE").to_dict('records')    






def CommonCreateAndUpdate_DataBase(strFILE_NAME=None,TableName=None,createTableSchema=None,key=None):
    """ query data from the vendors table """
    
    print("While coming to update in the database")
    print("StrFileName",strFILE_NAME)
    print("TableName",TableName)
    print("createTableSchema",createTableSchema)
    print("key",key)
    outputData=False
    conn = None
    try:
        
        conn = psycopg2.connect(database=DATA_BASE, user = DATA_USER, password = DATA_PASSWORD, host = DATA_HOST, port = DATA_PORT)
        
    
        import os
       
        path='./CSV/'+strFILE_NAME
        print("CommonCreateAndUpdate_DataBase",path)
        if os.path.isfile(path):
            try:
                dfFile = pd.read_csv(path)
                print("Read dfFile",dfFile)
            except :
                dfFile = pd.DataFrame()
               
                
            if len(dfFile.index)>0:
                    print("Success")
            else:
                dfFile.loc[0] = 'INVALID'
           
              
                 
        else:
            dfFile=pd.DataFrame()
      
        print(dfFile['address'])
        
        if conn:
         
            
            cur = conn.cursor()
            sql_query='''CREATE TABLE IF NOT EXISTS  "{}" '''.format( TableName)
            sql_query=sql_query+createTableSchema;
            a=cur.execute(sql_query)
         
            cur.execute('''select * from "{}";'''.format( TableName))
            tupples = cur.fetchall()   
            
            col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
            col_names_str += "table_name = '{}';".format( TableName)
           
            cur.execute( col_names_str )
            col_names = ( cur.fetchall() )
            
            
            #print("col_names",col_names)
            columnsAll=[]
          
            for tup in col_names:
                
                #print("tuples",tup)

            # append the col name string to the list
                columnsAll += [ tup[0] ]
               
                #print(tup[0])
            
            df = pd.DataFrame(tupples, columns=columnsAll)
            
         
            row = cur.fetchone()
            
               
            #print(columnsAll,tuple(columnsAll),row)
            while row is not None:
                #print(row)
                row = cur.fetchone()   
           
            #print(" print conn",path,row)     
            with open(path, 'r',encoding='utf-8') as f:
                
              
                  import csv
                  next(f)
             
                  spamreader=csv.reader(f)
                  
                  #print("spamreader",spamreader)
                   
                  df1=pd.DataFrame()
                  df1=[row for row in spamreader]
                 
                  #print("df1",df1)
                  
                  dfNew = pd.DataFrame (df1, columns =columnsAll)
        
                  mask=dfNew[key].str.upper().isin(df[key].str.upper())
                  
                 # print("get first mask",mask)
                  mask=-mask
                  
                 # print("mask",mask)
                 # print("dfnewmask",dfNew[mask])
                 
                  dfNew=dfNew[mask]
                  
                  #print("HHH",dfNew)
                  
                  # it is correct upto this
                  #print("Key of dfnew", dfNew[key])
                  
                  dfNew[key]=dfNew[key].str.upper()
                  
                  
                 # print("Key of dfnew", dfNew[key],key)
                  # dfNew = dfNew.drop_duplicates(subset = [key])
                 # print("dfNew",dfNew)
                 
                  strFILE_NAMET=path.split('.csv')
                  
                  dfNew.to_csv(strFILE_NAMET[0]+"TEMP.csv",index=False)
          
                  try:
                      with open(strFILE_NAMET[0]+"TEMP.csv", 'r') as f:
                          next(f)
                          #print(f)
                          cur.copy_from(f, TableName, sep=',',
                                        columns=tuple(columnsAll))
                          
                          outputData=True
                        
                    
                  except (Exception) as error:
                      
                      print(error)
                     
                      
                   
                
        
            conn.commit()
          
            cur.close()
            conn.close()
            
            

            
    except (Exception, psycopg2.DatabaseError) as error:
        
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    print("outputDataoutputDataoutputDataoutputData",outputData)
    return outputData


def Update_DataBaseByStatus(dataFrame=None,TableName=None,key=None):
    """ query data from the vendors table """
    conn = None
    try:
        
        conn = psycopg2.connect(database=DATA_BASE, user = DATA_USER, password = DATA_PASSWORD, host = DATA_HOST, port = DATA_PORT)
    
     
        
        if conn:
         
            
            cur = conn.cursor()
         
            cur.execute('''select * from "{}";'''.format( TableName))
            tupples = cur.fetchall()   
            
            col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
            col_names_str += "table_name = '{}';".format( TableName)
           
            cur.execute( col_names_str )
            col_names = ( cur.fetchall() )
            
            columnsAll=[]
          
            for tup in col_names:

            # append the col name string to the list
                columnsAll += [ tup[0] ]
               
                #print(tup[0])
            
            dfDataBase = pd.DataFrame(tupples, columns=columnsAll)
            
            print(dfDataBase,dataFrame)
            
            # Update single record now
            
            for i in range(len(dataFrame)) :   
                
                print()
               
                qr='''update  "{}" '''.format( TableName)
                
                sql_update_query = qr+""" set problemdetails = %s where key = %s"""
                cur.execute(sql_update_query, (dataFrame['problemdetails'].iloc[i], dataFrame[key].iloc[i]))
                
                sql_update_query = qr+""" set assignto = %s where key = %s"""
                cur.execute(sql_update_query, (dataFrame['assignto'].iloc[i], dataFrame[key].iloc[i]))
                
                sql_update_query = qr+""" set taskstatus = %s where key = %s"""
                cur.execute(sql_update_query, (dataFrame['taskstatus'].iloc[i], dataFrame[key].iloc[i]))
          
              
               
                sql_update_query = qr+""" set attendeddate = %s where key = %s"""
                cur.execute(sql_update_query, (dataFrame['attendeddate'].iloc[i], dataFrame[key].iloc[i]))
               
                sql_update_query = qr+""" set closeddate = %s where key = %s"""
                cur.execute(sql_update_query, (dataFrame['closeddate'].iloc[i], dataFrame[key].iloc[i]))
                
               
            
             
  
            
            #DfUpdatd=dfFile[dfDataBase[COloumsToBeCheked].eq(dfFile)[COloumsToBeCheked].any(axis=1)]
         
            # row = cur.fetchone()
            
            # while row is not None:
                
            #     row = cur.fetchone()   
           
            
            #print("DfUpdatd Data Base",dfUpdated)   
            # with open(path, 'r') as f:
            #       import csv
            #       next(f)
            #       spamreader=csv.reader(f)
            #       df1=pd.DataFrame()
            #       df1=[row for row in spamreader]
            #       dfNew = pd.DataFrame (df1, columns =columnsAll)
                  
                 
        
            #       mask=dfNew[key].str.upper().isin(dfUpdated[key].str.upper())
            #       mask=-mask
            #        #print(mask)
            #        #print(dfNew[mask])
            #       dfNew=dfNew[mask]
            #       dfNew[key]=dfNew[key].str.upper()
                  
            #       dfNew = dfNew.drop_duplicates(subset = [key])
            #       strFILE_NAMET=path.split('.csv')
            #        #print(strFILE_NAMET)
                  
            #       dfNew.to_csv(strFILE_NAMET[0]+"INTEMP.csv"+strFILE_NAMET[1],index=False)
            #       try:
                       
            #              print(dfNew) 
            #       except (Exception) as error:
            #            print(error)
                      
                   
                
        
            conn.commit()
          
            cur.close()
            conn.close()
            

            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()





key='key'
CSV_FILENAME="RepairLifeCycleEntry.csv"
TABLE_NAME="COMPLAIN_MANAGEMENT"
createTableSchema='''(key VARCHAR(255) PRIMARY KEY,partnumber VARCHAR(255),serialnumber VARCHAR(255),description VARCHAR(1000),problemlist VARCHAR(255),
        problemdetails VARCHAR(255),assignto VARCHAR(255),taskstatus VARCHAR(255),complaintdate VARCHAR(255),attendeddate VARCHAR(255),closeddate VARCHAR(255));'''
#CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)

pathT='./CSV/RepairLifeCycleEntry.csv'
dfHis= Read_DataBase("COMPLAIN_MANAGEMENT")
dfHis.to_csv(pathT,index=False)



key='key_id'
CSV_FILENAME="RepairLifeCycleEntry_HISTORY.csv"
TABLE_NAME="COMPLAIN_MANAGEMENT_HISTORY"
createTableSchema='''(key_id VARCHAR(500) PRIMARY KEY,key VARCHAR(255) ,partnumber VARCHAR(255),serialnumber VARCHAR(255),description VARCHAR(1000),problemlist VARCHAR(255),
        problemdetails VARCHAR(255),assignto VARCHAR(255),transferredto VARCHAR(255),taskstatus VARCHAR(255),complaintdate VARCHAR(255),attendeddate VARCHAR(255),closeddate VARCHAR(255));'''
#CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)


pathT='./CSV/RepairLifeCycleEntry_HISTORY.csv'
dfHis= Read_DataBase("COMPLAIN_MANAGEMENT_HISTORY")
dfHis.to_csv(pathT,index=False)




key='key'
CSV_FILENAME="NewMembersList.csv"
TABLE_NAME="MEMBERS_USERS_MANAGEMENT"
createTableSchema='''(key VARCHAR(255) PRIMARY KEY,name VARCHAR(255),gender VARCHAR(255),address VARCHAR(1000),block VARCHAR(255),
        pincode VARCHAR(255),statename VARCHAR(255),districtname VARCHAR(255),
        assemblyname VARCHAR(255),contactno VARCHAR(255),emailid VARCHAR(500),date VARCHAR(255),ssid VARCHAR(10000));'''
#CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)

pathT='./CSV/NewMembersList.csv'
dfHis= Read_DataBase("MEMBERS_USERS_MANAGEMENT")
dfHis.to_csv(pathT,index=False)






key='key'
CSV_FILENAME="GroupName.csv"
TABLE_NAME="MEMBERS_WHATSAPP_GROUP"
createTableSchema='''(key VARCHAR(255) PRIMARY KEY,name VARCHAR(255),id VARCHAR(10000));'''
#CommonCreateAndUpdate_DataBase(CSV_FILENAME,TABLE_NAME,createTableSchema,key)

pathT='./CSV/GroupName.csv'
dfHis= Read_DataBase("MEMBERS_WHATSAPP_GROUP")
dfHis.to_csv(pathT,index=False)





