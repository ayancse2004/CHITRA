#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:41:04 2022

@author: pdm
"""

import datetime
import os
import pandas as pd

def ReadMembersListfromCSVCHECK():
    import os

    path='../CSV/NewMembersList.csv'
         
    if os.path.exists(path):
             
        try:
            dfFile = pd.read_csv(path)
            return dfFile
                 
        except :
            dfFile = pd.DataFrame()
            return dfFile
        
        
    dfFile = pd.DataFrame()
    return dfFile    

    
todaysDate=datetime.date.today().strftime('%d-%m-%y')
    
df=ReadMembersListfromCSVCHECK()
df['date'] = (pd.to_datetime(df['date'],format=('%d/%m/%Y %H:%M:%S')).dt.date).astype(str)

# df=df[df['districtname']=='SAHARANPUR']
# Dfsum=df.groupby('date').count()
# Dfsum['date'] = Dfsum.index

# Dfsum=Dfsum.reset_index(drop=True)
# print(Dfsum[['date','districtname']])

print(df['date'])

print(df['districtname'])

dfnew=df[df['districtname']=='CHITRAKOOT']
dfnew=dfnew.reset_index()

print(dfnew['statename'])



STATENAME=dfnew['statename'][0]
print(STATENAME)


dfnew=df[df['statename']==STATENAME]


Dfsum=dfnew.groupby('date').count()
Dfsum['date'] = Dfsum.index

print(Dfsum['date'])








