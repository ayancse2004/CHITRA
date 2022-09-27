import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('config.txt')

#print(config.get('database', 'con'))

engine = create_engine(config.get('database', 'con'))


try:

   
    conn = engine.raw_connection()
    TableName="PART_NUMBER_DATABASE"
    
    with conn.cursor() as cur:
        col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
        col_names_str += "table_name = '{}';".format( TableName)
        cur.execute( col_names_str )
        
     
                
        col_names = ( cur.fetchall() )
        
      
        
        
        sql_query='''CREATE TABLE IF NOT EXISTS "user" (
            id int NOT NULL,
            username varchar(255) NOT NULL,
            email varchar(255) NOT NULL,
            password varchar(1000) NOT NULL,
            admin int NOT NULL DEFAULT '0',
            PRIMARY KEY (id),
            UNIQUE(username),
            UNIQUE(email)
            ) ;'''
        
        a=cur.execute(sql_query)
        
    
        cur.execute('''select * from "user";''')
       # print("The number of parts:Database ", cur.rowcount)
        tupples = cur.fetchall() 
        #print(tupples)
        
        cur.close()
        conn.commit()
except:
    print("An exception occurred") 
#print(col_names)




