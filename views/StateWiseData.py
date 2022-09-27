#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:07:25 2022

@author: pdm
"""
import pandas as pd


PathT="./CSV/India_states.csv"
column_names=['ID','SEQ','STATE_CODE','STATE_NAME','DISTRICT_CODE','DISTRICT_NAME','SUB_DISTRICT_NAME']
df = pd.read_csv(PathT, delimiter=",", names=column_names)


def StateName():
    
    df1 = df.applymap(lambda s: s.upper() if type(s) == str else s)
    df1=df1[df1['STATE_NAME']!='STATE_NAME']
    df1=df1.dropna()
    
    return  df1['STATE_NAME'].unique()
    
  
    

def DistrictNameByStateName(DisName=None):
    df1 = df.applymap(lambda s: s.upper() if type(s) == str else s)
    
    df1=df1[df1['STATE_NAME']==DisName.upper()]
    df1=df1[df1['DISTRICT_NAME']!=DisName.upper()]
    df1=df1.dropna()
    
    return  df1['DISTRICT_NAME'].str.upper().unique()
    
def SubDistrictNameByStateName(DisName=None):
        df1 = df.applymap(lambda s: s.upper() if type(s) == str else s)
        
        df1=df1[df1['DISTRICT_NAME']==DisName.upper()]
        df1=df1[df1['SUB_DISTRICT_NAME']!=DisName.upper()]
        df1=df1.dropna()
        
        return  df1['SUB_DISTRICT_NAME'].str.upper().unique()
    
    
