#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:05:47 2022

@author: pdm
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:56:32 2022

@author: pdm
"""

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import pandas as pd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib




def CustompdfGeneratorpdff(df):
    print("entered")
    if len(df)>0 and len(df['emailid'].iloc[0])>0:
        try:
            img=Image.open('../assets/mailimage.jpg')
            I1=ImageDraw.Draw(img)
            myfont=ImageFont.truetype('FreeMono.ttf',35)
            print("entered1")
            name=df['ssid'].iloc[0]
            I1.text((540,315),"Membership No:",font=myfont,fill=(255,255,0)) 
            I1.text((540,350),name,font=myfont,fill=(255,255,0)) 
           
            myfont=ImageFont.truetype('FreeMono.ttf',25)
            
            
            name=df['name'].iloc[0]
            I1.text((130,410),name,font=myfont,fill=(0,45,45))
            
            #*****************************************************#
            myfont=ImageFont.truetype('FreeMono.ttf',15)
            name=df['address'].iloc[0]
            I1.text((200,450),name.split(" ")[0],font=myfont,fill=(0,45,45))
            
            try:
                lenn=len(name.split(" ")[0])
                I1.text((200+10*lenn,450),name.split(" ")[1],font=myfont,fill=(0,45,45))
            except:
                pass
            
            try:
                lenn=lenn+len(name.split(" ")[1])
                I1.text((330+(10*lenn),450),name.split(" ")[2],font=myfont,fill=(0,45,45))
            except:
                pass
            try:
                lenn=lenn+len(name.split(" ")[2])
                I1.text((330+(10*lenn),450),name.split(" ")[3],font=myfont,fill=(0,45,45))
            except:
                pass
            try:
                lenn=lenn+len(name.split(" ")[3])
                I1.text((330+(10*lenn),450),name.split(" ")[4],font=myfont,fill=(0,45,45))
            except:
                pass
            
            
            
            myfont=ImageFont.truetype('FreeMono.ttf',18)
            
            name=df['statename'].iloc[0]
            I1.text((900,450),name,font=myfont,fill=(0,45,45))
            
            name=df['districtname'].iloc[0]
            I1.text((690,450),name,font=myfont,fill=(0,45,45))
            print("entered")
                    
            
            myfont=ImageFont.truetype('FreeMono.ttf',25)
            
            name=df['assemblyname'].iloc[0]
            I1.text((250,490),name,font=myfont,fill=(0,45,45))
            #*****************************************************#
            
            name=str(df['contactno'].iloc[0])
            I1.text((680,493),name,font=myfont,fill=(0,45,45))
            
            myfont=ImageFont.truetype('FreeMono.ttf',15)
            name=str(df['date'].iloc[0])
            I1.text((180,535),name.split(" ")[0],font=myfont,fill=(0,45,45))
            
            #img.show()
            img.save('../assets/mailimage1.jpg')
            

            

             
            print("entered")
            
            pdfname = '../assets/mailimage1.jpg'
            
           
            # bodyname = 'Hello'+" "+df['name']+''',
            
            # '''
            
            body='''
            
            ''' 'Dear ' + df['name'].iloc[0] +',\nYour Membership Details are: \n'+'Your membership Id is :'+ df['ssid'].iloc[0] + '\n your Registered Number is :'+str(df['contactno'].iloc[0]) + '''
            
            Please download the attched file for future reference
            From:
            Apna Dal S
            Team
            '''
                 

                    
                            
                          
                
                

            
            # put your email here
            
            sender = 'ajay.cse2004@gmail.com'
            # get the password in the gmail (manage your google account, click on the avatar on the right)
            # then go to security (right) and app password (center)
            # insert the password and then choose mail and this computer and then generate
            # copy the password generated here
            password = 'whgnysbsgusdexjw'
            # put the email of the receiver here
            receiver = df['emailid'].iloc[0]
       
             
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = 'Your e-Membership Details from ApnadalS Team'
         
            message.attach(MIMEText(body, 'plain'))
             
           
        
            # open the file in bynary
            binary_pdf = open(pdfname, 'rb')
             
            payload = MIMEBase('application', 'octate-stream', Name=pdfname)
            # payload = MIMEBase('application', 'pdf', Name=pdfname)
            payload.set_payload((binary_pdf).read())
             
            # enconding the binary into base64
            encoders.encode_base64(payload)
             
            # add header with pdf name
            payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
            message.attach(payload)
             
            #use gmail with port
            
            session = smtplib.SMTP('smtp.gmail.com', 587)
             
            #enable security
            session.starttls()
             
            #login with mail_id and password
            session.login(sender, password)
             
            text = message.as_string()
            session.sendmail(sender, receiver, text)
            session.quit()
            print('Mail Sent')
        
        except:
            print("Mail Sent error")







path='../CSV/NewMembersList.csv'
import os  
   
if os.path.exists(path):
   
        try:
            dfFile = pd.read_csv(path)
            #print("Read dfFile",dfFile)
       
        except :
            dfFile = pd.DataFrame()

print(dfFile[72:73])
CustompdfGeneratorpdff(dfFile[72:73])











